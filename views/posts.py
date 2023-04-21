import sqlite3
from models import Post


def get_all_posts():
    """gets all the posts"""
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content
        FROM posts p
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

            posts.append(post.__dict__)

    return posts
