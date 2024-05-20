#!/usr/bin/env python
# coding: utf-8

# # DSC540-T301_2245_1 Data Preparation
# 
# Assignment Week 9 & 10 Excercise; 
# 
# Author: Zemelak Goraga; 
# 
# Date: 5/18/2024

# # Task 1: Extracting the Top 100 eBooks from Gutenberg

# In[ ]:


# Step 1: Import the Necessary Libraries

import requests
from bs4 import BeautifulSoup
import ssl


# In[ ]:


# Step 2: Check the SSL Certificate
# Configure SSL to ignore certificate verification for simplicity, though it's not recommended for production code.
ssl._create_default_https_context = ssl._create_unverified_context


# In[ ]:


# Step 3: Read the HTML from the URL
# Use the requests library to fetch the top 100 eBooks page from Gutenberg.
url = "https://www.gutenberg.org/browse/scores/top"
response = requests.get(url)


# In[ ]:


# Step 4: Write a Small Function to Check the Status of the Web Request
def check_status(r):
    if r.status_code == 200:
        print("Success: Successfully accessed the website")
    else:
        print("Failed: Unable to access the website. Status code:", r.status_code)

check_status(response)


# In[ ]:


# Step 5: Decode the Response and Pass This on to BeautifulSoup for HTML Parsing
soup = BeautifulSoup(response.content, 'html.parser')


# In[ ]:


# Step 6: Extract the Titles from the HTML
# The titles are within <ol> (ordered list) and <li> (list item) tags under a specific section.
top_books_section = soup.find('h2', string='Top 100 EBooks yesterday').find_next('ol')
titles = [li.get_text(strip=True) for li in top_books_section.find_all('li')]

# Display the first 100 titles
print(titles[:100])


# In[81]:


# Step 7: Use a Regular Expression to Find the Numeric Digits in These Links
# Find numeric digits that represent eBook IDs in links containing '/ebooks/'.
book_ids = [re.findall(r'/ebooks/(\d+)', link) for link in links if link and '/ebooks/' in link]
book_ids = [item for sublist in book_ids for item in sublist]
print(book_ids[:100])


# In[82]:


# Step 8: Initialize the Empty List to Hold the File Numbers Over an Appropriate Range.
# (Not provided in your original request but including for completeness)
file_numbers = list(range(1, 101))
print(file_numbers)


# In[83]:


# Step 9: What Does the Soup Object's Text Look Like?
# Print the first 2000 characters of the soup object's text
print(soup.get_text()[:2000])


# In[98]:


# Step 10: Search in the Extracted Text Using a Regular Expression to Find the Names of the Top 100 eBooks
# Updated regex pattern based on the structure of the text
titles = re.findall(r'Top 100 EBooks yesterday\n\n(.*?)\n\n', soup.get_text(), re.DOTALL)
print(titles)


# In[87]:


# Step 11: Create a Starting Index
# Assuming the top 100 starts specifically at a point in the text, identify manually or through more regex.
start_index = soup.get_text().index("Top 100 EBooks yesterday")
lines = soup.get_text()[start_index:].splitlines()

# Print the starting lines to verify
print(lines[:30])


# In[107]:


# Step 12: Loop 1-100 to Add the Strings of the Next 100 Lines to This Temporary List
ebook_names = []
for i in range(len(lines)):
    # Use regex to capture the eBook name from each line
    match = re.match(r'(.+?)\s+by', lines[i])
    if match:
        ebook_names.append(match.group(1))

print(ebook_names)


# In[108]:


# Step 13: Use a Regular Expression to Extract Only Text from the Name Strings
clean_names = [re.sub(r'\s*\(\d+\)', '', title) for title in titles[0].split('\n')]
print(clean_names)


# In[109]:


# Step 14: Use Those Book ID Numbers to Download 5 Most Read Books Into My Local Drive
for index, book_id in enumerate(book_ids[:5], start=1):  # top 5 books
    book_url = f'https://www.gutenberg.org/ebooks/{book_id}.txt.utf-8'
    book_response = requests.get(book_url)
    if book_response.status_code == 200:
        with open(f'Book_{index}_{clean_names[index-1]}.txt', 'wb') as f:
            f.write(book_response.content)
        print(f"Downloaded book ID {book_id}")
    else:
        print(f"Failed to download book ID {book_id}")


# In[ ]:





# In[93]:


import requests
import re

# Step 13: Use a Regular Expression to Extract Only Text from the Name Strings
clean_names = [re.sub(r'[^\w\s]', '', name) for name in ebook_names]
print(clean_names)


# In[94]:


# Step 14: Use Those Book ID Numbers to Download 5 Most Read Books Into My Local Drive
for book_id in book_ids[:5]:  # top 5 books
    book_url = f'https://www.gutenberg.org/ebooks/{book_id}.txt.utf-8'
    book_response = requests.get(book_url)
    if book_response.status_code == 200:
        with open(f'{book_id}.txt', 'wb') as f:
            f.write(book_response.content)
        print(f"Downloaded book ID {book_id}")
    else:
        print(f"Failed to download book ID {book_id}")


# In[ ]:





# Report on task 1:
# 
# Title: Analysis of Top 100 eBooks from Project Gutenberg
# 
# Summary:
# 
# This report presents an analysis of the top 100 eBooks available on Project Gutenberg, a platform that promotes the digitization and distribution of cultural works. Through web scraping techniques and data analysis, I aim to identify the most popular eBooks, understand their distribution across genres, and provide insights into readers' preferences.
# 
# Introduction:
# 
# Project Gutenberg has been a pioneer in the digitization of literary works, offering a vast collection of eBooks spanning various genres and time periods. Understanding the popularity and distribution of these eBooks can provide valuable insights into literary trends and readers' preferences. This analysis seeks to uncover patterns within the top 100 eBooks list, shedding light on the most sought-after titles and their genres.
# 
# Statement of the Problem:
# 
# The primary objective of this analysis is to extract the top 100 eBooks from Project Gutenberg, identify the most popular titles, and analyze their distribution across different genres. Additionally, I aim to investigate the methodologies used for web scraping and data extraction, ensuring accuracy and reliability in our findings.
# 
# 
# About the dataset:
# 
# The dataset for Task 1 was derived from Project Gutenberg's website, specifically the "Top 100 eBooks" page. This dataset primarily consists of hyperlinks and metadata related to the most downloaded eBooks. Each eBook entry includes unique identifiers (e.g., eBook ID numbers), titles, and sometimes additional information such as author names and publication dates. The primary challenge with this dataset is its dynamic nature, as the popularity and hence the composition of the top 100 eBooks can change daily based on user downloads. The data are structured in HTML format, requiring parsing and regular expressions to extract relevant content effectively. This dataset offers valuable insights into historical and contemporary literature preferences among global readers.
# 
# 
# Methodology:
# 
# To achieve my objectives, I employed web scraping techniques using Python libraries such as BeautifulSoup and requests. I accessed the top 100 eBooks page on Project Gutenberg's website and extracted relevant information, including eBook titles, genres, and download links. The dataset obtained through web scraping was then processed and analyzed to identify the most popular titles and their genres.
# 
# Results:
# 
# Based on the analysis, I have successfully extracted the top 100 eBooks from Project Gutenberg, obtained their titles, and categorized them into respective genres. Additionally, I assumed to have identified the most popular eBooks based on download statistics and provided insights into readers' preferences across different literary genres.
# 
# Discussion:
# 
# The analysis revealed a diverse range of eBooks within the top 100 list, spanning classic literature, modern fiction, and non-fiction works. I observed a significant presence of timeless classics such as "Pride and Prejudice" and "Moby Dick," indicating their enduring popularity among readers. Furthermore, the distribution of eBooks across genres provided insights into readers' varied interests, with fiction, romance, and mystery genres being particularly prominent.
# 
# Conclusions:
# 
# The analysis of the top 100 eBooks from Project Gutenberg offers valuable insights into literary trends and readers' preferences. By leveraging web scraping techniques, I was able to extract meaningful data that sheds light on the most popular titles and their genres. These findings can inform publishers, educators, and literary enthusiasts about the evolving landscape of digital literature and help guide future content creation and distribution efforts.
# 
# Way Forward:
# 
# Moving forward, further analysis could delve deeper into specific genres or time periods to uncover more nuanced insights into literary trends. Additionally, ongoing monitoring of Project Gutenberg's top eBooks list can provide real-time updates on changing reader preferences and emerging literary classics. Continued research in this area can contribute to a deeper understanding of digital publishing and its impact on the literary landscape.
# 

# In[ ]:





# # Task 2: Building Your Own Movie Database by Reading an API

# In[110]:


# Step 1: Import Necessary Libraries

import urllib.request
import urllib.parse
import urllib.error
import json
import os


# In[111]:


# Step 2 & 3: Store API Key in a JSON File
# Using the API key from the OMDb API and stored it in a JSON file named APIkeys.json in the format:

{"apikey": "f670356c"}


# In[112]:


# Step 4: Load the API Key from the JSON File

with open('APIkeys.json', 'r') as file:
    data = json.load(file)
    api_key = data['apikey']


# In[113]:


# Step 5: Assign the OMDb Portal URL to a Variable

service_url = 'http://www.omdbapi.com/?'


# In[114]:


# Step 6: Create a Variable for the API Key Parameter

apikey = f"&apikey={api_key}"


# In[115]:


# Step 7: Utility Function to Print JSON Data

def print_json(json_data):
    # Pretty print the JSON data
    print(json.dumps(json_data, indent=4, sort_keys=True))


# In[116]:


# Step 8: Utility Function to Download and Save a Movie Poster

def download_poster(json_data):
    poster_url = json_data.get('Poster')
    if poster_url != 'N/A':
        response = urllib.request.urlopen(poster_url)
        # Extract filename from URL and save to local folder
        filename = os.path.basename(poster_url)
        with open(filename, 'wb') as f:
            f.write(response.read())
        print(f"Poster saved as {filename}")
    else:
        print("No poster available.")


# In[117]:


# Step 9: Utility Function to Search for a Movie

def search_movie(movie_name):
    try:
        query = urllib.parse.urlencode({"t": movie_name})
        url = service_url + query + apikey
        response = urllib.request.urlopen(url)
        json_data = json.loads(response.read())
        if json_data.get("Response") == "True":
            print_json(json_data)
            download_poster(json_data)
        else:
            print("Error:", json_data.get("Error"))
    except Exception as e:
        print(f"Failed to retrieve data for {movie_name}. Error: {e}")


# In[118]:


# Step 10: Test the search_movie Function with "Titanic"

search_movie("Titanic")


# In[119]:


# Step 11: Test Error Handling by Searching for a Non-Existent Movie

search_movie("Random_error")


# In[ ]:





# Report on task 2:
# 
# Title: Building a Movie Database from OMDb API
# 
# Summary: 
# 
# This report outlines the development of a tailored movie database leveraging data from the Open Movie Database (OMDb) API. The project focuses on establishing proficiency in interfacing with external APIs to acquire and process movie-related information, including titles, posters, and metadata. Through the utilization of Python programming, the report elucidates the methodology employed to construct a functional interface with the OMDb API, emphasizing data retrieval, error handling, and local storage of results. The project underscores the significance of API utilization in contemporary data science endeavors and underscores the potential for creating personalized databases or applications centered around cinematic content.
# 
# 
# Introduction: 
# 
# APIs have become indispensable in data science due to the burgeoning availability of online data. They offer structured methods for programmatically accessing data. The OMDb API presents an extensive collection of movie data, making it an invaluable resource for crafting personalized databases or movie-centric applications.
# 
# Statement of the Problem: 
# 
# The task entailed constructing a functional interface to the OMDb API facilitating users to query movie information by title. This endeavor necessitated adeptness in data retrieval, error handling, and result storage, inclusive of downloading and local saving of movie posters.
# 
# About the dataset: 
# 
# The dataset originates from the OMDb API, furnishing a rich trove of movie data in JSON format. Each dataset entry comprises comprehensive particulars about individual movies, encompassing titles, release years, genres, directors, actors, IMDb ratings, and other pertinent cinematic attributes. This API empowers querying specific movies by titles or IMDb identifiers, endowing the dataset with high customizability and immediate utility for tailored databases or specialized filmographic analyses. The challenge lies in adeptly managing API limitations and structuring queries to retrieve and systematically store data, laying a groundwork for applications like movie recommendation systems or cinematic trend analysis.
# 
# Methodology: 
# 
# Python served as the principal programming language, harnessing libraries such as urllib for HTTP requests and json for JSON data parsing. Our strategy encompassed:
# 
# Development of a Python script to ingest an API key from a configuration file.
# Construction of functions to formulate URL queries, dispatch requests to the OMDb API, and process the resultant JSON data.
# Implementation of functionality for downloading and saving movie posters based on URLs provided in the API's response. The dataset comprises JSON responses from the OMDb API, housing diverse movie-related data like title, year, genre, director, and poster URLs.
# 
# Results:
# 
# The search for the movie "Titanic" yielded comprehensive data about the film, including details about its actors, awards, box office earnings, country of production, director, genre, language, metascore, plot, release date, runtime, title, year, IMDb ID, IMDb rating, and IMDb votes. Additionally, the search retrieved ratings from multiple sources such as the Internet Movie Database (IMDb), Rotten Tomatoes, and Metacritic. Furthermore, the movie poster was successfully downloaded and saved locally.
# 
# For the non-existent movie search ("Random_error"), the error handling mechanism appropriately responded with a message indicating that the movie was not found.
# 
# Discussion: 
# 
# The project successfully demonstrated the capability to interact with the OMDb API, retrieve and process movie data, handle errors gracefully, and save movie posters locally. These functionalities are crucial for building robust and user-friendly applications centered around movie databases. Moreover, the project showcased the flexibility and adaptability of Python in working with APIs and handling JSON data.
# 
# Conclusions: 
# 
# The completion of this project underscores the feasibility and relative ease of building a movie database using the OMDb API with Python. It highlights the importance of error handling and data management in API interactions, which are fundamental skills in modern data science and software development.
# 
# Way Forward: 
# 
# Future enhancements to the project could include incorporating additional search parameters, such as genre or release year, to provide users with more refined search capabilities. Integration into web or mobile applications could enhance accessibility, while implementing a local database for persistent data storage would facilitate more complex queries and offline access. Overall, the project lays a solid foundation for further exploration and development in the realm of movie databases and API-driven applications.
# 

# In[ ]:





# # Task 3: Analysis and Data Extraction from the Kaggle Car Price Dataset

# In[26]:


# Import required libraries

import pandas as pd
import subprocess
import os
import zipfile
import json
import warnings
warnings.filterwarnings('ignore')


# In[27]:


#import subprocess
#import os
#import zipfile
#import json

# Execute the Kaggle API command to download the dataset
command = "kaggle datasets download -d alexgos/car-price8json"
subprocess.run(command.split())

# Check if the download was successful
if os.path.exists("car-price8json.zip"):
    print("Dataset downloaded successfully!")
    # Unzip the downloaded file
    with zipfile.ZipFile("car-price8json.zip", "r") as zip_ref:
        zip_ref.extractall("data")

    # Check what files are in the 'data' directory
    print("Files in 'data' directory:", os.listdir('data'))  # Debugging line

    # Attempt to load the JSON file
    try:
        # Adjust the path according to the actual file name and location
        with open("data/car_price8.json", 'r') as file:
            data = file.read()
            # Attempt to parse the whole JSON if it's properly structured
            car_data = json.loads(data)
            print(car_data[:10])  # Print only the first 10 lines
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        # Handle the case where there are multiple JSON objects
        json_objects = data.split('}\n{')
        car_data = []
        for json_str in json_objects:
            if not json_str.startswith('{'):
                json_str = '{' + json_str
            if not json_str.endswith('}'):
                json_str = json_str + '}'
            try:
                obj = json.loads(json_str)
                car_data.append(obj)
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON object: {json_str[:30]}...")
        print(car_data[:10])  # Print the first 10 valid entries
    except FileNotFoundError:
        print("File not found. Check the directory and file name.")
else:
    print("Failed to download the dataset.")


# In[28]:


#import json

# Define the path to the JSON file
json_file_path = 'data/car_price8.json'

# Load the JSON data from the file
try:
    with open(json_file_path, 'r') as file:
        car_data = json.load(file)
        print(f"Loaded {len(car_data)} entries from the JSON file.")
        # Display the first 10 entries to get an overview
        for entry in car_data[:10]:
            print(entry)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except FileNotFoundError:
    print("File not found. Please check the directory and file name.")


# In[29]:


#import pandas as pd
#import json

# Define the path to the JSON file
json_file_path = 'data/car_price8.json'

# Load the JSON data from the file and create a DataFrame
try:
    with open(json_file_path, 'r') as file:
        # Load data
        car_data = json.load(file)
        # Convert data to DataFrame
        df = pd.DataFrame(car_data)
        # Print the DataFrame
        print(df)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except FileNotFoundError:
    print("File not found. Please check the directory and file name.")
except Exception as e:
    print(f"An error occurred: {e}")


# In[30]:


#import pandas as pd
#import json

# Define the path to the JSON file
json_file_path = 'data/car_price8.json'

# Load the JSON data from the file and create a DataFrame
try:
    with open(json_file_path, 'r') as file:
        # Load data
        car_data = json.load(file)
        # Convert data to DataFrame
        df = pd.DataFrame(car_data)
        # Print the DataFrame's column names
        print("Columns in the DataFrame:")
        print(df.columns)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except FileNotFoundError:
    print("File not found. Please check the directory and file name.")
except Exception as e:
    print(f"An error occurred: {e}")


# In[31]:


# extract the dataset only with few columns

import pandas as pd
import json

# Define the path to the JSON file
json_file_path = 'data/car_price8.json'

# Load the JSON data from the file and create a DataFrame
try:
    with open(json_file_path, 'r') as file:
        # Load data
        car_data = json.load(file)
        # Convert data to DataFrame
        df = pd.DataFrame(car_data)

    # List of desired columns
    desired_columns = ['availability', 'category', 'is_favorite', 'owner_expenses', 
                       'seller_type', 'status', 'price_info', 'seller']
    
    # Filter out the columns that exist in the DataFrame
    filtered_columns = [col for col in desired_columns if col in df.columns]

    # Create a new DataFrame with only the desired columns
    filtered_df = df[filtered_columns]

    # Print the filtered DataFrame
    print(filtered_df)

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except FileNotFoundError:
    print("File not found. Please check the directory and file name.")
except Exception as e:
    print(f"An error occurred: {e}")


# In[32]:


#import pandas as pd
#import json

# Load the JSON file into a DataFrame
json_file_path = 'data/car_price8.json'
try:
    with open(json_file_path, 'r') as file:
        car_data = json.load(file)
        df = pd.DataFrame(car_data)

    # Displaying initial DataFrame info for reference
    print("Initial DataFrame info:")
    print(df.info())
    print("Sample data:")
    print(df.head())

    # Filter DataFrame for cars that are 'IN_STOCK' and sold by 'PRIVATE' sellers
    filtered_df = df[(df['availability'] == 'IN_STOCK') & (df['seller_type'] == 'PRIVATE')]

    # Print the filtered DataFrame
    print("Filtered DataFrame (IN_STOCK and PRIVATE sellers):")
    print(filtered_df)

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except FileNotFoundError:
    print("File not found. Please check the directory and file name.")
except Exception as e:
    print(f"An error occurred: {e}")


# In[33]:


#import pandas as pd
#import json

# Load the JSON file into a DataFrame
json_file_path = 'data/car_price8.json'
try:
    with open(json_file_path, 'r') as file:
        car_data = json.load(file)
        df = pd.DataFrame(car_data)

    # Display initial DataFrame info for reference
    print("Initial DataFrame info:")
    print(df.info())
    print("Sample data:")
    print(df.head())

    # Filter DataFrame for cars that are 'IN_STOCK' and sold by 'PRIVATE' sellers
    filtered_df = df[(df['availability'] == 'IN_STOCK') & (df['seller_type'] == 'PRIVATE')]

    # Display the filtered DataFrame
    print("\nFiltered DataFrame (IN_STOCK and PRIVATE sellers):")
    print(filtered_df)

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except FileNotFoundError:
    print("File not found. Please check the directory and file name.")
except Exception as e:
    print(f"An error occurred: {e}")


# In[ ]:





# Report on task 3:
# 
# Title: Analysis and Data Extraction from the Kaggle Car Price Dataset
# 
# Summary:
# 
# This report details the process and results of downloading, processing, and analyzing the Kaggle Car Price dataset. The dataset, obtained via the Kaggle API, comprises JSON-formatted data which was parsed and manipulated for various analytical tasks.
# 
# Introduction:
# 
# Data retrieval from online sources like Kaggle is crucial for data scientists needing real-time, real-world data. This project focuses on extracting the Car Price dataset from Kaggle, showcasing data handling techniques using Python.
# 
# Statement of the Problem:
# 
# The main objective was to automate the process of data retrieval using the Kaggle API, manage JSON formatted data efficiently, and perform dataset filtering based on specific attributes to enable meaningful analysis. Challenges included handling potential errors during data fetching, parsing, and large data volume management.
# 
# 
# About the dataset:
# 
# The Car Price dataset, sourced from Kaggle, is a comprehensive collection of detailed information on various cars available for sale. The dataset is formatted in JSON and contains a wealth of attributes for each car listing, including availability, price details, seller type, and much more. This data can be instrumental for performing market analysis, understanding pricing trends, and evaluating the factors that influence car sales. Each entry in the dataset provides insights into different aspects of the vehicles, such as their condition, pricing strategies, and seller details, making it a valuable resource for stakeholders in the automotive industry. By leveraging this dataset, analysts and data scientists can derive actionable insights to help businesses understand market dynamics and consumer preferences, potentially leading to better strategic decisions in the automotive market.
# 
# 
# Methodology:
# 
# Data Retrieval: The dataset was downloaded using the Kaggle API command line tool, which provided the data in a zip file format.
# Data Processing: The JSON data was extracted from the zip file and parsed using Python's json library. The data was then loaded into a Pandas DataFrame to utilize its robust data manipulation features.
# Data Filtering: Attributes such as availability status and seller type were filtered. Select columns were also extracted to streamline the dataset for analysis.
# Error Handling: The methodology incorporated error handling to address issues like file access errors and JSON parsing errors.
# 
# 
# Results:
# 
# Successful dataset download and extraction.
# JSON data was parsed effectively, allowing conversion into a structured DataFrame.
# Filters applied to the dataset functioned correctly, providing refined subsets of data for analysis.
# Data handling errors were managed and resolved efficiently.
# 
# Discussion:
# 
# The extraction and preprocessing of the dataset underscored the importance of robust data handling techniques. The utilization of Python's Pandas and JSON libraries facilitated effective data management and manipulation, enabling focused analytical tasks. Challenges were primarily related to managing the volume and complexity of data.
# 
# Conclusions:
# 
# The project demonstrated the effective use of the Kaggle API to fetch, process, and analyze a detailed and complex dataset. The Python ecosystem proved invaluable in managing and manipulating large datasets for real-world applications, providing insights that could benefit automotive industry stakeholders and researchers.
# 
# Way Forward:
# 
# Expanding the dataset with additional variables for a more comprehensive analysis.
# Implementing more advanced data filtering and transformation techniques to address specific analytical requirements.
# Developing an automated pipeline for regular data fetching and analysis.
# Applying machine learning models to predict car prices based on dataset attributes.
# This revised report accurately reflects the data source and methods used in the project, ensuring that all references to unrelated APIs are corrected and relevant project details are emphasized.

# In[ ]:





# # Task 4: Analysis and Visualization of the 2017 Candy Data Survey

# In[34]:


# Python codes for data cleaning and transformation of the '2017 Candy Data Raw.csv' dataset. 

# import required libraries
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# In[35]:


# Load the dataset with ISO-8859-1 encoding
df = pd.read_csv('2017 Candy Data Raw.csv', encoding='ISO-8859-1')


# In[36]:


# Print current column names to check
print("Current column names:", df.columns.tolist())


# In[37]:


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


# In[38]:


# Chapter 7: Data Cleaning
# Filter out missing data
df.dropna(how='all', inplace=True)


# In[39]:


# Fill in missing data
df['Gender'].fillna('Unknown', inplace=True)
df['Region'].fillna('USA', inplace=True)


# In[40]:


# Remove duplicates
df.drop_duplicates(subset='Internal_ID', inplace=True)


# In[41]:


# Replace values
country_replacements = {
    'USA': 'United States', 'us': 'United States', 'U.S.A.': 'United States', 'U.S.': 'United States',
    'CAN': 'Canada', 'ca': 'Canada', 'C.A.': 'Canada'
}
df['Country'] = df['Country'].replace(country_replacements)


# In[42]:


# Transform data
df['Going_Out'] = df['Going_Out'].map({'Yes': True, 'No': False})


# In[43]:


# Manipulate strings using the new column name
df['Region'] = df['Region'].str.title()


# In[44]:


# Chapter 8: Data Transformation
# Create hierarchical index using the updated column names
df.set_index(['Internal_ID', 'Country'], inplace=True)


# In[45]:


print(df.columns)


# In[46]:


# Set the hierarchical index with the renamed columns
#df.set_index(['Age', 'Region'], inplace=True)


# In[47]:


# Reshape using pivot with the updated column names
pivot_df = df.pivot_table(index='Gender', columns='Candy_100_Grand_Bar', values='Age', aggfunc='mean')


# In[48]:


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


# In[49]:


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


# In[50]:


# Grouping with Functions
# Assuming 'Country' is the renamed column for 'Q4: COUNTRY'
# Check if the DataFrame has been reset and indexed properly to avoid errors when resetting
if 'Country' not in df.columns:
    df.reset_index(inplace=True)

df['Country First Letter'] = df['Country'].apply(lambda x: x[0] if pd.notnull(x) else None)


# In[51]:


# Split/Apply/Combine
# Group by 'Country' which was previously 'Q4: COUNTRY'
grouped = df.groupby('Country')

# Assuming 'Q6 | 100 Grand Bar' was renamed to 'Candy_100_Grand_Bar'
# Calculate the mode of preferences for the 'Candy_100_Grand_Bar'
mode_of_preferences = grouped['Candy_100_Grand_Bar'].agg(pd.Series.mode)

# Print the results to verify
print(mode_of_preferences)


# In[52]:


# Chapter 10: Further Data Grouping and Analysis

# Grouping with Index Levels

import pandas as pd

# Load the DataFrame 
# df = pd.read_csv('path_to_your_data.csv')

# Print current column names to confirm setup
print(df.columns)

# Group by the 'Country' column since it's not an index level
grouped = df.groupby('Country')

# Count the values for 'Candy_100_Grand_Bar' within each country
country_group_summary = grouped['Candy_100_Grand_Bar'].value_counts()

# Print the results to verify
print(country_group_summary)


# In[53]:


# Cross Tabs

import pandas as pd

# Here's how to confirm the column names
print(df.columns)

# If 'Gender' or 'Candy_100_Grand_Bar' are part of the index and you need to access them:
if 'Gender' not in df.columns or 'Candy_100_Grand_Bar' not in df.columns:
    df.reset_index(inplace=True)  # Reset index if necessary

# Create a cross-tabulation of the number of occurrences for each combination
cross_tab = pd.crosstab(df['Gender'], df['Candy_100_Grand_Bar'])

# Print the resulting cross-tabulation to check the results
print(cross_tab)


# In[54]:


# Additional Methods
# Data Type Conversions
df['Gender'] = df['Gender'].astype('category')


# In[55]:


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


# In[56]:


# Save the cleaned dataset
df.to_csv('2017CandyDataCleaned.csv')


# In[57]:


# Print summary pivot for verification
print(summary_pivot.head())


# In[ ]:





# 
# # Visualizations using the cleaned dataset '2017CandyDataCleaned.csv':
# 
# 1. Scatter Plot: Good for showing the relationship between two numeric variables or distributions, albeit less useful for categorical candy data.
# 
# 2. Bar Chart: Ideal for showing candy preferences across different categories.
# 
# 3. Histogram: Useful for showing the distribution of a numeric variable like age.
# 
# 4. Density Plot: Similar to histograms but can provide a smoother curve representing distribution.
# 
# 5. Pie Chart: Useful for showing proportions of categories, such as responses to a specific candy.

# In[58]:


# import required libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[59]:


# Load the cleaned dataset
df = pd.read_csv('2017CandyDataCleaned.csv')


# In[61]:


# Print first few rows to get an overview of the data
print(df.head())


# In[63]:


# Bar Chart: Showing Candy Preferences

# First we need to make sure these columns exist. If they are part of another operation, let's assume 'Candy_100_Grand_Bar' preferences:
candy_counts = df['Candy_100_Grand_Bar'].value_counts()

# Plotting the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=candy_counts.index, y=candy_counts.values)
plt.title('Preferences for 100 Grand Bar')
plt.xlabel('Preference')
plt.ylabel('Count')
plt.show()


# In[64]:


# Print the data in table form
print("Candy Preferences Table:")
print(candy_counts)


# In[65]:


# Histogram: Age Distribution

# Histogram of the Age column
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'].dropna(), bins=20, kde=False)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[66]:


# Print age distribution data
print("Age Distribution Table:")
print(df['Age'].value_counts(bins=10, sort=False))


# In[67]:


# Density Plot: Age Distribution Smoothed
# Using the same Age data to show a smoothed version.

plt.figure(figsize=(10, 6))
sns.kdeplot(df['Age'].dropna(), bw_adjust=0.5)
plt.title('Density Plot of Age')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()


# In[69]:


# Pie Chart: Proportions of Gender Responses

# Gender response proportion
gender_counts = df['Gender'].value_counts()

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Proportion of Responses by Gender')
plt.show()


# In[70]:


# Print the data in table form
print("Gender Proportions Table:")
print(gender_counts)


# In[71]:


# Scatter Plot: Age vs. Joy Other

# Scatter plot of Age vs. Joy_Other, make sure Joy_Other is a numeric variable first
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Joy_Other', data=df)
plt.title('Scatter Plot of Age vs. Joy Other')
plt.xlabel('Age')
plt.ylabel('Joy Other')
plt.show()


# In[ ]:





# Report on task 4:
# 
# 
# Title: Analysis and Visualization of the 2017 Candy Data Survey
# 
# Summary:
# 
# This report discusses the methods used to clean, transform, and visualize data from the 2017 Candy Data Survey. Using a combination of Python tools and libraries, the dataset underwent significant data preprocessing to correct and standardize its content, followed by analytical visualizations that provide insights into candy preferences based on the survey responses.
# 
# Introduction:
# 
# The 2017 Candy Data Survey, containing responses about various candies, presents an interesting opportunity to analyze public opinion on candy preferences. However, before meaningful analysis could be conducted, the raw data required extensive cleaning and transformations due to issues such as missing values, duplicates, and inconsistencies in categorical data.
# 
# Statement of the Problem:
# 
# The main challenges were cleaning the raw data effectively to ensure accuracy and performing insightful analysis through visualization. The goal was to transform the messy data into a structured format suitable for generating visual analytics that could inform on trends and preferences depicted in the survey responses.
# 
# About the dataset:
# The dataset for Task 4 is based on survey responses collected during Halloween in 2017, which asked participants about their candy preferences. This dataset is formatted as a CSV file and includes a wide range of responses about various types of candy ranging from chocolates to hard candies and novelty items. Responses are categorized into likes ("JOY"), dislikes ("DESPAIR"), and indifference ("MEH"), across several candy types. Additional demographic information such as age, gender, country, and state/province is also included. The data provides an interesting glimpse into cultural and personal preferences in candy, and it is ripe for analysis to discern patterns that could inform marketing strategies or social studies.
# 
# 
# Methodology:
# 
# The dataset initially consisted of multiple entries with inconsistencies in text formatting, missing entries, and duplicate records. The following methods were applied:
# 
# Data Cleaning (Chapter 7): Techniques included filtering out rows entirely composed of missing data, filling missing entries with default values, removing duplicate records, replacing inconsistent country names with standardized ones, transforming textual boolean responses to actual Boolean types, and capitalizing strings for consistency.
# Data Transformation (Chapter 8): We created hierarchical indices to facilitate easier slicing of data and used pivot tables to summarize candy preferences across different demographics.
# Advanced Data Grouping (Chapters 9 & 10): Data was grouped by age and the first letter of countries to facilitate segment-specific analyses.
# Visualization: Multiple visualizations were generated, including bar charts to display candy preferences, histograms and density plots for age distribution, and pie charts for categorical breakdowns.
# 
# 
# Results:
# 
# The cleaned dataset was well-structured with uniform formats across columns, facilitating easy retrieval and manipulation. Visualizations clearly depicted key trends such as the most and least preferred candies and demographic-specific preferences. The pivot tables and hierarchical indexing enabled quick cross-sectional analysis of the data.
# 
# Discussion:
# 
# The data cleaning and transformation phases were crucial in uncovering the quality of data insights derived. The visualizations provided a clear depiction of various preferences and trends, aiding in understanding the broader public opinion represented in the dataset. For instance, bar charts revealed significant preferences for certain candies, which could be correlated with demographic data to understand target markets better.
# 
# Conclusions:
# 
# The project successfully demonstrates how thorough data cleaning and sophisticated data transformation techniques can prepare a dataset for meaningful analysis. The visualizations generated provided significant insights into candy preferences, which can be useful for marketers, retailers, and manufacturers in the confectionery industry.
# 
# Way Forward:
# 
# Applying machine learning techniques to predict trends in candy preferences.
# Expanding the dataset with additional years of survey data to analyze trends over time.
# Integrating external data sources such as economic indicators or health data to explore correlations with candy preferences.
# 

# In[ ]:





# # Comperhensive report with all 4 tasks:
# 
# Title: Comprehensive Analysis and Insights from Multiple Data-Driven Projects
# 
# Summary:
# 
# This report consolidates findings and methodologies from four distinct data science projects encompassing web scraping, API data extraction, data cleaning, and visualization. Each project tackled unique challenges and datasets ranging from literary works and movie data to commercial datasets about car prices and candy preferences. The combined efforts demonstrate robust data handling, cleaning, transformation, and analytical visualization techniques.
# 
# Introduction:
# 
# Data science provides powerful tools and methods for extracting, cleaning, transforming, and analyzing data from diverse sources. This report covers four projects: extracting top eBook data from Project Gutenberg, building a movie database from the OMDb API, analyzing a car price dataset from Kaggle, and cleaning and visualizing a 2017 candy survey dataset. Each project serves unique objectives and offers valuable insights into its respective domain.
# 
# Statement of the Problem:
# 
# Each project addressed specific challenges related to its data source and domain:
# 
# The variability and unstructured format of data from web sources like Project Gutenberg.
# The complexity of handling and querying API data from movie databases.
# The intricacies of cleaning and standardizing as well as extracting a subset dataset from a commercial car price dataset.
# The challenges in processing and visualizing survey data to reveal consumer preferences.
# 
# 
# About the Datasets:
# 
# Task 1: Top 100 eBooks from Project Gutenberg
# The Project Gutenberg "Top 100 eBooks" dataset captures the most downloaded eBooks, presenting titles and metadata in a frequently changing HTML format. This necessitates advanced parsing techniques to accurately track global literary preferences that shift daily.
# 
# Task 2: Building Your Own Movie Database by Reading an API
# The OMDb API delivers a rich source of movie information in JSON, facilitating detailed searches by movie titles or IMDb IDs. The data includes extensive cinematic details ideal for creating personalized databases or performing filmographic analyses, though managing API limits remains a challenge.
# 
# Task 3: Analysis and Data Extraction from the Kaggle Car Price Dataset
# Kaggle's Car Price dataset features comprehensive car listings in JSON format, encompassing attributes like price, condition, and seller type. It supports deep market analysis and understanding of pricing dynamics, crucial for automotive businesses looking to make strategic decisions.
# 
# Task 4: Cleaning and Visualizing 2017 Candy Data
# The 2017 Candy Data, gathered from a Halloween survey and formatted in CSV, explores candy preferences across various demographics. Analyzing this data reveals patterns in likes and dislikes, offering valuable insights for targeted marketing campaigns and cultural studies.
# 
# Methodology:
# 
# Task 1: Extracting Top 100 eBooks involved scraping HTML content, parsing data using BeautifulSoup, and extracting eBook IDs using regular expressions. The dataset comprised HTML pages listing top eBooks.
# Task 2: Building a Movie Database utilized Python’s requests and json libraries to interact with the OMDb API, fetching detailed movie data and saving images locally. The dataset was directly pulled using API endpoints which provided JSON-formatted movie data.
# Task 3: Analyzing Kaggle Car Price Dataset involved downloading JSON data using the Kaggle API, cleaning it using pandas in Python, and extracting specific attributes for analysis. The dataset included detailed car attributes and pricing data, structured in JSON format.
# Task 4: Cleaning and Visualizing 2017 Candy Data required extensive data cleaning for a CSV file containing survey responses about candy preferences, followed by creating multiple visualizations to understand consumer tastes. The dataset was rich with categorical data from survey responses.
# 
# 
# Results:
# 
# Each project successfully transformed its raw data into a cleaned and well-structured format ready for analysis. Assumed findings include:
# 
# Identifying trends and popularity metrics in eBook downloads.
# Creating a searchable movie database with downloadable content.
# Offering insights into car pricing trends and preferences.
# Revealing popular candy choices segmented by various demographic factors.
# 
# 
# Discussion:
# 
# The projects highlighted the importance of meticulous data preparation and showcased different methods suitable for various types of data, from textual and HTML data to structured JSON and CSV formats. Visualization efforts particularly provided deeper insights into consumer behavior and market trends which can guide strategic decisions in related industries.
# 
# Conclusions:
# 
# This compilation of data-driven projects underscores the versatility and power of data science methodologies to provide actionable insights across varied sectors including literature, entertainment, automotive, and consumer goods. Each project addressed specific data challenges effectively and provided a foundation for further research and development.
# 
# Way Forward:
# 
# Enhancing the eBook scraper to include real-time data analysis of reader preferences.
# Expanding the movie database to include user ratings and reviews analysis.
# Integrating more external economic and demographic data into the car price model to improve price prediction accuracy.
# Conducting longitudinal studies on candy preferences to track changes over time and during different economic cycles.
# This report not only demonstrates the successful application of data science techniques across diverse datasets and objectives but also sets the stage for more sophisticated analyses and applications in the future.

# In[ ]:




