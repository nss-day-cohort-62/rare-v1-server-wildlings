import sqlite3
from models import Tag


def get_all_tags():
    """gets all the tags"""
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT 
          t.id,
          t.label
        FROM tags t
        ORDER BY t.label COLLATE NOCASE ASC
        """)

        # Initialize an empty list to hold all customer representations
        tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            tag = Tag(
                row['id'],
                row['label']
            )

            tags.append(tag.__dict__)

    return tags


def create_tag(new_tag):
    '''create new tag'''
    with sqlite3.connect("./db.sqlite3") as conn:
        # conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags
            (label)
        VALUES
            ( ? );
        """, (new_tag['label'], ))
        id = db_cursor.lastrowid
        new_tag['id'] = id

    return new_tag
