import pandas as pd

# Assuming 'df' is the DataFrame loaded from the previous step (Step 2)
# Grouping the data by the 'country' column and calculating the average value of 'Rate'

# Step 1: Group by 'country' and calculate average 'Rate'
country_avg_rate = df.groupby('country')['Rate'].mean().reset_index()

# Display the result
print("Average 'Rate' for each country:")
print(country_avg_rate)

# Equivalent SQL Query:
# SELECT country, AVG(Rate) AS avg_rate
# FROM tourism_dataset
# GROUP BY country;

# Step 2: Identify top 3 categories with the highest average 'Rate' across all countries
# Assuming 'category' column exists, group by 'category' and calculate the average 'Rate'
top_categories = df.groupby('category')['Rate'].mean().sort_values(ascending=False).head(3).reset_index()

# Display the top 3 categories
print("\nTop 3 categories with the highest average 'Rate':")
print(top_categories)

# Equivalent SQL Query:
# SELECT category, AVG(Rate) AS avg_rate
# FROM tourism_dataset
# GROUP BY category
# ORDER BY avg_rate DESC
# LIMIT 3;
