import sqlite3
from models import Category


def get_all_categories():
    """gets all the categories"""
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT 
            c.id,
            c.label
        FROM categories c
        ORDER BY c.label ASC
        """)

        # Initialize an empty list to hold all customer representations
        categories = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            category = Category(
                row['id'],
                row['label']
            )

            categories.append(category.__dict__)

    return categories

def create_category(new_category):
    '''create new category'''
    with sqlite3.connect("./db.sqlite3") as conn:
        # conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Categories
            (label)
        VALUES
            ( ? );
        """, (new_category['label'], ))
        id = db_cursor.lastrowid
        new_category['id'] = id

    return new_category