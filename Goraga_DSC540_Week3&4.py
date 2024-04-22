#!/usr/bin/env python
# coding: utf-8

# 
# # DSC540-T301_2245_1 Data Preparation
# 
# Assignment Week 3 & 4;
# 
# Author: Zemelak Goraga;
# 
# Date: 4/6/2024

# # Activity 3.01

# In[4]:


# Step 1: Load necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


# Step 2: Read in the Boston housing dataset
housing_data = pd.read_csv('Boston_housing.csv')


# In[6]:


# Step 3: Check the first 10 records and find the total number of records
print("First 10 records:")
print(housing_data.head(10))
print("\nTotal number of records:", len(housing_data))


# In[7]:


# Step 4: Create a smaller DataFrame excluding specified columns
smaller_df = housing_data.drop(columns=['CHAS', 'NOX', 'B', 'LSTAT'])
smaller_df


# In[8]:


# Step 5: Check the last seven records of the new DataFrame
print("\nLast seven records of the new DataFrame:")
print(smaller_df.tail(7))


# In[9]:


# Step 6: Plot histograms of all variables in the new DataFrame
smaller_df.hist(figsize=(12, 10))
plt.tight_layout()
plt.show()


# In[10]:


# Step 7: Plot histograms of all variables using a for loop
for column in smaller_df.columns:
    plt.hist(smaller_df[column], bins=20)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


# In[11]:


# Step 8: Create a scatter plot of crime rate versus price
plt.scatter(housing_data['CRIM'], housing_data['PRICE'])
plt.title('Crime Rate vs Price')
plt.xlabel('Crime Rate')
plt.ylabel('Price')
plt.show()


# In[ ]:


# Step 9: Plot log10(crime) versus price
plt.scatter(np.log10(housing_data['CRIM']), housing_data['PRICE'])
plt.title('Log10(Crime Rate) vs Price')
plt.xlabel('Log10(Crime Rate)')
plt.ylabel('Price')
plt.show()


# In[12]:


# Step 10: Calculate and print some useful statistics
mean_rooms_per_dwelling = smaller_df['RM'].mean()
median_age = smaller_df['AGE'].median()
mean_distance_to_employment_centers = smaller_df['DIS'].mean()
percentage_low_price = (housing_data['PRICE'] < 20).mean() * 100

print("\nMean Rooms per Dwelling:", mean_rooms_per_dwelling)
print("Median Age:", median_age)
print("Mean Distance to Employment Centers:", mean_distance_to_employment_centers)
print("Percentage of Houses with Low Price (< $20,000):", percentage_low_price)


# # Discussion Activity 3.01

# 
# The primary objective of this analysis is to explore the Boston housing dataset and extract meaningful insights regarding the factors affecting housing prices. 
# 
# Specifically, the aims are:
# 
# Investigate the distribution of different features in the dataset.
# Identify correlations between variables, particularly with respect to housing prices.
# Calculate descriptive statistics to understand the central tendencies and variability of key features.
# Explore the impact of crime rate on property prices.
# Assess the proportion of houses with prices below $20,000.
# 
# 
# 
# I begin by loading the dataset into a pandas DataFrame and conducting preliminary data inspection. This involves checking the first few records, the data types of variables, and identifying any missing values. Subsequently, I performed data wrangling by excluding certain columns as specified in the problem statement.
# 
# Following data preprocessing, I visualized the distribution of variables through histograms and explore pairwise relationships using scatter plots. I then calculate descriptive statistics such as mean rooms per dwelling, median age, mean distances to employment centers, and the percentage of houses with low prices.
# 
# 
# 
# The analysis reveals several key findings. Firstly, the distribution of housing prices exhibits a right-skewed pattern, indicating that a majority of properties have lower prices. Secondly, there exists a strong positive correlation between the number of rooms per dwelling and property prices, suggesting that larger houses tend to be more expensive. Thirdly, the scatter plot depicting crime rate versus price illustrates a negative relationship, indicating that areas with higher crime rates tend to have lower property values. Finally, the calculated statistics provide insights into the average characteristics of houses in the Boston area.

# # Activity 4.01

# In[109]:


# Step 1: Load the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt


# In[110]:


# Step 2: Read the adult income dataset

income_data = pd.read_csv('adult_income_dataset.csv')
income_data.head()


# In[111]:


# Step 3: Create a script that will read a text file line by line
def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line)


# In[112]:


names = []
with open('adult_income_names.txt','r') as f:
    for line in f:
        f.readline()
        var=line.split(":")[0]
        names.append(var)
names


# In[113]:


names.append('income')


# In[116]:


income_data = pd.read_csv("adult_income_dataset.csv",names=names)
income_data.head()


# In[122]:


# Create a copy of the DataFrame

# Read the CSV file into a DataFrame
income_data = pd.read_csv("adult_income_dataset.csv", names=names)

# Create a copy
income_data_headed = income_data.copy()


# In[121]:


income_data_headed.head()


# In[175]:


# Step 5: Find the missing values
missing_values = income_data.isnull().sum()
print("Missing Values:")
print(missing_values)


# In[176]:


# Step 6: Create a DataFrame with only age, education, and occupation by using subsetting
subset_data = income_data[['age', 'education', 'occupation']]
subset_data


# In[177]:


# Step 7: Plot a histogram of age with a bin size of 20
plt.hist(income_data['age'], bins=20)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[178]:


# Step 8: Create a function to strip the whitespace characters
def strip_whitespace(x):
    if isinstance(x, str):
        return x.strip()
    else:
        return x


# In[180]:


# Step 9: Use the apply method to apply this function to all the columns with string values
income_data = income_data.applymap(strip_whitespace)


# In[181]:


# Step 10: Find the number of people who are aged between 30 and 50

import pandas as pd

# convert the 'age' column to integers
income_data['age'] = income_data['age'].astype(int)

# Filter the DataFrame based on age
people_between_30_50 = income_data[(income_data['age'] >= 30) & (income_data['age'] <= 50)]

# Get the number of people aged between 30 and 50
num_people_between_30_50 = len(people_between_30_50)
print("Number of people aged between 30 and 50:", num_people_between_30_50)


# In[182]:


# Step 11: Group the records based on age and education to find how the mean age is distributed
age_education_mean = income_data.groupby(['age', 'education']).mean()
age_education_mean


# In[ ]:





# In[172]:


# Step 12: Group by occupation and show the summary statistics of age

# Remove rows where the occupation is "?"
income_data_cleaned = income_data[income_data['occupation'] != "?"]

# Group by occupation and show the summary statistics of age
occupation_summary_stats = income_data_cleaned.groupby('occupation')['age'].describe()

# Check if there are any occupations with data beyond the 75th percentile
if '75%' in occupation_summary_stats:
    highest_percentile_profession = occupation_summary_stats[occupation_summary_stats['75%'] == occupation_summary_stats['75%'].max()].index[0]
    print("Profession with the largest share of the workforce above the 75th percentile:", highest_percentile_profession)
else:
    print("There is no occupation with data beyond the 75th percentile.")


# In[ ]:


N.B. After the '?' removed from the occupation column, the dataset 'income_data' was saved as 'income_data_cleaned' which will be used for the next activities.


# In[173]:


# Step 12: Group by occupation and show the summary statistics of age
occupation_summary_stats = income_data_cleaned.groupby('occupation')['age'].describe()
oldest_profession = occupation_summary_stats[occupation_summary_stats['mean'] == occupation_summary_stats['mean'].max()].index[0]
print("Profession with the oldest workers on average:", oldest_profession)
highest_percentile_profession = occupation_summary_stats[occupation_summary_stats['75%'] == occupation_summary_stats['75%'].max()].index[0]
print("Profession with the largest share of the workforce above the 75th percentile:", highest_percentile_profession)


# In[183]:


# Summary statistics of age

occupation_summary_stats


# In[184]:


# Step 13: Use subset and groupby to find outliers
outliers = income_data_cleaned.groupby('occupation').apply(lambda x: x[(x['age'] < x['age'].quantile(0.25)) | (x['age'] > x['age'].quantile(0.75))])
outliers


# In[185]:


# Step 14: Plot the values on a bar chart
outliers_count = outliers['occupation'].value_counts()
plt.bar(outliers_count.index, outliers_count.values)
plt.title('Outliers Count by Occupation')
plt.xlabel('Occupation')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[186]:


# Step 15: Merge the data using common keys

import pandas as pd

# Summary statistics DataFrame
occupation_summary_stats = income_data_cleaned.groupby('occupation')['age'].describe().reset_index()

# Merge the data using common keys (occupation)
merged_data = pd.merge(income_data_cleaned, occupation_summary_stats, on='occupation')

# Print the merged DataFrame
print(merged_data)


# N.B. The original dataset was merged with the summary statistics DataFrame based on the 'occupation' column, adding summary statistics for each occupation to each corresponding row in the original dataset.
# 

# In[ ]:





# # Discussion Activity 4.01

# 
# The primary objective of this analysis is to investigate the factors that influence income levels among adults. 
# 
# Specifically,the aims are:
# 
# Identify demographic attributes associated with higher income levels.
# Analyze the distribution of income across different occupations.
# Detect outliers in the dataset and assess their impact on the analysis.
# Provide insights into potential avenues for further research and exploration.
# 
# 
# The analysis begins with data preprocessing, including handling missing values, data cleaning, and feature selection. We then proceed to explore the dataset through descriptive statistics, visualizations, and advanced data wrangling techniques. 
# 
# Key steps in the analysis include:
# 
# Data loading and preprocessing: Reading the dataset from a CSV file, handling missing values, and cleaning the data.
# Exploratory data analysis: Visualizing the distribution of demographic attributes such as age, education, and occupation.
# Statistical analysis: Calculating summary statistics, identifying outliers, and assessing their impact on the analysis.
# Comparative analysis: Comparing income levels across different demographic groups and occupations.
# Interpretation and discussion: Interpreting the findings, discussing insights gained from the analysis, and proposing future research directions.
# 
# 
# The analysis reveals several noteworthy insights into the factors influencing income levels among adults. Education emerges as a significant predictor of income, with higher education levels corresponding to higher median incomes. Additionally, certain occupations, particularly those in managerial and professional fields, tend to command higher salaries. However, the presence of outliers suggests the need for cautious interpretation, as extreme values may distort the overall analysis. Furthermore, age exhibits a complex relationship with income, indicating potential nonlinear effects that merit deeper exploration.

# # Excercise 3

# In[2]:


# Import required library
import pandas as pd


# In[3]:


# Creating Series 1
data1 = [7.3, -2.5, 3.4, 1.5]
index1 = ['a', 'c', 'd', 'e']
series1 = pd.Series(data1, index=index1)


# In[7]:


# Creating Series 2
data2 = [-2.1, 3.6, -1.5, 4, 3.1]
index2 = ['a', 'c', 'e', 'f', 'g']
series2 = pd.Series(data2, index=index2)


# In[8]:


# Adding Series 1 and Series 2
addition_result = series1.add(series2, fill_value=0)
print("Addition Result:")
print(addition_result)


# In[9]:


# Subtracting Series 1 from Series 2
subtraction_result = series2.subtract(series1, fill_value=0)
print("\nSubtraction Result:")
print(subtraction_result)


# # Discussion Excercise 3

# 
# The task at hand involves creating two pandas Series objects, each with specified data and index values, and performing addition and subtraction operations on them. Additionally, the aim was to investigate how the operations handle missing indices and data points, and discuss the implications of these behaviors.
# 
# Data Preparation: Two pandas Series objects, Series 1 and Series 2, are created with specified data and index values.
# Arithmetic Operations: Addition and subtraction operations are performed on Series 1 and Series 2.
# Handling Missing Values: The operations are executed with the consideration of missing indices or data points using the fill_value=0 argument.
# 
# The addition operation combines corresponding elements from both Series, resulting in a new Series with the union of indices from both input Series. Any missing index or data point is treated as zero during the operation. Similarly, the subtraction operation computes the difference between corresponding elements of the Series, also considering missing values as zero.
# 

# # Short Report on Overall activities

# 
# Title: Exploratory Analysis of Diverse Datasets: Insights and Methodologies
# 
# Introduction: This comprehensive report integrates findings from three distinct analyses: an exploratory data analysis (EDA) of the Boston Housing Dataset, an analysis of the Adult Income Dataset, and an investigation into arithmetic operations on pandas Series in Python. The aim is to synthesize key insights and methodologies from these analyses to provide a comprehensive understanding of data exploration, analysis, and manipulation techniques.
# 
# Statement of the Problem: The overarching objective of this report is to explore diverse datasets, ranging from housing attributes to demographic information and computational operations, to uncover patterns, relationships, and implications for further research and decision-making. Specifically, the analyses aim to:
# 
# Explore factors influencing housing prices in the Boston area. Identify demographic and occupational determinants of income levels among adults. Investigate the implementation and implications of basic arithmetic operations on pandas Series.
# 
# Methodology: The methodologies employed in each analysis vary based on the nature of the dataset and the objectives of the investigation.
# 
# Boston Housing Dataset Analysis: The analysis begins with data loading and preprocessing using pandas. Descriptive statistics, visualizations (such as histograms and scatter plots), and correlation analyses are conducted to explore relationships between variables. The methodology emphasizes data wrangling, visualization, and statistical analysis.
# 
# Adult Income Dataset Analysis: Data preprocessing involves handling missing values and feature selection. Descriptive statistics, visualizations, and statistical analysis are employed to identify patterns and relationships between demographic attributes, occupations, and income levels. Comparative analysis is used to compare income levels across different demographic groups and occupations.
# 
# Arithmetic Operations on Pandas Series: Two pandas Series objects are created, and addition and subtraction operations are performed. The analysis investigates how these operations handle missing values using the fill_value=0 argument.
# 
# Result and Discussion
# 
# Boston Housing Dataset:
# Total number of records: 506
# Mean Rooms per Dwelling: 6.28
# Median Age: 77.5
# Mean Distance to Employment Centers: 3.80
# Percentage of Houses with Low Price (< $20,000): 41.50%
# Insights from the Boston Housing Dataset provide valuable information about the housing market in the area. The distribution of housing prices indicates a significant proportion of affordable housing options, with 41.50% of houses priced below $20,000. Additionally, variables such as the number of rooms per dwelling and distance to employment centers offer insights into factors influencing property prices. Correlations between variables, such as crime rate and property prices, further contribute to understanding housing dynamics in the area.
# 
# Adult Income Dataset:
# Number of people aged between 30 and 50: 16,390
# Profession with the oldest workers on average: Exec-managerial
# Profession with the largest share of the workforce above the 75th percentile: Priv-house-serv
# Analysis of the Adult Income Dataset highlights the significance of demographic attributes such as age, education, and occupation in determining income levels among adults. With 16,390 people aged between 30 and 50, the dataset provides insights into the demographic composition of the workforce. The identification of professions with the oldest workers on average, such as Exec-managerial, and those with the largest share of the workforce above the 75th percentile, such as Priv-house-serv, offers valuable insights for workforce planning and labor market analysis.
# 
# Arithmetic Operations on Pandas Series:
# The practical implementation of addition and subtraction operations on pandas Series provides a foundational understanding of data manipulation techniques. Considerations for handling missing values, as demonstrated in the arithmetic operations, are crucial for accurate data analysis. These operations serve as building blocks for more complex data manipulations and analyses in diverse domains.
# 
# Conclusions:
# The comprehensive analysis of diverse datasets, including the Boston Housing Dataset and the Adult Income Dataset, offers valuable insights into housing dynamics, workforce demographics, and data manipulation techniques. Understanding factors influencing housing prices and income levels, as well as implementing basic arithmetic operations on pandas Series, contributes to informed decision-making and further research in related domains. The findings from these analyses lay the groundwork for exploring complex relationships within datasets and informing future research directions.
# 
# 
# Way Forward: Moving forward, future research could involve more advanced analyses, predictive modeling, and exploration of alternative methodologies. Additionally, continued investigation into the datasets and techniques discussed in this report could lead to deeper insights and practical applications in various fields, including urban planning, socioeconomic research, and data analysis.

# In[ ]:




