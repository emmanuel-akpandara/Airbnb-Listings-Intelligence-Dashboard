import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Clean data
df = dataset.dropna(subset=['review_scores_rating', 'price'])


df['combo'] = df['property_type'] + ' - ' + df['room_type']


combo_stats = df.groupby('combo').agg({
    'price': 'mean',
    'review_scores_rating': 'mean',
    'combo': 'count'
}).rename(columns={'combo': 'count'}).reset_index()

#  price-to-rating ratio
combo_stats['price_to_rating'] = combo_stats['price'] / combo_stats['review_scores_rating']

# Filtering out combos with very few listings
combo_stats = combo_stats[combo_stats['count'] > 5]

# Sort by best value
best_combos = combo_stats.sort_values('price_to_rating').head(10)


plt.figure(figsize=(12, 7))
sns.set_style("whitegrid")
barplot = sns.barplot(
    data=best_combos,
    x='price_to_rating',
    y='combo',
    palette='viridis'
)


barplot.set_title('Top Property + Room Type Combos\n(Best Price-to-Rating Ratio)', fontsize=20)
barplot.set_xlabel('Price / Rating', fontsize=16)
barplot.set_ylabel('Property - Room Combo', fontsize=16)
barplot.tick_params(labelsize=16)

plt.tight_layout()
plt.show()

