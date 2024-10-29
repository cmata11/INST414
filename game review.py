import pandas as pd
import re

# Read the CSV file
df = pd.read_csv("merged_data.csv")

# Function to extract number of reviews from text description
def extract_review_count(text):
    if pd.isna(text):
        return 0
    match = re.search(r'of the ([\d,]+) user reviews', text)
    if match:
        return int(match.group(1).replace(',', ''))
    return 0

# Function to extract percentage from text description
def extract_percentage(text):
    if pd.isna(text):
        return 0
    match = re.search(r'(\d+)% of the', text)
    if match:
        return int(match.group(1))
    return 0

# Create new columns with extracted data
df['review_count'] = df['All Reviews Number'].apply(extract_review_count)
df['review_percentage'] = df['All Reviews Number'].apply(extract_percentage)

# Filter for games with more than 100,000 reviews and sort by percentage
filtered_df = df[df['review_count'] > 100000].sort_values(by="review_percentage", ascending=False)

# Display filtered results
top_reviews = filtered_df[["Title", "All Reviews Number", "review_count", "review_percentage"]].head(50)

print("Top Titles (Games with 100,000+ reviews):")
print("-" * 80)
for index, row in top_reviews.iterrows():
    print(f"Title: {row['Title']}")
    print(f"Positive Reviews: {row['review_percentage']}%")
    print(f"Total Reviews: {row['review_count']:,}")
    print("-" * 80)

# Print summary statistics
print(f"\nTotal number of games with over 100,000 reviews: {len(filtered_df)}")