import pandas as pd
file_paths = [&#39;COMED_hourly.csv&#39;,&#39;DAYTON_hourly.csv&#39;,&#39;DEOK_hourly.csv&#39;,
&#39;DOM_hourly.csv&#39;,&#39;DUQ_hourly.csv&#39;,&#39;EKPC_hourly.csv&#39;,&#39;FE_hourly.csv&#39;,&#39;NI_
hourly.csv&#39;,&#39;pjm_hourly_est.csv&#39;,&#39;PJM_Load_hourly.csv&#39;,&#39;PJME_hourly.csv&#39;]
data_frames = [pd.read_csv(file) for file in file_paths]
combined_data = pd.concat(data_frames, ignore_index=True , sort=False)
combined_data.fillna(combined_data.mean(), inplace=True)
combined_data[&#39;date_column&#39;] =
pd.to_datetime(combined_data[&#39;date_column&#39;])
combined_data = pd.get_dummies(combined_data,
columns=[&#39;categorical_column&#39;])
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
numeric_columns = [&#39;column1&#39;, &#39;column2&#39;]  # Replace with your numeric
columns
combined_data[numeric_columns] =
scaler.fit_transform(combined_data[numeric_columns])
print(combined_data.iloc[:2,:2])
import pandas as pd
import matplotlib.pyplot as plt
summary_stats = combined_data.describe()
plt.figure(figsize=(12, 6))
plt.plot(combined_data[‘date_column’], combined_data[‘column1’],
label=’Column1’)

plt.plot(combined_data[‘date_column’], combined_data[‘column2’],
label=’Column2’)
plt.xlabel(‘Date’)
plt.ylabel(‘Energy Consumption’)
plt.title(‘Energy Consumption Over Time’)
plt.legend()
plt.grid(True)
plt.show()

correlation_matrix = combined_data.corr()
plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap=’coolwarm’, interpolation=’none’)
plt.colorbar()
plt.title(‘Correlation Matrix’)
plt.xticks(range(len(correlation_matrix.columns), correlation_matrix.columns,
rotation=’vertical’)
plt.yticks(range(len(correlation_matrix.columns), correlation_matrix.columns)
plt.show()