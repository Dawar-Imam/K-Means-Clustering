# K-Means Clustering

## Introduction

K-means clustering is an unsupervised machine learning algorithm used to partition a dataset into distinct groups, or clusters, based on similarities between data points. The algorithm iteratively assigns data points to the nearest cluster centroid and updates centroids based on the mean of the assigned points. It aims to minimize variance within clusters and maximize variance between clusters. K-means is computationally efficient and widely used in various applications, but it requires the number of clusters to be predefined and can be sensitive to initial centroids and outliers.

The following project uses K-Means Clustering for group users based on how they engage with an application. A detailed description about the dataset will be described later.

## Requirements

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Dataset Description

The dataset "userbehaviour.csv" consists of user behavior data related to an application. It includes various features that capture different aspects of user engagement and interaction with the app. Some key features in the dataset are:

```bash
userid:                     Unique identifier for each user in the dataset.
Average Screen Time:        The average amount of time a user spends on the application.
Average Spent on App (INR): The average amount of money spent by the user on the application.
Left Review:                Indicates whether the user left a review about their experience on the application (1 for true, 0 for false).
Ratings:                    The ratings given by the user to the application.
New Password Request:       The number of times the user requested a new password.
Last Visited Minutes:       Minutes passed since the user was last active on the application.
Status:                     Indicates whether the application is installed or uninstalled by the user.
```

The goal here is to perform app user segmentation based on user behavior data using the K-means clustering algorithm. The dataset provided contains information about how users engage with the application, including metrics such as average screen time, amount spent on the app, ratings given, and more.


```bash
Descriptive statistics:
             userid  Average Screen Time  Average Spent on App (INR)  Left Review     Ratings  New Password Request  Last Visited Minutes
count   999.000000           999.000000                  999.000000   999.000000  999.000000            999.000000            999.000000
mean   1500.000000            24.390390                  424.415415     0.497497    6.513514              4.941942           5110.898899
std     288.530761            14.235415                  312.365695     0.500244    2.701511              2.784626           8592.036516
min    1001.000000             0.000000                    0.000000     0.000000    0.000000              1.000000            201.000000
25%    1250.500000            12.000000                   96.000000     0.000000    5.000000              3.000000           1495.500000
50%    1500.000000            24.000000                  394.000000     0.000000    7.000000              5.000000           2865.000000
75%    1749.500000            36.000000                  717.500000     1.000000    9.000000              7.000000           4198.000000
max    1999.000000            50.000000                  998.000000     1.000000   10.000000             15.000000          49715.000000
```

Other statistics of the dataset are also shown during program execution, as well as null values inside the data columns.
Key highlights are also shown below:


## Training and Testing

Run the model.py file after installing the given requirements.

Dataset information composing of null value counts, feature descriptions, and statistics are shown during program execution. After cleaning the dataset, techincal insights were displayed using graphs as well as key users were
highlighted and segmented  using K-Means approach.

```bash
Other Key Highlights

Highest screen time:    50.0
Lowest screen time:     0.0
Average screen time:    24.39039039039039
Highest amount spent:   998.0
Lowest amount spent:    0.0
Average amount spent:   424.4154154154154
```

## Graphical Results

![1](Graphs/Ratings%20vs%20Screen%20Time.png)
![2](Graphs/Spending%20Capacity%20vs%20Screen%20Time.png)
![3](Graphs/User%20Segmentation%20with%20K-means%20Clustering.png)
