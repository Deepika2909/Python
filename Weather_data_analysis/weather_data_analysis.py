import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have a CSV file named 'weather_data.csv' with the provided column names
# Replace 'weather_data.csv' with the actual file name or URL containing your data
df = pd.read_csv(r'C:\path\to\your\weather_data.csv')

# Drop non-numeric columns before calculating the correlation matrix
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
df_numeric = df[numeric_columns]

# Display basic information about the dataset
print(df_numeric.info())

# Display summary statistics of the numeric columns
print(df_numeric.describe())

# Check for missing values
print("Missing values:\n", df_numeric.isnull().sum())

# Visualize correlation matrix using a heatmap
correlation_matrix = df_numeric.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Add more analysis and plots based on your specific needs
