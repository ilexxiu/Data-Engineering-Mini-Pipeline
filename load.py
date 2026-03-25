import pandas as pd
import sqlite3


def load_to_db(df, db_name="database.db", table_name="books"):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"Data loaded into {db_name} successfully ")

# Read CSV file
books_cleaned = pd.read_csv("data/cleaned_books.csv")

# Load data into database
load_to_db(books_cleaned)

# Check if 'books' table exists
conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books';")
table_exists = cursor.fetchone()
conn.close()

if table_exists:
    print("The 'books' table exists in the database")
else:
    print("The 'books' table does NOT exist ")