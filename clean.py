import pandas as pd

def clean_prices(df):
    df['price'] = pd.to_numeric(df['price'].str.replace('[^0-9.]','', regex=True), errors='coerce')
    df = df.dropna(subset=['price'])
    return df

def clean_availability(df):
    # convert availability to simple boolean
    df['in_stock'] = df['availability'].apply(lambda x: True if 'In stock' in x else False)
    df.drop('availability', axis=1, inplace=True)
    return df

# Load raw data
books = pd.read_csv("data/raw_books.csv")

# Apply cleaning
books = clean_prices(books)
books = clean_availability(books)

# Remove duplicates
books.drop_duplicates(inplace=True)

# Fix column names
books.columns = books.columns.str.strip().str.lower()

# Save cleaned data
books.to_csv("data/cleaned_books.csv", index=False)
print("Cleaning completed ")