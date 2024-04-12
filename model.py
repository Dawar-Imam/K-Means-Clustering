from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

################################################################# Q1
# Import the dataset
data = pd.read_csv("userbehaviour.csv")

# Check for null values
null_values = data.isnull().sum()
print("Null values in the dataset:\n", null_values)

# Display column information
column_info = data.info()
print("\nColumn information:\n", column_info)

# Display descriptive statistics
descriptive_stats = data.describe()
print("\nDescriptive statistics:\n", descriptive_stats)

################################################################# Q2 n Q3

# Highest screen time
highest_screen_time = data['Average Screen Time'].max()
print("Highest screen time:", highest_screen_time)

# Lowest screen time
lowest_screen_time = data['Average Screen Time'].min()
print("Lowest screen time:", lowest_screen_time)

# Average screen time
average_screen_time = data['Average Screen Time'].mean()
print("Average screen time:", average_screen_time)
#Task 3 - Check the highest, lowest, and average amount spent by all users:

# Highest amount spent
highest_amount_spent = data['Average Spent on App (INR)'].max()
print("Highest amount spent:", highest_amount_spent)

# Lowest amount spent
lowest_amount_spent = data['Average Spent on App (INR)'].min()
print("Lowest amount spent:", lowest_amount_spent)

# Average amount spent
average_amount_spent = data['Average Spent on App (INR)'].mean()
print("Average amount spent:", average_amount_spent)

################################


# Separate data for installed and uninstalled users
installed_users = data[data['Status'] == 'Installed']
uninstalled_users = data[data['Status'] == 'Uninstalled']

# Create a bubble graph
plt.figure(figsize=(12, 8))
plt.scatter(installed_users['Average Screen Time'], installed_users['Average Spent on App (INR)'], 
            s=installed_users['Ratings']*10, c='blue', alpha=0.5, label='Installed')
plt.scatter(uninstalled_users['Average Screen Time'], uninstalled_users['Average Spent on App (INR)'], 
            s=uninstalled_users['Ratings']*10, c='red', alpha=0.5, label='Uninstalled')

plt.ylabel('Average Spent on App (INR)')
plt.xlabel('Average Screen Time')
plt.title('Spending Capacity vs Screen Time')
plt.legend()
plt.grid(True)
plt.show()


#####################################

# Separate data for installed and uninstalled apps
installed_apps = data[data['Status'] == 'Installed']
uninstalled_apps = data[data['Status'] == 'Uninstalled']

# Create the bubble graph
plt.figure(figsize=(12, 8))

# Plot installed apps in blue
plt.scatter(installed_apps['Average Screen Time'], installed_apps['Ratings'], 
            s=installed_apps['Average Spent on App (INR)']*.4, c='blue', alpha=0.5, label='Installed Apps')

# Plot uninstalled apps in red
plt.scatter(uninstalled_apps['Average Screen Time'], uninstalled_apps['Ratings'], 
            s=uninstalled_apps['Average Spent on App (INR)']*.4, c='red', alpha=0.5, label='Uninstalled Apps')

plt.xlabel('Average Screen Time')
plt.ylabel('Ratings')
plt.title('Ratings vs Screen Time Bubble Graph')
plt.legend()
plt.grid(True)
plt.show()

#################################


# Load the user behavior dataset

# Selecting features for clustering
# data.drop('userid', axis=1, inplace=True)

# Convert 'Status' column values into numbers
label_encoder = LabelEncoder()
data['Status'] = label_encoder.fit_transform(data['Status'])

# Selecting features for clustering
# X = data.drop('Status', axis=1)  # Exclude the 'Status' column for clustering

# Perform K-means clustering with k=2 (you can adjust k as needed)
# Perform K-means clustering with k=3
kmeans = KMeans(n_clusters=3, random_state=0).fit(data.drop(['userid'], axis=1))

# Add a new column to the dataframe to store the cluster labels
data['Cluster'] = kmeans.labels_

# # Visualize the clusters

# Define colors for each cluster
# Define colors for each cluster
colors = {0: 'blue', 1: 'green', 2: 'red'}
cluster_labels = {0: 'Retained', 1: 'Churn', 2: 'Needs Attention'}

# Visualize the segments
plt.figure(figsize=(12, 8))

# Plot each cluster with a different color
for cluster_num, color in colors.items():
    cluster_data = data[data['Cluster'] == cluster_num]
    plt.scatter(cluster_data['Last Visited Minutes'], cluster_data['Average Spent on App (INR)'], c=color, label=cluster_labels[cluster_num], s=50)

plt.ylabel('Average Spent on App (INR)')
plt.xlabel('Last Visited Minutes')
plt.title('User Segmentation with K-means Clustering')
plt.legend()
plt.show()

