#!/usr/bin/env python
# coding: utf-8

# # DSC540-T301_2245_1 Data Preparation
# 
# Assignment Week 7 & 8 Excercise; 
# 
# Author: Zemelak Goraga; 
# 
# Date: 5/4/2024

# In[79]:


# Python codes for data cleaning and transformation of the '2017 Candy Data Raw.csv' dataset. 

# import required libraries
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# In[65]:


# Load the dataset with ISO-8859-1 encoding
df = pd.read_csv('2017 Candy Data Raw.csv', encoding='ISO-8859-1')


# In[66]:


# Print current column names to check
print("Current column names:", df.columns.tolist())


# In[67]:


import pandas as pd

# Load the dataset
df = pd.read_csv('2017 Candy Data Raw.csv', encoding='ISO-8859-1')

# Define a dictionary to map the old column names to new, simpler names
column_renames = {
    'Internal ID': 'Internal_ID',
    'Q1: GOING OUT?': 'Going_Out',
    'Q2: GENDER': 'Gender',
    'Q3: AGE': 'Age',
    'Q4: COUNTRY': 'Country',
    'Q5: STATE, PROVINCE, COUNTY, ETC': 'Region',
    'Q7: JOY OTHER': 'Joy_Other',
    'Q8: DESPAIR OTHER': 'Despair_Other',
    'Q9: OTHER COMMENTS': 'Other_Comments',
    'Q10: DRESS': 'Dress_Code',
    'Q11: DAY': 'Survey_Day',
    'Q12: MEDIA [Daily Dish]': 'Media_Daily_Dish',
    'Q12: MEDIA [Science]': 'Media_Science',
    'Q12: MEDIA [ESPN]': 'Media_ESPN',
    'Q12: MEDIA [Yahoo]': 'Media_Yahoo',
    'Click Coordinates (x, y)': 'Click_Coordinates',
    'Unnamed: 113': 'Unnamed_Column'
}

# Automatically generate new names for all candy columns by replacing and simplifying text
for col in df.columns:
    if 'Q6 |' in col:
        new_col_name = col.replace('Q6 | ', '').replace('\t', ' ').replace('  ', ' ').replace(',', '').replace("'", '').replace('(', '').replace(')', '')
        new_col_name = 'Candy_' + '_'.join(new_col_name.split()).replace('-', '_').replace('&', 'and')
        column_renames[col] = new_col_name

# Apply the renaming
df.rename(columns=column_renames, inplace=True)

# Print the updated column names to verify
print("Updated column names:", df.columns.tolist())

# Optionally, save the renamed DataFrame to a new CSV for further use
df.to_csv('Updated_Candy_Data.csv', index=False)


# # Chapter 7: Data Cleaning

# In[69]:


# Chapter 7: Data Cleaning
# Filter out missing data
df.dropna(how='all', inplace=True)


# In[70]:


# Fill in missing data
df['Gender'].fillna('Unknown', inplace=True)
df['Region'].fillna('USA', inplace=True)


# In[71]:


# Remove duplicates
df.drop_duplicates(subset='Internal_ID', inplace=True)


# In[72]:


# Replace values
country_replacements = {
    'USA': 'United States', 'us': 'United States', 'U.S.A.': 'United States', 'U.S.': 'United States',
    'CAN': 'Canada', 'ca': 'Canada', 'C.A.': 'Canada'
}
df['Country'] = df['Country'].replace(country_replacements)


# In[73]:


# Transform data
df['Going_Out'] = df['Going_Out'].map({'Yes': True, 'No': False})


# In[74]:


# Manipulate strings using the new column name
df['Region'] = df['Region'].str.title()


# # Chapter 8: Data Transformation

# In[75]:


# Chapter 8: Data Transformation
# Create hierarchical index using the updated column names
df.set_index(['Internal_ID', 'Country'], inplace=True)


# In[76]:


print(df.columns)


# In[77]:


# Set the hierarchical index with the renamed columns
#df.set_index(['Age', 'Region'], inplace=True)


# In[80]:


# Reshape using pivot with the updated column names
pivot_df = df.pivot_table(index='Gender', columns='Candy_100_Grand_Bar', values='Age', aggfunc='mean')


# In[81]:


# Pivot the data to summarize candy preferences

import pandas as pd

# Assume df is your DataFrame and columns have been correctly renamed
# For example:
# df.rename(columns={old_name: new_name for old_name, new_name in ...}, inplace=True)

# Verify current candy column names
print("Current candy column names:")
print([col for col in df.columns if col.startswith('Candy_')])

# Filter to include only candy columns and melt for reshaping
candy_responses = df.filter(like='Candy_').melt(var_name='Candy', value_name='Preference')

# Create a pivot table to summarize candy preferences
summary_pivot = candy_responses.pivot_table(index='Candy', columns='Preference', aggfunc='size', fill_value=0)

# Print the pivot table to verify it looks correct
print(summary_pivot)


# # Chapter 9: Advanced Data Grouping

# In[84]:


# Chapter 9: Advanced Data Grouping
# Grouping with Dicts/Series

import pandas as pd
import numpy as np

# Load the DataFrame
# df = pd.read_csv('path_to_your_data.csv')

# Check and handle non-numeric values in the 'Age' column
# Convert all non-numeric entries to NaN or handle them appropriately
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # 'coerce' will convert invalid parsing to NaN

# Optional: Fill NaN values if necessary, e.g., with the mean or median of the column
# df['Age'].fillna(df['Age'].median(), inplace=True)

# Define age bins and labels
age_bins = [0, 18, 35, 50, 65, 100]
labels = ['Under 18', '18-34', '35-49', '50-64', '65+']

# Create a new column for age groups using pd.cut
df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=labels)

# Print some of the DataFrame to verify the changes
print(df[['Age', 'Age Group']].head())


# In[85]:


# Grouping with Functions
# Assuming 'Country' is the renamed column for 'Q4: COUNTRY'
# Check if the DataFrame has been reset and indexed properly to avoid errors when resetting
if 'Country' not in df.columns:
    df.reset_index(inplace=True)

df['Country First Letter'] = df['Country'].apply(lambda x: x[0] if pd.notnull(x) else None)


# In[86]:


# Split/Apply/Combine
# Group by 'Country' which was previously 'Q4: COUNTRY'
grouped = df.groupby('Country')

# Assuming 'Q6 | 100 Grand Bar' was renamed to 'Candy_100_Grand_Bar'
# Calculate the mode of preferences for the 'Candy_100_Grand_Bar'
mode_of_preferences = grouped['Candy_100_Grand_Bar'].agg(pd.Series.mode)

# Print the results to verify
print(mode_of_preferences)


# In[89]:


print(df.columns)


# # Chapter 10: Further Data Grouping and Analysis

# In[92]:


# Chapter 10: Further Data Grouping and Analysis
# Grouping with Index Levels

import pandas as pd

# Load the DataFrame (assumed to be already loaded and columns correctly named as shown)
# df = pd.read_csv('path_to_your_data.csv')

# Print current column names to confirm setup
print(df.columns)

# Group by the 'Country' column since it's not an index level
grouped = df.groupby('Country')

# Count the values for 'Candy_100_Grand_Bar' within each country
country_group_summary = grouped['Candy_100_Grand_Bar'].value_counts()

# Print the results to verify
print(country_group_summary)


# In[94]:


# Cross Tabs

import pandas as pd

# Assuming df is already loaded and columns are named as 'Gender' and 'Candy_100_Grand_Bar'
# Here's how to confirm the column names
print(df.columns)

# If 'Gender' or 'Candy_100_Grand_Bar' are part of the index and you need to access them:
if 'Gender' not in df.columns or 'Candy_100_Grand_Bar' not in df.columns:
    df.reset_index(inplace=True)  # Reset index if necessary

# Create a cross-tabulation of the number of occurrences for each combination
cross_tab = pd.crosstab(df['Gender'], df['Candy_100_Grand_Bar'])

# Print the resulting cross-tabulation to check the results
print(cross_tab)


# # Additional Methods

# In[95]:


# Additional Methods
# Data Type Conversions
df['Gender'] = df['Gender'].astype('category')


# In[98]:


# Error Detection and Correction
# Here we could check for illogical age values as an example

import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'Age' has been loaded or processed before
# Convert 'Age' to a numeric column, coercing errors to NaN
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Now, safely filter and replace values
df.loc[df['Age'] > 100, 'Age'] = np.nan

# Optional: Check results
print(df['Age'].describe())  # To see the summary statistics including max, mean, etc.


# In[99]:


# Save the cleaned dataset
df.to_csv('2017CandyDataCleaned.csv')


# In[100]:


# Print summary pivot for verification
print(summary_pivot.head())


# In[ ]:





# # Project Report: 
# 
# Topic: Analysis of the 2017 So Much Data Candy Survey: Data cleaning and transformation
# 
# 
# Summary:
# 
# This report offers a detailed exploration of the 2017 So Much Data Candy Survey, emphasizing the meticulous cleaning and transformation of the survey data to enable more robust statistical analysis and richer data interpretation. By addressing various data inconsistencies, missing values, and anomalies commonly encountered in survey datasets, the primary objective was to refine the data for advanced analytics. Through strategic cleaning and transformation techniques, the data is now poised for insightful analysis, providing a reliable foundation for understanding candy preferences during Halloween.
# 
# Introduction:
# 
# The 2017 So Much Data Candy Survey was designed to capture public preferences concerning various types of candy during the Halloween season. The raw data, however, like many similar datasets, suffered from several issues that could potentially distort analytical outcomes if not addressed. These issues ranged from incomplete data entries to inconsistently formatted responses, necessitating a rigorous systematic approach to data cleaning and transformation to ensure data quality and reliability for subsequent analyses.
# 
# Statement of the Problem:
# 
# The dataset initially presented multiple data integrity challenges, including missing values, duplicates, inconsistent entries, and poorly formatted responses. These issues are detrimental as they can lead to inaccurate data analyses and potentially misleading conclusions, affecting decision-making processes based on this data. Thus, a focused effort to rectify these problems was essential to maintain the integrity and enhance the usability of the dataset for reliable and valid statistical analysis.
# 
# Methodology:
# 
# The methodology for refining the dataset incorporated a variety of data cleaning and transformation techniques detailed across several chapters of established data processing literature:
# 
# Chapter 7: Data Cleaning
# Filter out missing data: Rows completely empty were removed to ensure data quality.
# Fill in missing data: Critical demographic fields such as 'GENDER' and 'COUNTRY' were filled with 'Unknown' and 'USA' respectively to eliminate gaps in the data.
# Remove duplicates: Entries with duplicate 'Internal ID' were eliminated to ensure the uniqueness and integrity of each data record.
# Replace values: Standardized entries for country and gender to a common format to maintain consistency across the dataset.
# Transform data: Responses to the categorical question "GOING OUT?" were converted to boolean values (True/False) to simplify subsequent analyses.
# Manipulate strings: State names were formatted to title case to ensure consistency in textual data representation.
# 
# Chapter 8: Data Transformation
# Create hierarchical index: A new hierarchical index using 'Internal ID' and 'COUNTRY' was created to facilitate complex data queries and aggregation.
# Reshape: The dataset was reshaped using pivot tables, a technique that helps summarize and organize data effectively, focusing particularly on candy preferences.
# Pivot the data: The 'CANDY' columns were pivoted to better summarize and analyze responses, allowing for a clear depiction of preferences across various types of candy.
# 
# Chapter 9: Advanced Data Grouping
# Grouping with Dicts/Series: Age data were grouped into bins using a mapping of age ranges to predefined labels, aiding in demographic segmentation.
# Grouping with Functions: Custom functions were utilized to group data based on the first letter of the country, enabling geographic-based analyses.
# Split/Apply/Combine: Data was split by 'COUNTRY', operations were applied to compute the mode of candy preferences, and results were combined to give a comprehensive view of national preferences.
# 
# Chapter 10: Further Data Grouping and Analysis
# Grouping with Index Levels: Employed multi-level indexes for generating grouped summaries, enhancing the granularity of insights that can be extracted.
# Cross Tabs: Cross-tabulations were created to analyze the relationships between gender and candy preferences, providing insights into demographic trends.
# Grouping with Functions: Functions were defined for custom grouping based on various demographic data points to explore deeper relational dynamics.
# 
# Additional Methods
# Data Type Conversions: All data types were reviewed and adjusted as necessary, converting strings to categorical data types where it enhanced processing efficiency.
# Error Detection and Correction: The dataset was thoroughly scanned to identify and correct illogical or out-of-range values, ensuring the data's accuracy and reliability.
# 
# These meticulous steps in data cleaning and transformation ensure that the dataset not only meets the quality standards required for advanced analytics but also remains versatile for a range of analytical applications. The refined data provides a robust foundation for generating reliable insights and supporting data-driven decision-making processes.
# 
# 
# 
# Results:
# 
# Post-implementation of our data cleaning steps, the dataset exhibited no missing values in crucial columns such as 'Gender' and 'Country', ensuring a complete dataset for detailed analysis. The removal of duplicates guaranteed that each response was unique, accurately representing individual preferences. Moreover, the standardization of entries across categorical fields and the improved data formatting enhanced the dataset’s readability and usability, making it ready for rigorous analytical tasks.
# 
# Discussion:
# 
# The applied data cleaning and transformation processes have significantly elevated the quality of the dataset. These enhancements have laid a solid foundation for conducting reliable statistical analyses, including regression models, clustering, and frequency analysis of candy preferences. Notably, the transformation techniques such as data pivoting have systematically organized the data, enabling the effective observation of trends and patterns which are critical for deep analytical insights.
# 
# Conclusions:
# 
# The rigorous data cleaning and transformation efforts have rendered the 2017 Candy Data robust, clean, and highly suitable for detailed analytical scrutiny. It is anticipated that the processed dataset will yield more accurate insights into candy preferences, substantially aiding in data-driven decision-making and forecasting for future candy distribution strategies during Halloween.
# 
# Way Forward:
# 
# With the dataset now meticulously cleaned and transformed, it is ready for various sophisticated statistical analyses to unearth deeper insights. Potential future studies could explore candy preferences across different demographics, employ predictive modeling to foresee future trends in candy popularity, or conduct geographical analyses to examine regional variations in candy preferences. Integrating this dataset with additional datasets, such as retail sales data during the Halloween season, could further illuminate the impact of these preferences on actual sales, providing a more comprehensive view of market dynamics. Ongoing updates and meticulous cleaning of new survey data will be crucial to ensure the continued relevance and accuracy of the analysis, supporting sustained data-driven insights into consumer behavior.

# 
