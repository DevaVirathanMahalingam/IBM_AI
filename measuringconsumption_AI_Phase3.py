import pandas as pd

# Step 2: Load and Combine CSV Files
file_paths = ['COMED_hourly.csv','DAYTON_hourly.csv','DEOK_hourly.csv', 'DOM_hourly.csv','DUQ_hourly.csv','EKPC_hourly.csv','FE_hourly.csv','NI_hourly.csv','pjm_hourly_est.csv','PJM_Load_hourly.csv','PJME_hourly.csv']
data_frames = [pd.read_csv(file) for file in file_paths]

# Combine the data frames into a single DataFrame
combined_data = pd.concat(data_frames, ignore_index=True , sort=False)

# Step 3: Preprocessing
# Handle missing values (e.g., fill with mean for numeric columns)
combined_data.fillna(combined_data.mean(), inplace=True)

# Convert data types if needed (e.g., date columns to datetime)
combined_data['date_column'] = pd.to_datetime(combined_data['date_column'])

# Encode categorical variables (if any)
combined_data = pd.get_dummies(combined_data, columns=['categorical_column'])

# Normalize or scale numerical features (e.g., Min-Max scaling)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
numeric_columns = ['column1', 'column2']  # Replace with your numeric columns
combined_data[numeric_columns] = scaler.fit_transform(combined_data[numeric_columns])

# Step 4: Data Exploration
# Optionally, explore the combined dataset using Pandas functions, e.g., combined_data.head(), combined_data.describe(), etc.

# Save the preprocessed data to a new CSV file (optional)
print(combined_data.iloc[:2,:2])
