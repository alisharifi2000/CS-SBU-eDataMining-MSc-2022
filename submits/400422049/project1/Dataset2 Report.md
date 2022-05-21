# About Dataset

## Where is the data from?
The data was scraped from Immoscout24, the biggest real estate platform in Germany. Immoscout24 has listings for both rental properties and homes for sale, however, the data only contains offers for rental properties.
The scraping process is described in this blog post and the corresponding code for scraping and minimal processing afterwards can be found in this Github repo.
At a given time, all available offers were scraped from the site and saved. This process was repeated three times, so the data set contains offers from the dates 2018-09-22, 2019-05-10 and 2019-10-08.

## Content
The data set contains most of the important properties, such as living area size, the rent, both base rent as well as total rent (if applicable), the location (street and house number, if available, ZIP code and state), type of energy etc. It also has two variables containing longer free text descriptions: description with a text describing the offer and facilities describing all available facilities, newest renovation etc. The date column was added to give the time of scraping.

# Getting Started
In this section first we are going to import modules and then set up the connections to the kaggle in order to have access to the datasets and importing them to the google colab environment. 

## Importing Modules

## Installing the _kaggle_ Module
In order to have access to kaggle API for fetching the datasets, we need to install the kaggle module inside the environment using bash commmad python package installer **pip**.

## Importing the **Apartment rental offers in Germany** Dataset

# 1. Reading the Dataset and Some Preliminary Checks
The data was scraped from Immoscout24, the biggest real estate platform in Germany. Immoscout24 has listings for both rental properties and homes for sale, however, the data only contains offers for rental properties.

In this section, after reading the dataset, we are going to do some preliminary checks and take a look at the outlines of the dataset; such as the columns, size of dataset, data-types to see what can we do to optimize the dataset for what's coming next.
```
imm.shape
```

```
(268850, 49)
```

```
imm.columns
```

```
Index(['regio1', 'serviceCharge', 'heatingType', 'telekomTvOffer',
       'telekomHybridUploadSpeed', 'newlyConst', 'balcony', 'picturecount',
       'pricetrend', 'telekomUploadSpeed', 'totalRent', 'yearConstructed',
       'scoutId', 'noParkSpaces', 'firingTypes', 'hasKitchen', 'geo_bln',
       'cellar', 'yearConstructedRange', 'baseRent', 'houseNumber',
       'livingSpace', 'geo_krs', 'condition', 'interiorQual', 'petsAllowed',
       'street', 'streetPlain', 'lift', 'baseRentRange', 'typeOfFlat',
       'geo_plz', 'noRooms', 'thermalChar', 'floor', 'numberOfFloors',
       'noRoomsRange', 'garden', 'livingSpaceRange', 'regio2', 'regio3',
       'description', 'facilities', 'heatingCosts', 'energyEfficiencyClass',
       'lastRefurbish', 'electricityBasePrice', 'electricityKwhPrice', 'date'],
      dtype='object')
```
## Optimizing the Data-types : Any Candidates?
As you might notice, mostly the datatypes are not set to `category`, whereas there are columns which could be revised in terms of datatype for better peformance and better readability. Following you may find the selected columns and the procedure of optimizing them in terms of datatypes. (Also the memory usage will do better after the changes) 

By checking the unique values in each column, we are going to filter the ones with less than 20 unique values. Thses columns are good candidates for going under an astype operation and transforming into `category` type.

```
for cols in imm.nunique()[imm.nunique() < 20].index :
  imm[cols] = imm[cols].astype('category')
```
## Handling Null Values
Null values is an evitable aspect of any real dataset. So it would be better if we accept the existance of null values and do some work to handle them in the best way so that we can cover these caveats and also enrich our dataset with some proper data instead.

Following you may find the same procedure in our dataset. First we need to have an aggregate report on how these null values are spreaded throughout the rows and columns. Then we need to choose the best approach based on the datatype to fill these values. 

```
# how null data is spreaded throughout the dataframe

nul_col_mask = imm.isnull().sum()/len(imm) > 0.5

nul_col = imm.columns[nul_col_mask]

imm.drop(columns=nul_col , inplace = True)
```
```
imm.dropna(axis=0, thresh=len(imm.columns)*0.8 , inplace = True)
```
## Handling Outliers

Outliers are records which have some anomalies in their values in comparison with some criteria, mostly from a statistical point of view.

There are different methods on how to handle outliers and it's better to apply each method according to the nature of dataset.

```
for cols in imm.columns:

  if imm[cols].dtype == 'int64' or imm[cols].dtype == 'float64':
      upper_range = imm[cols].mean() + 3 * imm[cols].std()
      lower_range = imm[cols].mean() - 3 * imm[cols].std()
      
      indexs = imm[(imm[cols] > upper_range) | (imm[cols] < lower_range)].index
      imm = imm.drop(indexs)
```

## Handling Duplicates

Using the `scoutId` column, one is able to check if there are duplicated records in the dataset:

we have found none based on `scoutId`

```
duplicated_rows = imm.duplicated(subset = 'scoutId',keep= 'first')
duplicated_rows.sum()
```
```
0
```
# 2. Aggregate information 
Aggregate data refers to numerical or non-numerical information that is collected from multiple sources and/or on multiple measures, variables, or individuals and compiled into data summaries or summary reports, typically for the purposes of public reporting or statistical analysis.

## Total number of Ads

```
len(imm)
```

```
226151
```
