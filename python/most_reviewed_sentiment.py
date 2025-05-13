
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

df = dataset.dropna(subset=['comments'])

most_reviewed_listing = (
    df.groupby('name')['review_id']
    .count()
    .sort_values(ascending=False)
    .idxmax()
)

# Filter only comments for the most reviewed listing
most_reviewed_df = df[df['name'] == most_reviewed_listing]

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

most_reviewed_df['sentiment'] = most_reviewed_df['comments'].apply(get_sentiment)

sentiment_counts = most_reviewed_df['sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['Sentiment', 'Count']

plt.figure(figsize=(8, 5))
bars = plt.bar(sentiment_counts['Sentiment'], sentiment_counts['Count'], color=['green', 'orange', 'red'])

# Optional styling
plt.title(f"Sentiment Distribution for Most Reviewed Listing:\n{most_reviewed_listing}", fontsize=20)
plt.xlabel("Sentiment", fontsize=14)
plt.ylabel("Number of Comments", fontsize=14)
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)

# Add value labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, int(yval), ha='center', fontsize=14)

plt.tight_layout()
plt.show()
