import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

def get_top_expensive_books(db_name="database.db", table_name="books", top_n=5):
    conn = sqlite3.connect(db_name)
    query = f"SELECT title, price FROM {table_name} ORDER BY price DESC LIMIT {top_n}"
    top_books = pd.read_sql(query, conn)
    conn.close()
    return top_books

# Get top 5 expensive books
top_books = get_top_expensive_books()
print("Top 5 Expensive Books:")
print(top_books)

# Save analysis
top_books.to_csv("data/top_books.csv", index=False)
print("Analysis saved ")

#plot bar chart for top 5 expensive books
plt.figure(figsize=(12,6))
sns.set_style("whitegrid")

bars = sns.barplot(
    y=top_books['title'].str.wrap(25), 
    x='price', 
    data=top_books, 
    palette="viridis"
)

for bar in bars.patches:
    plt.text(
        bar.get_width() + 1, 
        bar.get_y() + bar.get_height()/2,
        f'£{bar.get_width():.2f}',
        va='center'
    )

plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.title("Top 5 Most Expensive Books")
plt.tight_layout()
plt.show()