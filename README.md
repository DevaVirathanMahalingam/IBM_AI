Data Loading and Preprocessing

Load multiple CSV files containing hourly energy consumption data for different regions.
Fill missing values in the dataset with the mean of each column.
Convert the date column to datetime format for time-based analysis.
Perform one-hot encoding for categorical columns in the dataset.
Scale numeric columns using Min-Max scaling to standardize the data.
Time Series Data Visualization

Plot the energy consumption data over time for two selected numeric columns (e.g., 'column1' and 'column2').
Create a line plot to visualize the trend in energy consumption.
Add labels, a title, and a legend to the plot for better understanding.
Correlation Matrix Visualization

Calculate the correlation matrix for all columns in the dataset.
Visualize the correlation matrix as a heatmap to understand the relationships between variables.
Use a color scale to represent the strength of correlations.
Prerequisites
Before using this code, make sure you have the following:

Python installed on your system (version 3.x recommended).

Required Python packages installed. You can install them using pip:





How to Use
Place your CSV files containing energy consumption data in the same directory as this script or specify the file paths in the file_paths list.

Replace the placeholder column names ('column1', 'column2', 'date_column', 'categorical_column') in the code with the actual column names from your dataset.

Run the script in a Python environment. You can execute it using a Python IDE or from the command line:




The script will load, preprocess, and visualize the energy consumption data.

The time series plot will show the trend in energy consumption over time for the selected columns.

The correlation matrix heatmap will help you identify relationships between variables in the dataset.





Customization
You can customize the script to load different datasets or change the visualization settings to suit your specific data and analysis needs.

Adjust the numeric columns, date column, and categorical columns as needed in the code.

Modify the plotting settings, such as plot labels, titles, and colors, for the best representation of your data.

