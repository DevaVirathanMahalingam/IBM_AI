import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Load the data
file_paths = ['COMED_hourly.csv', 'DAYTON_hourly.csv', 'DEOK_hourly.csv', 'DOM_hourly.csv', 'DUQ_hourly.csv', 'EKPC_hourly.csv', 'FE_hourly.csv', 'NI_hourly.csv', 'pjm_hourly_est.csv', 'PJM_Load_hourly.csv', 'PJME_hourly.csv']
data_frames = [pd.read_csv(file) for file in file_paths]
combined_data = pd.concat(data_frames, ignore_index=True, sort=False)

# Fill missing values with column means
combined_data.fillna(combined_data.mean(), inplace=True)

# Convert the date column to datetime
combined_data['date_column'] = pd.to_datetime(combined_data['date_column'])

# Perform one-hot encoding for categorical columns
combined_data = pd.get_dummies(combined_data, columns=['categorical_column'])

# Define the numeric columns to be scaled
numeric_columns = ['column1', 'column2']

# Scale numeric columns using Min-Max scaling
scaler = MinMaxScaler()
combined_data[numeric_columns] = scaler.fit_transform(combined_data[numeric_columns])

# Print the first 2 rows and 2 columns of the DataFrame
print(combined_data.iloc[:2, :2])

# Plot time series data
plt.figure(figsize=(12, 6))
plt.plot(combined_data['date_column'], combined_data['column1'], label='Column1')
plt.plot(combined_data['date_column'], combined_data['column2'], label='Column2')
plt.xlabel('Date')
plt.ylabel('Energy Consumption')
plt.title('Energy Consumption Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Calculate and visualize the correlation matrix
correlation_matrix = combined_data.corr()
plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.title('Correlation Matrix')
plt.xticks(range(len(correlation_matrix.columns), correlation_matrix.columns, rotation='vertical')
plt.yticks(range(len(correlation_matrix.columns), correlation_matrix.columns)
plt.show()
