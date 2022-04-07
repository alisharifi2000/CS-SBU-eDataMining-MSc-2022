# About Dataset



## Context

Since 2008, guests and hosts have used Airbnb to expand on traveling possibilities and present more unique, personalized way of experiencing the world. This dataset describes the listing activity and metrics in NYC, NY for 2019.

## Content

This data file includes all needed information to find out more about hosts, geographical availability, necessary metrics to make predictions and draw conclusions.

# Getting Started
In this section first we are going to import modules and then set up the connections to the kaggle in order to have access to the datasets and importing them to the google colab environment. 

## Installing the _kaggle_ Module
In order to have access to kaggle API for fetching the datasets, we need to install the kaggle module inside the environment using bash commmad python package installer **pip**.

## Importing the **NYC Airbnb** Dataset
Using bash command `kaggle` we are willing to download the dataset.

# 1. Reading the Dataset and Some Preliminary Checks
In this section, after reading the dataset, we are going to do some preliminary checks and take a look at the outlines of the dataset; such as the columns, size of dataset, data-types to see what can we do to optimize the dataset for what's coming next.

## Optimizing the Data-types : Any Candidates?
As you might notice, mostly the datatypes are set to `object`, whereas there are columns which could be revised in terms of datatype for better peformance and better readability. Following you may find the selected columns and the procedure of optimizing them in terms of datatypes. (Also the memory usage will do better after the changes) 
```
NYC['neighbourhood_group'] = NYC['neighbourhood_group'].astype('category')
NYC['neighbourhood'] = NYC['neighbourhood'].astype('category')
NYC['room_type'] = NYC['room_type'].astype('category')
NYC['last_review'] = pd.to_datetime(NYC['last_review'])
```
## Handling Null Values
Null values is an evitable aspect of any real dataset. So it would be better if we accept the existance of null values and do some work to handle them in the best way so that we can cover these caveats and also enrich our dataset with some proper data instead.

Following you may find the same procedure in our dataset. First we need to have an aggregate report on how these null values are spreaded throughout the rows and columns. Then we need to choose the best approach based on the datatype to fill these values. 

First of all we can get rid of records with null values ( which are sparse ) in `name` and `host_name` safely.
```
id                                    0
name                                  0
host_id                               0
host_name                             0
neighbourhood_group                   0
neighbourhood                         0
latitude                              0
longitude                             0
room_type                             0
price                                 0
minimum_nights                        0
number_of_reviews                     0
last_review                       10037
reviews_per_month                 10037
calculated_host_listings_count        0
availability_365                      0
dtype: int64
```
based on the concise report above, the data is an easy one! from the null-values point of view. Only in 2 columns:
```
last_review                       10037
reviews_per_month                 10037

```
we are facing some sort of null values crisis. Checking these columns, it's clear that the `last_review` nulls are somehow significant if there are 0 reviews for the record. accordingly null values in the `reviews_per_month` columns are also due to zero reviews for the record. So we can safely replace null values in `review_per_month` by zeros.

## Adding **Gender** feature to the Dataset
Using some pre-built name-gender datasets on the web, based on `host_name` field, one might want to add **gender** information as a new feature column to the dataset. It might come in handy if we are willing to infere some relations based on the `gender` of the hosts.  

### Gender Dataset : Case 1

As you might notice we have added a new feature column as `temp_gender` to our dataset and changed its data-type to `category`.

But it's better to check if the name-gender correspondance is fairly complete or not by checking the number of null values in this new feature column :
```
male      0.362315
NaN       0.327930
female    0.309755
Name: temp_gender, dtype: float64
```
As it seems, unfortunately because our name-gender database was not a good resource, as a result we have quite many null values in the gender columns (~ 32.7% null results):
```
male      0.362315
NaN       0.327930
female    0.309755

```

 So we are going to check another resource with many more name-gender records in it, in the hope of better results:  

### Gender Dataset : Case 2
So in this section we are using another name-gender dataset with more than **95,000** records:



AS you might notice, using this new name-gender dataset , we were able to outperform the previous one ,in terms of non-null data.
```
female         0.438086
male           0.388677
unspecified    0.173237

```
Now there's only 17.3% unspecified gender in comparison with our last attempt which was 32.7% null gender data. So we are going to drop the `temp_gender` columns in favor of the newly-added `gender` feature column.

## Host-type : Are they individuals, couples or institutes?
Actually it came into my mind to check if I can retrieve more information about host-types using some keyword pattern search inside `host_name` string to answer this question: Are they individuals, couples or institutes?

So I created 3 different masks based on keywords that I thought may indicate different categories for us: _individuals, couples and institues_ and then add a new column for `host_type` and filling it up using these masks according to the `host_name` feature column.

## Some Final Thoughts about Clearing the Dataset

Beside optimizing datatypes and handling null values, there are other aspects that we need to take care of, if we want to do data science:

### Irrelevant Unhelpful Columns : Get Rid of Them!

There are always some internal codes or indices that will lose their significance as an independent data. _IDs_ or _row numbers_ are among those. We can drop them safely:
```
NYC.drop('id', axis=1, inplace=True)
```
### Ethical Considerations

Besides any technicalities that must be addressed in the data science context, ethical considerations also are of great importance. If there's any personal information which needs someone's consent for analysis, it's better to put them aside very early in the process:
`host_name` here might be one of those!
```
NYC.drop('host_name', axis=1, inplace=True)
```
## Handling Outliers

Outliers are records which have some anomalies in their values in comparison with some criteria, mostly from a statistical point of view.

There are different methods on how to handle outliers and it's better to apply each method according to the nature of dataset. Here, we applied Z-score criteria:
```
for cols in NYC.columns:
  if cols != 'host_id' :
    if NYC[cols].dtype == 'int64' or NYC[cols].dtype == 'float64':
        upper_range = NYC[cols].mean() + 3 * NYC[cols].std()
        lower_range = NYC[cols].mean() - 3 * NYC[cols].std()
        
        indexs = NYC[(NYC[cols] > upper_range) | (NYC[cols] < lower_range)].index
        NYC = NYC.drop(indexs)
```
### Recalculation of "calculated_host_listings_count"
Caution! The values in this column should be recalculated again because of its dependencies on other records that might have been omitted.

# 2. Aggregate information 
Aggregate data refers to numerical or non-numerical information that is collected from multiple sources and/or on multiple measures, variables, or individuals and compiled into data summaries or summary reports, typically for the purposes of public reporting or statistical analysis.

## Total number of Ads
```
len(NYC)
```
```
44090
```

## Number of Ads by neighbourhood_group Categories
```
NYC['neighbourhood_group'].value_counts()
```
```
Manhattan        19635
Brooklyn         19055
Queens            4278
Bronx              954
Staten Island      168
Name: neighbourhood_group, dtype: int64
```
![](https://github.com/rz-pb/CS-SBU-eDataMining-MSc-2022/blob/400422049/submits/400422049/project1/assets/neighbourhood_group.png)
## Price Statistical Measures
```
NYC['price'].describe()
```
```
count    44090.000000
mean       138.792334
std        107.936585
min          0.000000
25%         69.000000
50%        105.000000
75%        175.000000
max        860.000000
Name: price, dtype: float64
```

```
NYC['price'].mode()[0]
```

```
150
```
```
NYC['price'].median()
```
```
105.0
```
![](https://github.com/rz-pb/CS-SBU-eDataMining-MSc-2022/blob/400422049/submits/400422049/project1/assets/price_histplot.png)
## Number of Ads for Each Unique Host

Number of unique `host_id`s in dataset:
```
NYC['host_id'].nunique()
```
```
34807
```

```
NYC['host_id'].value_counts()
```

```
137358866    103
16098958      96
12243051      96
61391963      91
22541573      87
            ... 
5346314        1
6707228        1
69944410       1
33816358       1
68119814       1
Name: host_id, Length: 34807, dtype: int64
```

```
NYC['host_id'].value_counts().describe()
```

```
count    34807.000000
mean         1.266699
std          1.740087
min          1.000000
25%          1.000000
50%          1.000000
75%          1.000000
max        103.000000
Name: host_id, dtype: float64
```
```
NYC['host_id'].value_counts().median()
```

```
1.0
```

```
NYC['host_id'].value_counts().mode()[0]
```

```
1
```
As you might already noticed, number of ads for each unique host has an **extremely skewed distribution** towards 1 ad per host as the _mean_, _median_ and _mode_ are indicating clearly. A distribution is said to be skewed when the data points cluster more toward one side of the scale than the other. 

Therefore any distribution plot would be extremely disproportionate and gives little insight visually.

despite I tried to plot with a log scale y-axis to keep it more descriptive.

![](https://github.com/rz-pb/CS-SBU-eDataMining-MSc-2022/blob/400422049/submits/400422049/project1/assets/Number_of_Listings_for_Each_Host_Frequency_histplot.png)

## Number of Properties for Each Unique Host
If we are going to find the number of properties (not listings!) for each unique host, it requires to know what differentiates properties with eachother. I couldn't come to a conclusion that spatial coordinates can give us this criteria.
```
NYC[['host_id', 'latitude', 'longitude', 'room_type']].loc[NYC['latitude']==40.70738].head(90)
```
![](https://github.com/rz-pb/CS-SBU-eDataMining-MSc-2022/blob/400422049/submits/400422049/project1/assets/Screenshot%202022-04-07%20221557.png)

## Most Reviewed Listings
```
NYC['number_of_reviews'].nlargest(10)
```

```
129     155
152     155
1066    155
1949    155
2418    155
2572    155
4280    155
7040    155
7578    155
9156    155
Name: number_of_reviews, dtype: int64
```

```
sns.displot(data = NYC , x = 'number_of_reviews')
```

![](https://github.com/rz-pb/CS-SBU-eDataMining-MSc-2022/blob/400422049/submits/400422049/project1/assets/number_of_reviews_displot.png)
## Hosts with the Most Total Reviewed Listings
```
top_reviewed_hosts = pd.DataFrame(NYC.groupby('host_id')['number_of_reviews'].sum().nlargest(10))
top_reviewed_hosts.reset_index(inplace = True)
top_reviewed_hosts['host_id']  = top_reviewed_hosts['host_id'].astype('category')
```
![](https://github.com/rz-pb/CS-SBU-eDataMining-MSc-2022/blob/400422049/submits/400422049/project1/assets/Screenshot%202022-04-07%20222130.png)
```
top_reviewed_hosts.plot.bar(x='host_id',y='number_of_reviews', rot=0)
```
![](https://github.com/rz-pb/CS-SBU-eDataMining-MSc-2022/blob/400422049/submits/400422049/project1/assets/top_reviewed_hosts_plot.png)
