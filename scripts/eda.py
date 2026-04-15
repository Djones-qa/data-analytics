import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/sales.csv')

print('Dataset Info:')
print(df.info())

print('\nSummary Statistics:')
print(df.describe())

print('\nMissing Values:')
print(df.isnull().sum())

df['date'] = pd.to_datetime(df['date'])
sales_by_day = df.groupby(df['date'].dt.date)['total_amount'].sum()

plt.figure(figsize=(12,5))
sales_by_day.plot(kind='line', title='Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('visuals/daily_sales_trend.png')
plt.show()

top_products = df.groupby('product_name')['total_amount'].sum().sort_values(ascending=False).head(10)
print('\nTop Products:')
print(top_products)

plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Top 10 Products by Revenue')
plt.xlabel('Revenue')
plt.ylabel('Product')
plt.tight_layout()
plt.savefig('visuals/top_products.png')
plt.show()
