# Airbnb Listings & Review Intelligence Dashboard

A Business Intelligence project built with Power BI and Python to analyze Airbnb listings across major Belgian cities. It uncovers trends in review sentiment, pricing, host behavior, and prescriptive recommendations for property improvement.

##  Dataset

Source: Provided by Thomas More University for a semester project
        uploaded here: <a href="https://www.kaggle.com/datasets/emmanuelakpandara/airbnb-belgium-dataset">Link</a>

### Tables used:

fact_Listing: Contains listing ID, price, rating, host_id, minimum nights

dim_Review: User comments and ratings

dim_Host: Host metadata (host_id, host_name)

dim_City: City-level location

dim_Neighbourhood: Neighbourhood metadata linked to city

Sample data files available in /data

##  Data Preparation (Power Query)

### Key steps:
<ul></ul>
Merged listing and review data to enrich each record

Removed nulls in comments, ratings, and price

Created new columns:

Sentiment (via Python + TextBlob)

Combo = property_type + room_type

Established relationships via a clean star schema (fact-listing at center)

Power Query transformations available in the .pbix file and described in /docs/schema.md

## Sentiment Analysis (Python)

Used Python in Power Query to label sentiment per comment:

from textblob import TextBlob
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

Output used to:
<ul></ul>
Visualize sentiment distribution per city

Highlight negative reviews for diagnostic analysis

Drive topic modeling and improvement suggestions

See full script in /python/sentiment_analysis.py

## Dashboard Overview (4 Pages)

### Page 1: Overview & Descriptive Stats

KPIs: Total hosts, listings, average price

Top-rated and most expensive listings

Listings per city and per property type

### Page 2: Location Quality (Diagnostic)

Avg rating per city

5-star review ratio by city

Scatter plot: review count vs. rating

Insight: "Ghent has fewer 5-star listings, but a tighter distribution. Antwerp shows higher variance."

### Page 3: Property Performance

Avg minimum nights per city

Price vs. stay duration

Combo chart: property + room type vs. rating

Best value-for-money combinations

### Page 4: Diagnostic + Sentiment

Listings per host

Avg rating per host

Word cloud of common negative review themes (Python LDA)

Sentiment per city

### Key Insights

Ghent had the highest average review score at 4.72

Antwerp had more 5-star reviews, but less consistency

Hosts with more listings showed slightly lower average ratings

Cleanliness and communication were the most common negative themes

📄 Files & Structure

/airbnb-review-dashboard
├── README.md
├── AirbnbListings.pbix              # Power BI file
├── AirbnbListings.pdf               # Published dashboard (PDF)
├── /data                            # Sample reviews and listings
│   └── reviews_sample.csv
├── /visuals                         # Screenshots for preview
├── /python                          # Scripts for NLP, sentiment, topic modeling
│   └── sentiment_analysis.py
│   └── lda_topic_modeling.py
├── /docs                            # Schema diagrams, notes
└── LICENSE

## Getting Started

Clone this repository

Open AirbnbListings.pbix in Power BI Desktop

[Optional] Run scripts in /python to regenerate or experiment with sentiment analysis
