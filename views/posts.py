import sqlite3
from models import Post, Category, User


def get_all_posts(query_params):
    """gets all the posts"""
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        where_clause = ""

        if len(query_params) != 0:
            param = query_params[0]
            [qs_key, qs_value] = param.split("=")

            if qs_key == "_user":
                where_clause = f"WHERE p.user_id = {qs_value}"

        # Write the SQL query to get the information you want
        db_cursor.execute(f"""
        SELECT 
            p.id,
            p.title,
            p.publication_date,
            p.content,
            c.id category_id,
            c.label,
            u.id user_id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Posts p 
        JOIN Categories c 
            ON c.id = p.category_id
        JOIN Users u 
            ON u.id = p.user_id
            {where_clause}
        ORDER BY p.publication_date DESC 
        """)

        # Initialize an empty list to hold all customer representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            post = Post(
                row['id'],
                row['user_id'],
                row['category_id'],
                row['title'],
                row['publication_date'],
                row['content']
            )

            category = Category(row["category_id"], row["label"])

            user = User(row["user_id"], row["first_name"], row["last_name"], row["email"], row["bio"],
                        row["username"], row["password"], row["profile_image_url"], row["created_on"], row["active"])

            post.category = category.__dict__

            post.user = user.__dict__

            posts.append(post.__dict__)

    return posts


def get_single_post(id):
    """get a single post"""
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT 
            p.id,
            p.title,
            p.publication_date,
            p.content,
            c.id category_id,
            c.label,
            u.id user_id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Posts p 
        JOIN Categories c 
            ON c.id = p.category_id
        JOIN Users u 
            ON u.id = p.user_id
        WHERE p.id = ?
        ORDER BY p.publication_date DESC 
        """, (id, ))

        # Convert rows of data into a Python list
        data = db_cursor.fetchone()

        # Iterate list of data returned from database

        post = Post(
            data['id'],
            data['user_id'],
            data['category_id'],
            data['title'],
            data['publication_date'],
            data['content']
        )

        category = Category(data["category_id"], data["label"])

        user = User(data["user_id"], data["first_name"], data["last_name"], data["email"], data["bio"],
                    data["username"], data["password"], data["profile_image_url"], data["created_on"], data["active"])

        post.category = category.__dict__

        post.user = user.__dict__

    return post.__dict__


def create_post(new_post):
    '''create a new post'''

    with sqlite3.connect("./db.sqlite3") as conn:
        # conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts ( user_id, category_id, title, publication_date, content)
        VALUES
        ( ?,?,?,?,?)""", (new_post["user_id"], new_post["category_id"], new_post["title"], new_post["publication_date"], new_post["content"]))

        id = db_cursor.lastrowid
        new_post['id'] = id

    return new_post


def delete_post(id):
    """Deletes single post"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM posts
        WHERE id = ?
        """, (id, ))


def update_post(id, new_post):
    """Updates Post with Replacement"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE posts
            SET
                user_id = ?,
                category_id = ?,
                title = ?,
                publication_date = ?,
                content = ?
        WHERE id = ?
        """, (
            new_post['user_id'],
            new_post['category_id'],
            new_post['title'],
            new_post['publication_date'],
            new_post['content'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
