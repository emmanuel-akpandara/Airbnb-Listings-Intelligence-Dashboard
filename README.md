# Airbnb Listings & Review Intelligence Dashboard

A Business Intelligence project built with Power BI and Python to analyze Airbnb listings across major Belgian cities. It uncovers trends in review sentiment, pricing, host behavior, and prescriptive recommendations for property improvement.

##  Dataset

Source: Provided by Thomas More University for a semester project
        <a href="https://www.kaggle.com/datasets/emmanuelakpandara/airbnb-belgium-dataset">Link</a>

### Tables used:

fact_Listing: Contains listing ID, price, rating, host_id, minimum nights

dim_Review: User comments and ratings

dim_Host: Host metadata (host_id, host_name)

dim_City: City-level location

dim_property_type: The type of property a listing can have along with a subcategory of room types

dim_Neighbourhood: names of Neighbourhoods of each city

Sample data files available in /dataset

##  Data Preparation (Power Query)

The dataset contains separate folders for each city, Brussels, Ghent, and Antwerp and each folder includes the same types of Excel files (e.g., listings.csv, reviews.csv, etc.), but with data specific to that city.

To unify the data:
<ul>

<li>I loaded each worksheet individually into Power Query (e.g., antwerp_listings, ghent_listings, brussels_listings).</li>

<li>For each city’s file, I selected only the relevant columns (e.g., price, review score, room type).</li>

<li>I then appended the three city-level queries together for each worksheet type (e.g., all listings → fact_Listing, all reviews → dim_Review).</li>

<li>This process was repeated across each worksheet type to build consolidated tables that cover all three cities in one unified format.</li>

<li>These final tables were used to build a clean star schema, with fact_Listing at the center and dimensions like city, host, review, and property type.</li>

<li>Result: one centralized dataset that supports cross-city analysis in a consistent structure.</li>
</ul>
Removed nulls in comments, ratings, and price


Established relationships via a clean star schema (fact-listing at center)

Power Query transformations available in the .pbix file and described in /schema

## Sentiment Analysis (Python)

Goal: Enrich the review data by identifying the tone (positive, neutral, negative) of user comments and extract actionable insights from guest feedback.

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

### Limitation & Improvement:
While TextBlob is lightweight and easy to integrate, it has limitations in context awareness and multilingual support, especially for nuanced or Dutch reviews.
For improved accuracy, a future enhancement would involve using pretrained language models (e.g., BERT, RoBERTa, or multilingual LLMs) to generate more accurate and context-aware sentiment labels — ideally decoupled from Power BI and used to batch-process sentiment offline before loading into the model.

## Python Scripts Used:
### /python/most_reviewed_sentiment.py
#### What it does:
Identifies the most-reviewed listing and analyzes the sentiment distribution of its comments (positive, neutral, negative).

#### Why it’s useful:
This allows hosts and stakeholders to understand how guests feel about the most frequently booked listing — a potential benchmark or red flag. It also supports diagnostic storytelling by focusing on a high-volume case.

### /python/property_rating_ratio.py
#### What it does:
Calculates the average price-to-rating ratio for each property_type + room_type combination (e.g., "Apartment - Private Room") and shows the top 10 combos with the best value (filtered by minimum volume).

#### Why it’s useful:
It reveals which property configurations offer the best guest satisfaction relative to price, helping hosts and investors make better listing decisions. This supports prescriptive insight, turning data into recommendations.

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

Sentiment per city

### Key Insights

Ghent had the highest average review score at 4.72

Antwerp had more 5-star reviews, but less consistency

Hosts with more listings showed slightly lower average ratings

Cleanliness and communication were the most common negative themes

## Getting Started

Clone this repository

Open AirbnbListings.pbix in Power BI Desktop

[Optional] Run scripts in /python to regenerate or experiment 
