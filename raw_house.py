# -*- coding: utf-8 -*-
"""raw_house.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YBhH_FSxLB_Uc37q6IzaPqrgjy0UTaB4
"""

import pandas as pd
import numpy as np
import seaborn as sns
import seaborn as sns
import matplotlib.pyplot as plt

house = pd.read_csv("/content/raw_house_data - raw_house_data.csv")

house.head(5)

print(house.shape)
print(house.columns)
print(house.isna().sum())

"""# Drop NA's"""

house = house.dropna()
print(house.isna().sum())
print(house.shape)

house['HOA'].unique()

house['HOA'] = house['HOA'].str.replace(',', '')
mean_HOA = house['HOA'].loc[house['HOA'] != 'None']
mean_HOA = mean_HOA.astype(float).mean().round(2)
house['HOA'] = house['HOA'].replace('None', mean_HOA)
#house['HOA'] = house.HOA.fillna(value=np.nan, inplace=True)
#house['HOA'] = house['HOA'].astype(str).astype(float)
#mean_HOA = house['HOA'].mean()
#house['HOA'] = house['HOA'].fillna(mean_HOA, inplace=True)

print(house['HOA'].shape)
print(house['HOA'].unique())
house['HOA']

print(house.shape)
house = house.replace(to_replace='None', value=np.nan)
print(house.isna().sum())
house = house.dropna()
print(house.shape)

#house['HOA'].fillna((house['HOA'].mean()), inplace=True)
#print(house.isna().sum())
#house = house.dropna()
#print(house.shape)

house.max()

house.min()

sns.boxplot(house['lot_acres'])

sns.boxplot(house['year_built'])

print(house.shape)
house = house.loc[house['year_built'] != 0]
print(house.shape)
house = house.loc[house['lot_acres'] != 0]
print(house.shape)

sns.boxplot(house['lot_acres'])

sns.boxplot(house['year_built'])

house.max()

house.min()

house.sort_values(by=['lot_acres']).head(10)

house.head(10)

house.dtypes

house['bathrooms'].unique()

house['bathrooms'] = house['bathrooms'].astype(float)
house['garage'] = house['garage'].astype(float)
house['HOA'] = house['HOA'].astype(float)
house['sold_price'] = house['sold_price'].astype(int)

print(house.shape)
house = house.loc[house['bathrooms'] <= 35]
house = house.loc[house['bedrooms'] <= 35]
print(house.shape)



"""# Exploratory Data Analysis"""

house.describe().T.round(2)

corr = house.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

#sns.pairplot(house)

plt.figure(figsize=(10,6))
plt.scatter(house['sold_price'], house['lot_acres'])
#add axis labels
plt.xlabel('Sold price')
plt.ylabel('Lot Acres')

fig, ax = plt.subplots(figsize=(10, 8))
sns.lineplot(data=house, x="sold_price", y="bathrooms", ax=ax)

fig, ax = plt.subplots(figsize=(10, 8))
sns.lineplot(data=house, x="sold_price", y="fireplaces", ax=ax)

sns.displot(house, x="bathrooms", binwidth=1)

sns.displot(house, x="bedrooms", binwidth=1)

sns.histplot(data=house, x="year_built")

house['year_built'].value_counts().sort_index()[-20:]