import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Load the Data
df = pd.read_csv(r"C:\Users\deepika\Downloads\basic\basic\weather.csv")

# Step 2: Data Exploration
print(df.head())
print(df.info())
print(df.describe())

# Step 3: Data Visualization
sns.pairplot(df[['MinTemp', 'MaxTemp', 'Rainfall']])
plt.show()

# Step 4: Feature Engineering (if needed)

# Step 5: Data Analysis (analyze each term)
# Example: Calculate average MaxTemp by month
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
monthly_avg_max_temp = df.groupby('Month')['MaxTemp'].mean()

# Analyze Rainfall by Month
monthly_total_rainfall = df.groupby('Month')['Rainfall'].sum()

# Analyze Rainfall by Location
location_rainfall = df.groupby('Location')['Rainfall'].mean().sort_values(ascending=False)

# Step 6: Data Visualization (Part 2)
plt.figure(figsize=(15, 5))

# Plot Monthly Average Max Temperature
plt.subplot(1, 3, 1)
plt.plot(monthly_avg_max_temp.index, monthly_avg_max_temp.values, marker='o')
plt.xlabel('Month')
plt.ylabel('Average Max Temperature')
plt.title('Monthly Average Max Temperature')
plt.grid(True)

# Plot Monthly Total Rainfall
plt.subplot(1, 3, 2)
plt.bar(monthly_total_rainfall.index, monthly_total_rainfall.values)
plt.xlabel('Month')
plt.ylabel('Total Rainfall')
plt.title('Monthly Total Rainfall')
plt.grid(True)

# Plot Location-wise Average Rainfall
plt.subplot(1, 3, 3)
location_rainfall.plot(kind='bar', color='skyblue')
plt.xlabel('Location')
plt.ylabel('Average Rainfall')
plt.title('Average Rainfall by Location')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()

# Plotting Distribution of Rainfall
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(df['Rainfall'], bins=30, kde=True)
plt.title('Distribution of Rainfall')
plt.xlabel('Rainfall')
plt.ylabel('Frequency')

# Box plot of Rainfall by Month
plt.subplot(1, 2, 2)
sns.boxplot(x='Month', y='Rainfall', data=df)
plt.title('Boxplot of Rainfall by Month')
plt.xlabel('Month')
plt.ylabel('Rainfall')

plt.tight_layout()
plt.show()

# Step 7 (continued): Advanced Analysis (e.g., predict Rainfall)
# Continue with the previous code...

# Step 8 (continued): Conclusions and Insights (analyze each term)
# Example: Identify the highest and lowest rainfall months
highest_rainfall_month = monthly_avg_max_temp.idxmax()
lowest_rainfall_month = monthly_avg_max_temp.idxmin()
print(f'Highest rainfall month: {highest_rainfall_month}, Lowest rainfall month: {lowest_rainfall_month}')
