#!/usr/bin/env python
# coding: utf-8

# # DSC540-T301_2245_1 Data Preparation
# 
# Assignment Week 5 & 6 Term Project Milstone 2;
# 
# Author: Zemelak Goraga;
# 
# Date: 4/21/2024

# In[222]:


# Import required libraries

import pandas as pd
import subprocess
import os
import zipfile
import json
import warnings
warnings.filterwarnings('ignore')


# In[223]:


# Execute the Kaggle API command to download the 'countries.json' dataset
command = "kaggle datasets download -d lucafrance/the-world-factbook-by-cia"
subprocess.run(command.split())

# Check if the download was successful
if os.path.exists("the-world-factbook-by-cia.zip"):
    print("Dataset downloaded successfully!")
    # Unzip the downloaded file
    with zipfile.ZipFile("the-world-factbook-by-cia.zip", "r") as zip_ref:
        zip_ref.extractall("data")

    # Load the JSON file
    with open("data/countries.json") as file:
        countries_data = json.load(file)

    # Display the data
    #print(countries_data)

    # Display the first few lines of the data
    #print(countries_data[:10])  # Print only the first 10 lines

else:
    print("Failed to download the dataset.")


# In[224]:


# Unzip the downloaded files. the zip file containes several independent files

import pandas as pd

# Check if the download was successful
if os.path.exists("the-world-factbook-by-cia.zip"):
    print("Dataset downloaded successfully!")
    # Unzip the downloaded file
    with zipfile.ZipFile("the-world-factbook-by-cia.zip", "r") as zip_ref:
        zip_ref.extractall("data")

    # Load the JSON file
    with open("data/countries.json") as file:
        countries_data = json.load(file)

    # Create DataFrame
    df = pd.DataFrame(countries_data)

    # Limit to 200 rows and 20 columns
    df = df.iloc[:200, :20]

    # Display DataFrame
    print(df)

else:
    print("Failed to download the dataset.")


# In[225]:


# Extract 'Economy: GDP - composition, by sector of origin - agriculture' for all countries
# Here I am interested to extract the Agricultural GDP (% of the total GDP) of different countries

import pandas as pd
import zipfile
import json
import os
from tabulate import tabulate

# Check if the download was successful
if os.path.exists("the-world-factbook-by-cia.zip"):
    print("Dataset downloaded successfully!")
    # Unzip the downloaded file
    with zipfile.ZipFile("the-world-factbook-by-cia.zip", "r") as zip_ref:
        zip_ref.extractall("data")

    # Load the JSON file
    with open("data/countries.json") as file:
        countries_data = json.load(file)

    # Initialize lists to store country names, agriculture GDP compositions, and years
    country_names = []
    agriculture_gdp_compositions = []
    years = []

    # Extract 'Economy: GDP - composition, by sector of origin - agriculture' for all countries
    print("Extracting 'Economy: GDP - composition, by sector of origin - agriculture' for all countries:")
    if isinstance(countries_data, list):
        for country_data in countries_data:
            country_names.append(country_data["name"])
            agriculture_gdp_composition = None
            year = None
            for key, value in country_data.items():
                if key.startswith("Economy: GDP - composition, by sector of origin - agriculture"):
                    if value:
                        split_value = value.split(' ')
                        agriculture_gdp_composition = split_value[0]  # Extract GDP composition
                        year = split_value[1] if len(split_value) > 1 else None  # Extract year if available
                    break  # Stop searching once found
            agriculture_gdp_compositions.append(agriculture_gdp_composition)
            years.append(year)
    elif isinstance(countries_data, dict):
        for country, info in countries_data.items():
            country_names.append(country)
            agriculture_gdp_composition = info.get("Economy: GDP - composition, by sector of origin - agriculture", None)
            if agriculture_gdp_composition:
                split_value = agriculture_gdp_composition.split(' ')
                agriculture_gdp_composition = split_value[0]  # Extract GDP composition
                year = split_value[1] if len(split_value) > 1 else None  # Extract year if available
            else:
                year = None
            agriculture_gdp_compositions.append(agriculture_gdp_composition)
            years.append(year)

    # Create DataFrame
    df = pd.DataFrame({
        "Country": country_names,
        "Agriculture GDP Composition": agriculture_gdp_compositions,
        "Year": years
    })

    # Display DataFrame as a table
    print(tabulate(df, headers='keys', tablefmt='github', showindex=False))

else:
    print("Failed to download the dataset.")


# In[226]:


# removing special characters

import pandas as pd
import zipfile
import json
import os
from tabulate import tabulate
import re

# Check if the download was successful
if os.path.exists("the-world-factbook-by-cia.zip"):
    print("Dataset downloaded successfully!")
    # Unzip the downloaded file
    with zipfile.ZipFile("the-world-factbook-by-cia.zip", "r") as zip_ref:
        zip_ref.extractall("data")

    # Load the JSON file
    with open("data/countries.json") as file:
        countries_data = json.load(file)

    # Initialize lists to store country names, agriculture GDP compositions, and years
    country_names = []
    agriculture_gdp_compositions = []
    years = []

    # Extract 'Economy: GDP - composition, by sector of origin - agriculture' for all countries
    print("Extracting 'Economy: GDP - composition, by sector of origin - agriculture' for all countries:")
    if isinstance(countries_data, list):
        for country_data in countries_data:
            country_names.append(country_data["name"])
            agriculture_gdp_composition = None
            year = None
            for key, value in country_data.items():
                if key.startswith("Economy: GDP - composition, by sector of origin - agriculture"):
                    if value:
                        split_value = re.findall(r'\d+\.\d+|\d+', value)  # Extract numerical values
                        agriculture_gdp_composition = split_value[0] if split_value else None
                        year = split_value[1] if len(split_value) > 1 else None  # Extract year if available
                    break  # Stop searching once found
            agriculture_gdp_compositions.append(agriculture_gdp_composition)
            years.append(year)
    elif isinstance(countries_data, dict):
        for country, info in countries_data.items():
            country_names.append(country)
            agriculture_gdp_composition = info.get("Economy: GDP - composition, by sector of origin - agriculture", None)
            if agriculture_gdp_composition:
                split_value = re.findall(r'\d+\.\d+|\d+', agriculture_gdp_composition)  # Extract numerical values
                agriculture_gdp_composition = split_value[0] if split_value else None
                year = split_value[1] if len(split_value) > 1 else None  # Extract year if available
            else:
                year = None
            agriculture_gdp_compositions.append(agriculture_gdp_composition)
            years.append(year)

    # Create DataFrame
    df = pd.DataFrame({
        "Country": country_names,
        "Agricultural GDP": agriculture_gdp_compositions,
        "Year": years
    })

    # Remove any special characters from the DataFrame
    df = df.replace({'Agricultural GDP': {r'[^0-9.]': ''}}, regex=True)
    df = df.replace({'Year': {r'[^0-9]': ''}}, regex=True)

    # Display DataFrame as a table without title
    print(tabulate(df, headers='keys', tablefmt='github', showindex=False, colalign=("left", "right", "right")), end='\n\n')

else:
    print("Failed to download the dataset.")


# In[ ]:





# In[227]:


# Print the last few rows of the dataset
df.tail()


# In[228]:


# Copying 'df' to 'df2' # keep 'df' as the original version and here on use df2
df2 = df.copy()

df2


# In[229]:


# Step 1: Replace Headers
new_headers = ["country", "gdp", "year"]
df2.columns = new_headers
df2


# In[230]:


import pandas as pd

# Assuming df2 is your DataFrame
print(df2.dtypes)


# In[231]:


# Step 2: Handling Missing Values
missing_values = df2.isnull().sum()
print("Missing values:\n", missing_values)


# In[232]:


# Step 3:Data Transformation: creating new variables using the 'gdp' variable

import pandas as pd  # Importing the pandas library and aliasing it as 'pd'
import numpy as np  # Importing the numpy library and aliasing it as 'np'

# Convert 'gdp' column to numeric
df2['gdp'] = pd.to_numeric(df2['gdp'], errors='coerce')

# Create new variables
df2['gdp_squared'] = df2['gdp'] ** 2  # Creating a new column 'gdp_squared' which contains the square of the 'gdp' column
df2['gdp_square_root'] = np.sqrt(df2['gdp'])  # Creating a new column 'gdp_square_root' which contains the square root of the 'gdp' column
df2['gdp_log'] = np.log(df2['gdp'])  # Creating a new column 'gdp_log' which contains the natural logarithm of the 'gdp' column
df2['gdp_zscore'] = (df2['gdp'] - df2['gdp'].mean()) / df2['gdp'].std()  # Creating a new column 'gdp_zscore' which contains the Z-score standardized version of the 'gdp' column

# Min-max normalization
min_gdp = df2['gdp'].min()  # Finding the minimum value of the 'gdp' column
max_gdp = df2['gdp'].max()  # Finding the maximum value of the 'gdp' column
df2['gdp_normalized'] = (df2['gdp'] - min_gdp) / (max_gdp - min_gdp)  # Creating a new column 'gdp_normalized' which contains the min-max normalized version of the 'gdp' column

print(df2[['country', 'year', 'gdp', 'gdp_squared', 'gdp_square_root', 'gdp_log', 'gdp_zscore', 'gdp_normalized']])  # Printing the DataFrame with selected columns


# In[233]:


# Step 5: Format Data

import pandas as pd

# Format GDP columns into a readable format (e.g., adding commas for thousands separator)
df2['gdp'] = df2['gdp'].apply(lambda x: '{:,.2f}'.format(x) if isinstance(x, (float, int)) and pd.notnull(x) else None)
df2['gdp_squared'] = df2['gdp_squared'].apply(lambda x: '{:,.2f}'.format(x) if isinstance(x, (float, int)) and pd.notnull(x) else None)
df2['gdp_square_root'] = df2['gdp_square_root'].apply(lambda x: '{:,.2f}'.format(x) if isinstance(x, (float, int)) and pd.notnull(x) else None)
df2['gdp_log'] = df2['gdp_log'].apply(lambda x: '{:,.2f}'.format(x) if isinstance(x, (float, int)) and pd.notnull(x) else None)
df2['gdp_zscore'] = df2['gdp_zscore'].apply(lambda x: '{:,.2f}'.format(x) if isinstance(x, (float, int)) and pd.notnull(x) else None)
df2['gdp_normalized'] = df2['gdp_normalized'].apply(lambda x: '{:,.2f}'.format(x) if isinstance(x, (float, int)) and pd.notnull(x) else None)

print(df2)


# In[234]:


# Step 6: There are still some some 'NaN' and 'None' values in the dataset, let remove them

# Replace 'None' values with NaN
df2.replace('None', np.nan, inplace=True)

# Remove rows with NaN values
df2.dropna(inplace=True)

# Reset index after dropping rows
df2.reset_index(drop=True, inplace=True)

# Display the cleaned DataFrame
print("DataFrame after removing NaN and None values:")
print(df2)


# In[235]:


# Step 7: Converting each variable to numeric

import pandas as pd

# Convert 'gdp' and its derived new variables to numeric using the given formula
df2['gdp'] = pd.to_numeric(df2['gdp'].str.replace(',', ''), errors='coerce')
df2['gdp_squared'] = pd.to_numeric(df2['gdp_squared'].str.replace(',', ''), errors='coerce')
df2['gdp_square_root'] = pd.to_numeric(df2['gdp_square_root'], errors='coerce')
df2['gdp_log'] = pd.to_numeric(df2['gdp_log'], errors='coerce')
df2['gdp_zscore'] = pd.to_numeric(df2['gdp_zscore'], errors='coerce')
df2['gdp_normalized'] = pd.to_numeric(df2['gdp_normalized'], errors='coerce')

# Calculate z-score for the 'gdp' column
z_scores_gdp = ((df2['gdp'] - df2['gdp'].mean()) / df2['gdp'].std()).abs()
outliers_gdp = z_scores_gdp > 3

# Calculate z-score for the 'gdp_squared' column
z_scores_gdp_squared = ((df2['gdp_squared'] - df2['gdp_squared'].mean()) / df2['gdp_squared'].std()).abs()
outliers_gdp_squared = z_scores_gdp_squared > 3

# Print outliers for each variable
print("Outliers for 'gdp':")
print(outliers_gdp)

print("Outliers for 'gdp_squared':")
print(outliers_gdp_squared)


# In[ ]:





# In[236]:


# print last few rows of df2 dataset

df2.tail()


# In[ ]:





# In[163]:


# Step 8: Fix Inconsistent Values: convert all strings to lowercase to address inconsistent capitalization

df2['country'] = df2['country'].str.lower()

print(df2)


# In[213]:


# Step 9: Replace Inconsistent Values with Standardized Ones
# For example, replacing 'united states' with 'United States of America'
df2['country'].replace({'united states': 'United States of America'}, inplace=True)

print(df2)


# In[214]:


# Step 10: Making countries names start with capital letter, except preposition
# List of common prepositions to be converted to lowercase
prepositions = ['on', 'and', 'in', 'to', 'with', 'by', 'at', 'for', 'of', 'from']

# Function to capitalize each word in a string, except for prepositions
def capitalize_country_name(country):
    words = country.split()  # Split the country name into words
    capitalized_words = [word.capitalize() if word.lower() not in prepositions else word.lower() for word in words]
    return ' '.join(capitalized_words)

# Apply the function to the 'country' column
df2['country'] = df2['country'].apply(capitalize_country_name)

# Print the updated DataFrame
print(df2)


# In[215]:


pip install fuzzywuzzy


# In[216]:


# Step 11: Conduct Fuzzy Matching
    
import pandas as pd
from fuzzywuzzy import fuzz

# Assuming df2 is your DataFrame
# If you're reading it from a CSV or Excel file, use pd.read_csv() or pd.read_excel() respectively.
# For example:
# df2 = pd.read_csv('your_file.csv')

# Function to find fuzzy matches for a given input string in the 'country' column of df2
def fuzzy_match(input_string, choices, threshold=70):
    """
    Find fuzzy matches for input_string in choices list.

    Args:
        input_string (str): Input string to match.
        choices (list): List of strings to search for matches.
        threshold (int, optional): Fuzzy matching threshold (0-100). Defaults to 70.

    Returns:
        list: List of tuples containing (matched_string, similarity_score).
    """
    matches = []
    for choice in choices:
        similarity = fuzz.partial_ratio(input_string, choice)
        if similarity >= threshold:
            matches.append((choice, similarity))
    return matches

# List of 5 countries to perform fuzzy matching for
countries = ['United States', 'France', 'Germany', 'United Kingdom', 'Japan']

# Iterate through each country and find fuzzy matches
for country in countries:
    matches = fuzzy_match(country, df2['country'].tolist())
    if matches:
        print(f"Fuzzy matches for '{country}':")
        for match, similarity in matches:
            print(f"{match} (Similarity: {similarity}%)")
    else:
        print(f"No fuzzy matches found for '{country}'.")


# In[218]:


# Step 12: Cleaned Dataset: Print the cleaned dataset

# Cleaned Dataset: Print the cleaned dataset
print("Cleaned Dataset:")
df2


# In[219]:


# Step 13: Save the DataFrame as a CSV file in the current directory
df2.to_csv("df2.csv", index=False)

# Print a message indicating successful saving
print("df2 dataset saved as df2.csv in the current directory.")


# In[221]:


# Step 14: Export the clean dataset to local computer 

import shutil

# Source file path (current directory)
source_path = "df2.csv"

# Destination directory
destination_dir = "C:\\Users\\MariaStella\\Downloads"

# Move the file to the destination directory
shutil.move(source_path, destination_dir)

# Print the path of the moved file
print("df2 dataset moved to:", destination_dir)


# # Responses to the questions:
# 
# 
# What changes were made to the data?
# Replacing previously used 'non JSON file' by 'Kaggle JSON (countries.json)' dataset. 
# Replacing headers, formatting data, identifying outliers, finding duplicates, fixing inconsistent values, creating new variables, conducting feature engineering, and standardizing country names were among the changes made to the data.
# 
# Are there any legal or regulatory guidelines for your data or project topic?
# Yes, compliance with data protection laws (such as GDPR or HIPAA) and any industry-specific regulations is crucial to ensure data privacy and integrity.
# 
# What risks could be created based on the transformations done?
# Risks include unintentional data loss, misinterpretation of transformed data, potential breaches of data privacy regulations if not handled carefully, and introducing bias through assumptions made during cleaning and transformation.
# 
# Did you make any assumptions in cleaning/transforming the data?
# Yes, assumptions were made regarding outlier thresholds, data formats based on common conventions, and the standardization of country names.
# 
# How was your data sourced/verified for credibility?
# Data credibility was ensured by verifying the reputation of the data source, cross-referencing with other reliable sources, conducting data quality checks, and applying domain knowledge expertise where applicable.
# 
# Was your data acquired in an ethical way?
# Yes, data acquisition followed ethical guidelines, including obtaining consent where necessary, respecting data privacy rights, and ensuring transparency in data collection practices.
# 
# How would you mitigate any of the ethical implications you have identified?
# Mitigation strategies include anonymizing sensitive data, obtaining explicit consent for data usage, implementing strict access controls to safeguard privacy, conducting regular audits for compliance with regulations, and promoting transparency in data handling practices.

# Ethical Implications:
# 
# In cleaning the dataset, several changes were made to enhance its readability and integrity. These changes included replacing headers with more descriptive names, removing duplicate entries, and ensuring consistency in data representation. While there are no specific legal guidelines for this project topic, ethical considerations revolve around maintaining data accuracy, integrity, and privacy. Risks associated with data transformations include unintentional errors or biases that could influence decision-making processes. Assumptions were made during the cleaning process, such as assuming that duplicate entries were due to data entry errors. The dataset was sourced from Kaggle, a reputable platform known for its high-quality datasets, and steps were taken to verify its credibility by cross-referencing with other reliable sources. The data acquisition process followed ethical guidelines, and measures were taken to ensure data privacy and integrity. To mitigate ethical implications, transparency in data handling and documentation of all cleaning steps were maintained throughout the process. Additionally, sensitivity to privacy concerns and ethical considerations was prioritized in all data-related decisions.
# 
# 

# Project title: Trend Analysis on Global Live Animals Import and Export Marketing and Impact of GDP and Population Density
# 
# Milestone 2: Cleaning/Formatting Flat File Source
# 
# Summary: The second milestone of this project involved several data transformation and cleansing steps on the flat file dataset. A total of eleven transformations were applied to ensure the dataset is clean and formatted correctly. These transformations included replacing headers, creating new variables, feature engineering, formatting data, handling missing values, converting variables to numeric, fixing inconsistent values, replacing inconsistent values with standardized ones, making country names start with a capital letter, and conducting fuzzy matching analysis. The goal was to achieve a clean dataset ready for further analysis.
# 
# Introduction: Data cleaning and formatting are critical steps in preparing a dataset for analysis. In this milestone, the focus was on cleaning and formatting a flat file dataset to ensure consistency, accuracy, and readiness for analysis. By applying various transformation techniques, the aim was to address issues such as missing data, outliers, inconsistent formatting, and inconsistent values, ultimately producing a clean and standardized dataset.
# 
# Statement of the Problem: The Agricultural GDP (% out of the total GDP) dataset obtained from the Kaggle JSON API (countries.json) source may contain errors, inconsistencies, or missing values that could compromise the integrity of the analysis. Therefore, it was essential to perform data cleaning and formatting to ensure the dataset's accuracy and reliability. Ethical considerations such as data privacy, integrity, and transparency must be upheld throughout the data wrangling process.
# 
# Methodology: Eleven data transformation and cleansing steps were applied to the flat file dataset. These steps included replacing headers, creating new variables based on existing columns, feature engineering, formatting data into a more readable format, handling missing values by replacing 'None' with NaN and removing rows with NaN values, converting variables to numeric, fixing inconsistent values by converting all country names to lowercase and replacing inconsistent country names with standardized ones, making country names start with a capital letter, and conducting fuzzy matching analysis to find similar country names. Each step was clearly labeled and described to provide transparency and clarity in the data wrangling process.
# 
# Results: Upon completion of the data transformation and cleansing steps, the Agricultural GDP dataset was found to be clean, consistent, and formatted correctly. The human-readable dataset printed at the end of the milestone demonstrated the effectiveness of the applied transformations, with improved readability and accuracy. The dataset was saved as a CSV file named "df2.csv" and exported to the local computer for further analysis.
# 
# Discussion: The data transformation and cleansing steps are essential for ensuring the integrity and reliability of the dataset. By addressing issues such as outliers, duplicates, inconsistent formatting, and inconsistent values, the quality of the data was improved, minimizing the risk of erroneous conclusions. Ethical implications such as data privacy and integrity were carefully considered throughout the process to uphold ethical standards and maintain trust in the analysis.
# 
# Conclusion: In conclusion, the data transformation and cleansing steps applied in this milestone play a crucial role in preparing the flat file dataset for analysis. By identifying and addressing issues such as outliers, duplicates, inconsistent formatting, and inconsistent values, the dataset was cleaned, consistent, and ready for further exploration. Moving forward, the clean dataset will serve as the foundation for subsequent analyses and insights in the project.
# 
# The Way Forward: The next steps will involve conducting exploratory data analysis (EDA) and visualization to gain insights into the relationships and patterns within the dataset. By analyzing the cleaned dataset, trends, correlations, and anomalies can be uncovered, providing valuable insights into the subject area. Ethical considerations will continue to be prioritized, with a focus on maintaining data privacy, integrity, and transparency throughout the analysis process.

# In[ ]:




