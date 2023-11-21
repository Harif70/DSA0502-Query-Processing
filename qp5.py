import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Date': ['2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06'],
    'Trading_Volume': [1000000, 1200000, 800000, 1500000, 1100000]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
start_date = '2023-01-02'
end_date = '2023-01-06'
filtered_data = df[start_date:end_date]
plt.figure(figsize=(12, 6))
plt.bar(filtered_data.index, filtered_data['Trading_Volume'], color='b', alpha=0.7)
plt.title('Alphabet Inc. Trading Volume')
plt.xlabel('Date')
plt.ylabel('Trading Volume')
plt.grid(axis='y')
plt.show()
