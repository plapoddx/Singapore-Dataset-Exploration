import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('visit.csv')

# Select Southeast Asia data
southeast_asia = df[df['DataSeries'] == 'Southeast Asia']

# Select columns from October 2022 to June 2023
start_col = '2022Oct'
end_col = '2023Jun'

# Get all columns between start_col and end_col (inclusive)
selected_cols = df.columns[df.columns.get_loc(start_col):df.columns.get_loc(end_col) + 1]
selected_data = southeast_asia[selected_cols]

# Create a line plot
plt.figure(figsize=(12, 6))

# Plot the data
values = selected_data.iloc[0].astype(float)
plt.plot(range(len(selected_cols)), values, marker='o', linewidth=2, markersize=8)

# Customize the plot
plt.title('Southeast Asia Visitor Arrivals (October 2022 - June 2023)')
plt.xlabel('Month')
plt.ylabel('Number of Visitors')

# Set x-axis ticks and labels
plt.xticks(range(len(selected_cols)), selected_cols, rotation=45)
plt.grid(True)

# Add value labels on the points
for i, (x, y) in enumerate(zip(selected_cols, values)):
    plt.annotate(f'{int(y):,}', 
                (i, y),
                textcoords="offset points",
                xytext=(0,10),
                ha='center')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()

# Print the data
print("\nData used for plotting:")
print(selected_data) 