# DSC540-T301_2245_1 Data Preparation

Assignment Week 5 & 6 Term Project Milstone 2;

Author: Zemelak Goraga;

Date: 4/21/2024


```python
# Import required libraries

import pandas as pd
import subprocess
import os
import zipfile
import json
import warnings
warnings.filterwarnings('ignore')
```


```python
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
```

    Dataset downloaded successfully!
    


```python
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
```

    Dataset downloaded successfully!
                                                                                              Afghanistan  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            Ahmad Shah DURRANI unified the Pashtun tribes ...   
    Geography: Location                                 Southern Asia, north and west of Pakistan, eas...   
    Geography: Geographic coordinates                                                    33 00 N, 65 00 E   
    Geography: Map references                                                                        Asia   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                  20.2% (2021 est.)   
    Economy: Youth unemployment rate (ages 15-24) -...                                              18.6%   
    Economy: Youth unemployment rate (ages 15-24) -...                                              26.4%   
    Economy: Population below poverty line              54.5% (2016 est.)note: % of population with in...   
    Economy: Gini Index coefficient - distribution ...                                        29.4 (2008)   
    
                                                                                                 Akrotiri  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            By terms of the 1960 Treaty of Establishment t...   
    Geography: Location                                 Eastern Mediterranean, peninsula on the southw...   
    Geography: Geographic coordinates                                                    34 37 N, 32 58 E   
    Geography: Map references                                                                 Middle East   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Population below poverty line                                                            NaN   
    Economy: Gini Index coefficient - distribution ...                                                NaN   
    
                                                                                                  Albania  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            After declaring independence from the Ottoman ...   
    Geography: Location                                 Southeastern Europe, bordering the Adriatic Se...   
    Geography: Geographic coordinates                                                    41 00 N, 20 00 E   
    Geography: Map references                                                                      Europe   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                  27.8% (2021 est.)   
    Economy: Youth unemployment rate (ages 15-24) -...                                                28%   
    Economy: Youth unemployment rate (ages 15-24) -...                                              27.6%   
    Economy: Population below poverty line              22% (2020 est.)note: % of population with inco...   
    Economy: Gini Index coefficient - distribution ...  29.4 (2020 est.)note: index (0-100) of income ...   
    
                                                                                                  Algeria  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            Algeria has known many empires and dynasties, ...   
    Geography: Location                                 Northern Africa, bordering the Mediterranean S...   
    Geography: Geographic coordinates                                                     28 00 N, 3 00 E   
    Geography: Map references                                                                      Africa   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                  31.9% (2021 est.)   
    Economy: Youth unemployment rate (ages 15-24) -...                                              27.8%   
    Economy: Youth unemployment rate (ages 15-24) -...                                                54%   
    Economy: Population below poverty line                                               5.5% (2011 est.)   
    Economy: Gini Index coefficient - distribution ...                                   27.6 (2011 est.)   
    
                                                                                           American Samoa  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            Tutuila -- the largest island in American Samo...   
    Geography: Location                                 Oceania, group of islands in the South Pacific...   
    Geography: Geographic coordinates                                                   14 20 S, 170 00 W   
    Geography: Map references                                                                     Oceania   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Population below poverty line                                                             NA   
    Economy: Gini Index coefficient - distribution ...                                                NaN   
    
                                                                                                  Andorra  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            The landlocked Principality of Andorra -- one ...   
    Geography: Location                                 Southwestern Europe, Pyrenees mountains, on th...   
    Geography: Geographic coordinates                                                     42 30 N, 1 30 E   
    Geography: Map references                                                                      Europe   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Population below poverty line                                                            NaN   
    Economy: Gini Index coefficient - distribution ...                                                NaN   
    
                                                                                                   Angola  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            Bantu-speaking people settled in the area now ...   
    Geography: Location                                 Southern Africa, bordering the South Atlantic ...   
    Geography: Geographic coordinates                                                    12 30 S, 18 30 E   
    Geography: Map references                                                                      Africa   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                  18.5% (2021 est.)   
    Economy: Youth unemployment rate (ages 15-24) -...                                              18.2%   
    Economy: Youth unemployment rate (ages 15-24) -...                                              18.8%   
    Economy: Population below poverty line              32.3% (2018 est.)note: % of population with in...   
    Economy: Gini Index coefficient - distribution ...  51.3 (2018 est.)note: index (0-100) of income ...   
    
                                                                                                 Anguilla  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            English settlers from Saint Kitts first coloni...   
    Geography: Location                                 Caribbean, islands between the Caribbean Sea a...   
    Geography: Geographic coordinates                                                    18 15 N, 63 10 W   
    Geography: Map references                                           Central America and the Caribbean   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Population below poverty line                                                23% (2002 est.)   
    Economy: Gini Index coefficient - distribution ...                                                NaN   
    
                                                                                               Antarctica  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            Speculation over the existence of a "southern ...   
    Geography: Location                                    continent mostly south of the Antarctic Circle   
    Geography: Geographic coordinates                                                     90 00 S, 0 00 E   
    Geography: Map references                                                            Antarctic Region   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Population below poverty line                                                            NaN   
    Economy: Gini Index coefficient - distribution ...                                                NaN   
    
                                                                                      Antigua and Barbuda  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            The Siboney were the first people to inhabit t...   
    Geography: Location                                 Caribbean, islands between the Caribbean Sea a...   
    Geography: Geographic coordinates                                                    17 03 N, 61 48 W   
    Geography: Map references                                           Central America and the Caribbean   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Population below poverty line                                                             NA   
    Economy: Gini Index coefficient - distribution ...                                                NaN   
    
                                                                                                Argentina  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            In 1816, the United Provinces of the Río de la...   
    Geography: Location                                 Southern South America, bordering the South At...   
    Geography: Geographic coordinates                                                    34 00 S, 64 00 W   
    Geography: Map references                                                               South America   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                  29.9% (2021 est.)   
    Economy: Youth unemployment rate (ages 15-24) -...                                                25%   
    Economy: Youth unemployment rate (ages 15-24) -...                                              37.1%   
    Economy: Population below poverty line              39.2% (2022 est.)note: % of population with in...   
    Economy: Gini Index coefficient - distribution ...  42 (2021 est.)note: index (0-100) of income di...   
    
                                                                                                  Armenia  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            Armenia prides itself on being the first state...   
    Geography: Location                                 Southwestern Asia, between Turkey (to the west...   
    Geography: Geographic coordinates                                                    40 00 N, 45 00 E   
    Geography: Map references                                                                        Asia   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                  36.1% (2021 est.)   
    Economy: Youth unemployment rate (ages 15-24) -...                                                34%   
    Economy: Youth unemployment rate (ages 15-24) -...                                              38.7%   
    Economy: Population below poverty line              26.5% (2021 est.)note: % of population with in...   
    Economy: Gini Index coefficient - distribution ...  27.9 (2021 est.)note: index (0-100) of income ...   
    
                                                                                                    Aruba  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            Discovered and claimed for Spain in 1499, Arub...   
    Geography: Location                                 Caribbean, island in the Caribbean Sea, north ...   
    Geography: Geographic coordinates                                                    12 30 N, 69 58 W   
    Geography: Map references                                           Central America and the Caribbean   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Population below poverty line                                                             NA   
    Economy: Gini Index coefficient - distribution ...                                                NaN   
    
                                                                              Ashmore and Cartier Islands  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            Indonesian fishermen have long fished in the a...   
    Geography: Location                                 Southeastern Asia, islands in the Indian Ocean...   
    Geography: Geographic coordinates                                                   12 25 S, 123 20 E   
    Geography: Map references                                                              Southeast Asia   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN   
    Economy: Population below poverty line                                                            NaN   
    Economy: Gini Index coefficient - distribution ...                                                NaN   
    
                                                                                                Australia  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            Aboriginal Australians arrived on the continen...   
    Geography: Location                                 Oceania, continent between the Indian Ocean an...   
    Geography: Geographic coordinates                                                   27 00 S, 133 00 E   
    Geography: Map references                                                                     Oceania   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                  10.8% (2021 est.)   
    Economy: Youth unemployment rate (ages 15-24) -...                                              12.7%   
    Economy: Youth unemployment rate (ages 15-24) -...                                               8.9%   
    Economy: Population below poverty line                                                            NaN   
    Economy: Gini Index coefficient - distribution ...  34.3 (2018 est.)note: index (0-100) of income ...   
    
                                                                                                  Austria  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            Once the center of power for the large Austro-...   
    Geography: Location                                       Central Europe, north of Italy and Slovenia   
    Geography: Geographic coordinates                                                    47 20 N, 13 20 E   
    Geography: Map references                                                                      Europe   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                  11.4% (2021 est.)   
    Economy: Youth unemployment rate (ages 15-24) -...                                              11.5%   
    Economy: Youth unemployment rate (ages 15-24) -...                                              11.3%   
    Economy: Population below poverty line              14.8% (2021 est.)note: % of population with in...   
    Economy: Gini Index coefficient - distribution ...  29.8 (2020 est.)note: index (0-100) of income ...   
    
                                                                                               Azerbaijan  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            Azerbaijan -- a secular nation with a majority...   
    Geography: Location                                 Southwestern Asia, bordering the Caspian Sea, ...   
    Geography: Geographic coordinates                                                    40 30 N, 47 30 E   
    Geography: Map references                                                                        Asia   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                  16.5% (2021 est.)   
    Economy: Youth unemployment rate (ages 15-24) -...                                              14.4%   
    Economy: Youth unemployment rate (ages 15-24) -...                                              18.9%   
    Economy: Population below poverty line                                               4.9% (2015 est.)   
    Economy: Gini Index coefficient - distribution ...                                        33.7 (2008)   
    
                                                                                             Bahamas, The  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            Lucayan Indians inhabited the Bahama islands w...   
    Geography: Location                                 chain of islands in the North Atlantic Ocean, ...   
    Geography: Geographic coordinates                                                    24 15 N, 76 00 W   
    Geography: Map references                                           Central America and the Caribbean   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                  30.8% (2021 est.)   
    Economy: Youth unemployment rate (ages 15-24) -...                                              27.5%   
    Economy: Youth unemployment rate (ages 15-24) -...                                              35.6%   
    Economy: Population below poverty line                                               9.3% (2010 est.)   
    Economy: Gini Index coefficient - distribution ...                                                NaN   
    
                                                                                                  Bahrain  \
    url                                                 https://www.cia.gov/the-world-factbook/countri...   
    Introduction: Background                            In 1783, the Sunni AL-KHALIFA family took powe...   
    Geography: Location                                 Middle East, archipelago in the Persian Gulf, ...   
    Geography: Geographic coordinates                                                    26 00 N, 50 33 E   
    Geography: Map references                                                                 Middle East   
    ...                                                                                               ...   
    Economy: Youth unemployment rate (ages 15-24) -...                                   9.9% (2021 est.)   
    Economy: Youth unemployment rate (ages 15-24) -...                                               6.1%   
    Economy: Youth unemployment rate (ages 15-24) -...                                              20.5%   
    Economy: Population below poverty line                                                             NA   
    Economy: Gini Index coefficient - distribution ...                                                NaN   
    
                                                                                             Baker Island  
    url                                                 https://www.cia.gov/the-world-factbook/countri...  
    Introduction: Background                            All of the following US Pacific Island territo...  
    Geography: Location                                                                           Oceania  
    Geography: Geographic coordinates                                                                 NaN  
    Geography: Map references                                                                     Oceania  
    ...                                                                                               ...  
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN  
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN  
    Economy: Youth unemployment rate (ages 15-24) -...                                                NaN  
    Economy: Population below poverty line                                                            NaN  
    Economy: Gini Index coefficient - distribution ...                                                NaN  
    
    [200 rows x 20 columns]
    


```python
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
```

    Dataset downloaded successfully!
    Extracting 'Economy: GDP - composition, by sector of origin - agriculture' for all countries:
    | Country                                       | Agriculture GDP Composition   | Year     |
    |-----------------------------------------------|-------------------------------|----------|
    | Afghanistan                                   | 23%                           | (2016    |
    | Akrotiri                                      |                               |          |
    | Albania                                       | 21.7%                         | (2017    |
    | Algeria                                       | 13.3%                         | (2017    |
    | American Samoa                                | 27.4%                         | (2012)   |
    | Andorra                                       | 11.9%                         | (2015    |
    | Angola                                        | 10.2%                         | (2011    |
    | Anguilla                                      | 3%                            | (2017    |
    | Antarctica                                    |                               |          |
    | Antigua and Barbuda                           | 1.8%                          | (2017    |
    | Argentina                                     | 10.8%                         | (2017    |
    | Armenia                                       | 16.7%                         | (2017    |
    | Aruba                                         | 0.4%                          | (2002    |
    | Ashmore and Cartier Islands                   |                               |          |
    | Australia                                     | 3.6%                          | (2017    |
    | Austria                                       | 1.3%                          | (2017    |
    | Azerbaijan                                    | 6.1%                          | (2017    |
    | Bahamas, The                                  | 2.3%                          | (2017    |
    | Bahrain                                       | 0.3%                          | (2017    |
    | Baker Island                                  |                               |          |
    | Bangladesh                                    | 14.2%                         | (2017    |
    | Barbados                                      | 1.5%                          | (2017    |
    | Belarus                                       | 8.1%                          | (2017    |
    | Belgium                                       | 0.7%                          | (2017    |
    | Belize                                        | 10.3%                         | (2017    |
    | Benin                                         | 26.1%                         | (2017    |
    | Bermuda                                       | 0.9%                          | (2017    |
    | Bhutan                                        | 16.2%                         | (2017    |
    | Bolivia                                       | 13.8%                         | (2017    |
    | Bosnia and Herzegovina                        | 6.8%                          | (2017    |
    | Botswana                                      | 1.8%                          | (2017    |
    | Bouvet Island                                 |                               |          |
    | Brazil                                        | 6.6%                          | (2017    |
    | British Indian Ocean Territory                |                               |          |
    | British Virgin Islands                        | 0.2%                          | (2017    |
    | Brunei                                        | 1.2%                          | (2017    |
    | Bulgaria                                      | 4.3%                          | (2017    |
    | Burkina Faso                                  | 31%                           | (2017    |
    | Burma                                         | 24.1%                         | (2017    |
    | Burundi                                       | 39.5%                         | (2017    |
    | Cabo Verde                                    | 8.9%                          | (2017    |
    | Cambodia                                      | 25.3%                         | (2017    |
    | Cameroon                                      | 16.7%                         | (2017    |
    | Canada                                        | 1.6%                          | (2017    |
    | Cayman Islands                                | 0.3%                          | (2017    |
    | Central African Republic                      | 43.2%                         | (2017    |
    | Chad                                          | 52.3%                         | (2017    |
    | Chile                                         | 4.2%                          | (2017    |
    | China                                         | 7.9%                          | (2017    |
    | Christmas Island                              |                               |          |
    | Clipperton Island                             |                               |          |
    | Cocos (Keeling) Islands                       |                               |          |
    | Colombia                                      | 7.2%                          | (2017    |
    | Comoros                                       | 47.7%                         | (2017    |
    | Congo, Democratic Republic of the             | 19.7%                         | (2017    |
    | Congo, Republic of the                        | 9.3%                          | (2017    |
    | Cook Islands                                  | 5.1%                          | (2010    |
    | Coral Sea Islands                             |                               |          |
    | Costa Rica                                    | 5.5%                          | (2017    |
    | Croatia                                       | 3.7%                          | (2017    |
    | Cuba                                          | 4%                            | (2017    |
    | Curacao                                       | 0.7%                          | (2012    |
    | Cyprus                                        | 2%                            | (2017    |
    | Czechia                                       | 2.3%                          | (2017    |
    | Denmark                                       | 1.3%                          | (2017    |
    | Dhekelia                                      |                               |          |
    | Djibouti                                      | 2.4%                          | (2017    |
    | Dominica                                      | 22.3%                         | (2017    |
    | Dominican Republic                            | 5.6%                          | (2017    |
    | Ecuador                                       | 6.7%                          | (2017    |
    | Egypt                                         | 11.7%                         | (2017    |
    | El Salvador                                   | 12%                           | (2017    |
    | Equatorial Guinea                             | 2.5%                          | (2017    |
    | Eritrea                                       | 11.7%                         | (2017    |
    | Estonia                                       | 2.8%                          | (2017    |
    | Eswatini                                      | 6.5%                          | (2017    |
    | Ethiopia                                      | 34.8%                         | (2017    |
    | Falkland Islands (Islas Malvinas)             | 41%                           | (2015    |
    | Faroe Islands                                 | 18%                           | (2013    |
    | Fiji                                          | 13.5%                         | (2017    |
    | Finland                                       | 2.7%                          | (2017    |
    | France                                        | 1.7%                          | (2017    |
    | French Polynesia                              | 2.5%                          | (2009)   |
    | French Southern and Antarctic Lands           |                               |          |
    | Gabon                                         | 5%                            | (2017    |
    | Gambia, The                                   | 20.4%                         | (2017    |
    | Gaza Strip                                    | 3%                            | (2017    |
    | Georgia                                       | 8.2%                          | (2017    |
    | Germany                                       | 0.7%                          | (2017    |
    | Ghana                                         | 18.3%                         | (2017    |
    | Gibraltar                                     | 0%                            | (2016    |
    | Greece                                        | 4.1%                          | (2017    |
    | Greenland                                     | 15.9%                         | (2015    |
    | Grenada                                       | 6.8%                          | (2017    |
    | Guam                                          | NA                            |          |
    | Guatemala                                     | 13.3%                         | (2017    |
    | Guernsey                                      | 3%                            | (2000)   |
    | Guinea                                        | 19.8%                         | (2017    |
    | Guinea-Bissau                                 | 50%                           | (2017    |
    | Guyana                                        | 15.4%                         | (2017    |
    | Haiti                                         | 22.1%                         | (2017    |
    | Heard Island and McDonald Islands             |                               |          |
    | Holy See (Vatican City)                       |                               |          |
    | Honduras                                      | 14.2%                         | (2017    |
    | Hong Kong                                     | 0.1%                          | (2017    |
    | Howland Island                                |                               |          |
    | Hungary                                       | 3.9%                          | (2017    |
    | Iceland                                       | 5.8%                          | (2017    |
    | India                                         | 15.4%                         | (2016    |
    | Indonesia                                     | 13.7%                         | (2017    |
    | Iran                                          | 9.6%                          | (2016    |
    | Iraq                                          | 3.3%                          | (2017    |
    | Ireland                                       | 1.2%                          | (2017    |
    | Isle of Man                                   | 1%                            | (FY12/13 |
    | Israel                                        | 2.4%                          | (2017    |
    | Italy                                         | 2.1%                          | (2017    |
    | Jamaica                                       | 7%                            | (2017    |
    | Jan Mayen                                     |                               |          |
    | Japan                                         | 1.1%                          | (2017    |
    | Jarvis Island                                 |                               |          |
    | Jersey                                        | 2%                            | (2010)   |
    | Johnston Atoll                                |                               |          |
    | Jordan                                        | 4.5%                          | (2017    |
    | Kazakhstan                                    | 4.7%                          | (2017    |
    | Kenya                                         | 34.5%                         | (2017    |
    | Kingman Reef                                  |                               |          |
    | Kiribati                                      | 23%                           | (2016    |
    | Korea, North                                  | 22.5%                         | (2017    |
    | Korea, South                                  | 2.2%                          | (2017    |
    | Kosovo                                        | 11.9%                         | (2017    |
    | Kuwait                                        | 0.4%                          | (2017    |
    | Kyrgyzstan                                    | 14.6%                         | (2017    |
    | Laos                                          | 20.9%                         | (2017    |
    | Latvia                                        | 3.9%                          | (2017    |
    | Lebanon                                       | 3.9%                          | (2017    |
    | Lesotho                                       | 5.8%                          | (2016    |
    | Liberia                                       | 34%                           | (2017    |
    | Libya                                         | 1.3%                          | (2017    |
    | Liechtenstein                                 | 7%                            | (2014)   |
    | Lithuania                                     | 3.5%                          | (2017    |
    | Luxembourg                                    | 0.3%                          | (2017    |
    | Macau                                         | 0%                            | (2016    |
    | Madagascar                                    | 24%                           | (2017    |
    | Malawi                                        | 28.6%                         | (2017    |
    | Malaysia                                      | 8.8%                          | (2017    |
    | Maldives                                      | 3%                            | (2015    |
    | Mali                                          | 41.8%                         | (2017    |
    | Malta                                         | 1.1%                          | (2017    |
    | Marshall Islands                              | 4.4%                          | (2013    |
    | Mauritania                                    | 27.8%                         | (2017    |
    | Mauritius                                     | 4%                            | (2017    |
    | Mexico                                        | 3.6%                          | (2017    |
    | Micronesia, Federated States of               | 26.3%                         | (2013    |
    | Midway Islands                                |                               |          |
    | Moldova                                       | 17.7%                         | (2017    |
    | Monaco                                        | 0%                            | (2013)   |
    | Mongolia                                      | 12.1%                         | (2017    |
    | Montenegro                                    | 7.5%                          | (2016    |
    | Montserrat                                    | 1.9%                          | (2017    |
    | Morocco                                       | 14%                           | (2017    |
    | Mozambique                                    | 23.9%                         | (2017    |
    | Namibia                                       | 6.7%                          | (2016    |
    | Nauru                                         | 6.1%                          | (2009    |
    | Navassa Island                                |                               |          |
    | Nepal                                         | 27%                           | (2017    |
    | Netherlands                                   | 1.6%                          | (2017    |
    | New Caledonia                                 | 1.4%                          | (2017    |
    | New Zealand                                   | 5.7%                          | (2017    |
    | Nicaragua                                     | 15.5%                         | (2017    |
    | Niger                                         | 41.6%                         | (2017    |
    | Nigeria                                       | 21.1%                         | (2016    |
    | Niue                                          | 23.5%                         | (2003)   |
    | Norfolk Island                                |                               |          |
    | North Macedonia                               | 10.9%                         | (2017    |
    | Northern Mariana Islands                      | 1.7%                          | (2016)   |
    | Norway                                        | 2.3%                          | (2017    |
    | Oman                                          | 1.8%                          | (2017    |
    | Pakistan                                      | 24.4%                         | (2016    |
    | Palau                                         | 3%                            | (2016    |
    | Palmyra Atoll                                 |                               |          |
    | Panama                                        | 2.4%                          | (2017    |
    | Papua New Guinea                              | 22.1%                         | (2017    |
    | Paracel Islands                               |                               |          |
    | Paraguay                                      | 17.9%                         | (2017    |
    | Peru                                          | 7.6%                          | (2017    |
    | Philippines                                   | 9.6%                          | (2017    |
    | Pitcairn Islands                              |                               |          |
    | Poland                                        | 2.4%                          | (2017    |
    | Portugal                                      | 2.2%                          | (2017    |
    | Puerto Rico                                   | 0.8%                          | (2017    |
    | Qatar                                         | 0.2%                          | (2017    |
    | Romania                                       | 4.2%                          | (2017    |
    | Russia                                        | 4.7%                          | (2017    |
    | Rwanda                                        | 30.9%                         | (2017    |
    | Saint Barthelemy                              |                               |          |
    | Saint Helena, Ascension, and Tristan da Cunha | NA                            |          |
    | Saint Kitts and Nevis                         | 1.1%                          | (2017    |
    | Saint Lucia                                   | 2.9%                          | (2017    |
    | Saint Martin                                  | 1%                            | (2000)   |
    | Saint Pierre and Miquelon                     | 2%                            | (2006    |
    | Saint Vincent and the Grenadines              | 7.1%                          | (2017    |
    | Samoa                                         | 10.4%                         | (2017    |
    | San Marino                                    | 0.1%                          | (2009)   |
    | Sao Tome and Principe                         | 11.8%                         | (2017    |
    | Saudi Arabia                                  | 2.6%                          | (2017    |
    | Senegal                                       | 16.9%                         | (2017    |
    | Serbia                                        | 9.8%                          | (2017    |
    | Seychelles                                    | 2.5%                          | (2017    |
    | Sierra Leone                                  | 60.7%                         | (2017    |
    | Singapore                                     | 0%                            | (2017    |
    | Sint Maarten                                  | 0.4%                          | (2008    |
    | Slovakia                                      | 3.8%                          | (2017    |
    | Slovenia                                      | 1.8%                          | (2017    |
    | Solomon Islands                               | 34.3%                         | (2017    |
    | Somalia                                       | 60.2%                         | (2013    |
    | South Africa                                  | 2.8%                          | (2017    |
    | South Sudan                                   |                               |          |
    | Spain                                         | 2.6%                          | (2017    |
    | Spratly Islands                               |                               |          |
    | Sri Lanka                                     | 7.8%                          | (2017    |
    | Sudan                                         | 39.6%                         | (2017    |
    | Suriname                                      | 11.6%                         | (2017    |
    | Svalbard                                      |                               |          |
    | Sweden                                        | 1.6%                          | (2017    |
    | Switzerland                                   | 0.7%                          | (2017    |
    | Syria                                         | 20%                           | (2017    |
    | Taiwan                                        | 1.8%                          | (2017    |
    | Tajikistan                                    | 28.6%                         | (2017    |
    | Tanzania                                      | 23.4%                         | (2017    |
    | Thailand                                      | 8.2%                          | (2017    |
    | Timor-Leste                                   | 9.1%                          | (2017    |
    | Togo                                          | 28.8%                         | (2017    |
    | Tokelau                                       | NA                            |          |
    | Tonga                                         | 19.9%                         | (2017    |
    | Trinidad and Tobago                           | 0.4%                          | (2017    |
    | Tunisia                                       | 10.1%                         | (2017    |
    | Turkey (Turkiye)                              | 6.8%                          | (2017    |
    | Turkmenistan                                  | 7.5%                          | (2017    |
    | Turks and Caicos Islands                      | 0.5%                          | (2017    |
    | Tuvalu                                        | 24.5%                         | (2012    |
    | Uganda                                        | 28.2%                         | (2017    |
    | Ukraine                                       | 12.2%                         | (2017    |
    | United Arab Emirates                          | 0.9%                          | (2017    |
    | United Kingdom                                | 0.7%                          | (2017    |
    | United States                                 | 0.9%                          | (2017    |
    | Uruguay                                       | 6.2%                          | (2017    |
    | Uzbekistan                                    | 17.9%                         | (2017    |
    | Vanuatu                                       | 27.3%                         | (2017    |
    | Venezuela                                     | 4.7%                          | (2017    |
    | Vietnam                                       | 15.3%                         | (2017    |
    | Virgin Islands                                | 2%                            | (2012    |
    | Wake Island                                   |                               |          |
    | Wallis and Futuna                             | NA                            |          |
    | West Bank                                     | 2.9%                          | (2017    |
    | World                                         | 6.4%                          | (2017    |
    | Yemen                                         | 20.3%                         | (2017    |
    | Zambia                                        | 7.5%                          | (2017    |
    | Zimbabwe                                      | 12%                           | (2017    |
    


```python
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
```

    Dataset downloaded successfully!
    Extracting 'Economy: GDP - composition, by sector of origin - agriculture' for all countries:
    | Country                                       |   Agricultural GDP |   Year |
    |-----------------------------------------------|--------------------|--------|
    | Afghanistan                                   |                 23 |   2016 |
    | Akrotiri                                      |                    |        |
    | Albania                                       |               21.7 |   2017 |
    | Algeria                                       |               13.3 |   2017 |
    | American Samoa                                |               27.4 |   2012 |
    | Andorra                                       |               11.9 |   2015 |
    | Angola                                        |               10.2 |   2011 |
    | Anguilla                                      |                  3 |   2017 |
    | Antarctica                                    |                    |        |
    | Antigua and Barbuda                           |                1.8 |   2017 |
    | Argentina                                     |               10.8 |   2017 |
    | Armenia                                       |               16.7 |   2017 |
    | Aruba                                         |                0.4 |   2002 |
    | Ashmore and Cartier Islands                   |                    |        |
    | Australia                                     |                3.6 |   2017 |
    | Austria                                       |                1.3 |   2017 |
    | Azerbaijan                                    |                6.1 |   2017 |
    | Bahamas, The                                  |                2.3 |   2017 |
    | Bahrain                                       |                0.3 |   2017 |
    | Baker Island                                  |                    |        |
    | Bangladesh                                    |               14.2 |   2017 |
    | Barbados                                      |                1.5 |   2017 |
    | Belarus                                       |                8.1 |   2017 |
    | Belgium                                       |                0.7 |   2017 |
    | Belize                                        |               10.3 |   2017 |
    | Benin                                         |               26.1 |   2017 |
    | Bermuda                                       |                0.9 |   2017 |
    | Bhutan                                        |               16.2 |   2017 |
    | Bolivia                                       |               13.8 |   2017 |
    | Bosnia and Herzegovina                        |                6.8 |   2017 |
    | Botswana                                      |                1.8 |   2017 |
    | Bouvet Island                                 |                    |        |
    | Brazil                                        |                6.6 |   2017 |
    | British Indian Ocean Territory                |                    |        |
    | British Virgin Islands                        |                0.2 |   2017 |
    | Brunei                                        |                1.2 |   2017 |
    | Bulgaria                                      |                4.3 |   2017 |
    | Burkina Faso                                  |                 31 |   2017 |
    | Burma                                         |               24.1 |   2017 |
    | Burundi                                       |               39.5 |   2017 |
    | Cabo Verde                                    |                8.9 |   2017 |
    | Cambodia                                      |               25.3 |   2017 |
    | Cameroon                                      |               16.7 |   2017 |
    | Canada                                        |                1.6 |   2017 |
    | Cayman Islands                                |                0.3 |   2017 |
    | Central African Republic                      |               43.2 |   2017 |
    | Chad                                          |               52.3 |   2017 |
    | Chile                                         |                4.2 |   2017 |
    | China                                         |                7.9 |   2017 |
    | Christmas Island                              |                    |        |
    | Clipperton Island                             |                    |        |
    | Cocos (Keeling) Islands                       |                    |        |
    | Colombia                                      |                7.2 |   2017 |
    | Comoros                                       |               47.7 |   2017 |
    | Congo, Democratic Republic of the             |               19.7 |   2017 |
    | Congo, Republic of the                        |                9.3 |   2017 |
    | Cook Islands                                  |                5.1 |   2010 |
    | Coral Sea Islands                             |                    |        |
    | Costa Rica                                    |                5.5 |   2017 |
    | Croatia                                       |                3.7 |   2017 |
    | Cuba                                          |                  4 |   2017 |
    | Curacao                                       |                0.7 |   2012 |
    | Cyprus                                        |                  2 |   2017 |
    | Czechia                                       |                2.3 |   2017 |
    | Denmark                                       |                1.3 |   2017 |
    | Dhekelia                                      |                    |        |
    | Djibouti                                      |                2.4 |   2017 |
    | Dominica                                      |               22.3 |   2017 |
    | Dominican Republic                            |                5.6 |   2017 |
    | Ecuador                                       |                6.7 |   2017 |
    | Egypt                                         |               11.7 |   2017 |
    | El Salvador                                   |                 12 |   2017 |
    | Equatorial Guinea                             |                2.5 |   2017 |
    | Eritrea                                       |               11.7 |   2017 |
    | Estonia                                       |                2.8 |   2017 |
    | Eswatini                                      |                6.5 |   2017 |
    | Ethiopia                                      |               34.8 |   2017 |
    | Falkland Islands (Islas Malvinas)             |                 41 |   2015 |
    | Faroe Islands                                 |                 18 |   2013 |
    | Fiji                                          |               13.5 |   2017 |
    | Finland                                       |                2.7 |   2017 |
    | France                                        |                1.7 |   2017 |
    | French Polynesia                              |                2.5 |   2009 |
    | French Southern and Antarctic Lands           |                    |        |
    | Gabon                                         |                  5 |   2017 |
    | Gambia, The                                   |               20.4 |   2017 |
    | Gaza Strip                                    |                  3 |   2017 |
    | Georgia                                       |                8.2 |   2017 |
    | Germany                                       |                0.7 |   2017 |
    | Ghana                                         |               18.3 |   2017 |
    | Gibraltar                                     |                  0 |   2016 |
    | Greece                                        |                4.1 |   2017 |
    | Greenland                                     |               15.9 |   2015 |
    | Grenada                                       |                6.8 |   2017 |
    | Guam                                          |                    |        |
    | Guatemala                                     |               13.3 |   2017 |
    | Guernsey                                      |                  3 |   2000 |
    | Guinea                                        |               19.8 |   2017 |
    | Guinea-Bissau                                 |                 50 |   2017 |
    | Guyana                                        |               15.4 |   2017 |
    | Haiti                                         |               22.1 |   2017 |
    | Heard Island and McDonald Islands             |                    |        |
    | Holy See (Vatican City)                       |                    |        |
    | Honduras                                      |               14.2 |   2017 |
    | Hong Kong                                     |                0.1 |   2017 |
    | Howland Island                                |                    |        |
    | Hungary                                       |                3.9 |   2017 |
    | Iceland                                       |                5.8 |   2017 |
    | India                                         |               15.4 |   2016 |
    | Indonesia                                     |               13.7 |   2017 |
    | Iran                                          |                9.6 |   2016 |
    | Iraq                                          |                3.3 |   2017 |
    | Ireland                                       |                1.2 |   2017 |
    | Isle of Man                                   |                  1 |     12 |
    | Israel                                        |                2.4 |   2017 |
    | Italy                                         |                2.1 |   2017 |
    | Jamaica                                       |                  7 |   2017 |
    | Jan Mayen                                     |                    |        |
    | Japan                                         |                1.1 |   2017 |
    | Jarvis Island                                 |                    |        |
    | Jersey                                        |                  2 |   2010 |
    | Johnston Atoll                                |                    |        |
    | Jordan                                        |                4.5 |   2017 |
    | Kazakhstan                                    |                4.7 |   2017 |
    | Kenya                                         |               34.5 |   2017 |
    | Kingman Reef                                  |                    |        |
    | Kiribati                                      |                 23 |   2016 |
    | Korea, North                                  |               22.5 |   2017 |
    | Korea, South                                  |                2.2 |   2017 |
    | Kosovo                                        |               11.9 |   2017 |
    | Kuwait                                        |                0.4 |   2017 |
    | Kyrgyzstan                                    |               14.6 |   2017 |
    | Laos                                          |               20.9 |   2017 |
    | Latvia                                        |                3.9 |   2017 |
    | Lebanon                                       |                3.9 |   2017 |
    | Lesotho                                       |                5.8 |   2016 |
    | Liberia                                       |                 34 |   2017 |
    | Libya                                         |                1.3 |   2017 |
    | Liechtenstein                                 |                  7 |   2014 |
    | Lithuania                                     |                3.5 |   2017 |
    | Luxembourg                                    |                0.3 |   2017 |
    | Macau                                         |                  0 |   2016 |
    | Madagascar                                    |                 24 |   2017 |
    | Malawi                                        |               28.6 |   2017 |
    | Malaysia                                      |                8.8 |   2017 |
    | Maldives                                      |                  3 |   2015 |
    | Mali                                          |               41.8 |   2017 |
    | Malta                                         |                1.1 |   2017 |
    | Marshall Islands                              |                4.4 |   2013 |
    | Mauritania                                    |               27.8 |   2017 |
    | Mauritius                                     |                  4 |   2017 |
    | Mexico                                        |                3.6 |   2017 |
    | Micronesia, Federated States of               |               26.3 |   2013 |
    | Midway Islands                                |                    |        |
    | Moldova                                       |               17.7 |   2017 |
    | Monaco                                        |                  0 |   2013 |
    | Mongolia                                      |               12.1 |   2017 |
    | Montenegro                                    |                7.5 |   2016 |
    | Montserrat                                    |                1.9 |   2017 |
    | Morocco                                       |                 14 |   2017 |
    | Mozambique                                    |               23.9 |   2017 |
    | Namibia                                       |                6.7 |   2016 |
    | Nauru                                         |                6.1 |   2009 |
    | Navassa Island                                |                    |        |
    | Nepal                                         |                 27 |   2017 |
    | Netherlands                                   |                1.6 |   2017 |
    | New Caledonia                                 |                1.4 |   2017 |
    | New Zealand                                   |                5.7 |   2017 |
    | Nicaragua                                     |               15.5 |   2017 |
    | Niger                                         |               41.6 |   2017 |
    | Nigeria                                       |               21.1 |   2016 |
    | Niue                                          |               23.5 |   2003 |
    | Norfolk Island                                |                    |        |
    | North Macedonia                               |               10.9 |   2017 |
    | Northern Mariana Islands                      |                1.7 |   2016 |
    | Norway                                        |                2.3 |   2017 |
    | Oman                                          |                1.8 |   2017 |
    | Pakistan                                      |               24.4 |   2016 |
    | Palau                                         |                  3 |   2016 |
    | Palmyra Atoll                                 |                    |        |
    | Panama                                        |                2.4 |   2017 |
    | Papua New Guinea                              |               22.1 |   2017 |
    | Paracel Islands                               |                    |        |
    | Paraguay                                      |               17.9 |   2017 |
    | Peru                                          |                7.6 |   2017 |
    | Philippines                                   |                9.6 |   2017 |
    | Pitcairn Islands                              |                    |        |
    | Poland                                        |                2.4 |   2017 |
    | Portugal                                      |                2.2 |   2017 |
    | Puerto Rico                                   |                0.8 |   2017 |
    | Qatar                                         |                0.2 |   2017 |
    | Romania                                       |                4.2 |   2017 |
    | Russia                                        |                4.7 |   2017 |
    | Rwanda                                        |               30.9 |   2017 |
    | Saint Barthelemy                              |                    |        |
    | Saint Helena, Ascension, and Tristan da Cunha |                    |        |
    | Saint Kitts and Nevis                         |                1.1 |   2017 |
    | Saint Lucia                                   |                2.9 |   2017 |
    | Saint Martin                                  |                  1 |   2000 |
    | Saint Pierre and Miquelon                     |                  2 |   2006 |
    | Saint Vincent and the Grenadines              |                7.1 |   2017 |
    | Samoa                                         |               10.4 |   2017 |
    | San Marino                                    |                0.1 |   2009 |
    | Sao Tome and Principe                         |               11.8 |   2017 |
    | Saudi Arabia                                  |                2.6 |   2017 |
    | Senegal                                       |               16.9 |   2017 |
    | Serbia                                        |                9.8 |   2017 |
    | Seychelles                                    |                2.5 |   2017 |
    | Sierra Leone                                  |               60.7 |   2017 |
    | Singapore                                     |                  0 |   2017 |
    | Sint Maarten                                  |                0.4 |   2008 |
    | Slovakia                                      |                3.8 |   2017 |
    | Slovenia                                      |                1.8 |   2017 |
    | Solomon Islands                               |               34.3 |   2017 |
    | Somalia                                       |               60.2 |   2013 |
    | South Africa                                  |                2.8 |   2017 |
    | South Sudan                                   |                    |        |
    | Spain                                         |                2.6 |   2017 |
    | Spratly Islands                               |                    |        |
    | Sri Lanka                                     |                7.8 |   2017 |
    | Sudan                                         |               39.6 |   2017 |
    | Suriname                                      |               11.6 |   2017 |
    | Svalbard                                      |                    |        |
    | Sweden                                        |                1.6 |   2017 |
    | Switzerland                                   |                0.7 |   2017 |
    | Syria                                         |                 20 |   2017 |
    | Taiwan                                        |                1.8 |   2017 |
    | Tajikistan                                    |               28.6 |   2017 |
    | Tanzania                                      |               23.4 |   2017 |
    | Thailand                                      |                8.2 |   2017 |
    | Timor-Leste                                   |                9.1 |   2017 |
    | Togo                                          |               28.8 |   2017 |
    | Tokelau                                       |                    |        |
    | Tonga                                         |               19.9 |   2017 |
    | Trinidad and Tobago                           |                0.4 |   2017 |
    | Tunisia                                       |               10.1 |   2017 |
    | Turkey (Turkiye)                              |                6.8 |   2017 |
    | Turkmenistan                                  |                7.5 |   2017 |
    | Turks and Caicos Islands                      |                0.5 |   2017 |
    | Tuvalu                                        |               24.5 |   2012 |
    | Uganda                                        |               28.2 |   2017 |
    | Ukraine                                       |               12.2 |   2017 |
    | United Arab Emirates                          |                0.9 |   2017 |
    | United Kingdom                                |                0.7 |   2017 |
    | United States                                 |                0.9 |   2017 |
    | Uruguay                                       |                6.2 |   2017 |
    | Uzbekistan                                    |               17.9 |   2017 |
    | Vanuatu                                       |               27.3 |   2017 |
    | Venezuela                                     |                4.7 |   2017 |
    | Vietnam                                       |               15.3 |   2017 |
    | Virgin Islands                                |                  2 |   2012 |
    | Wake Island                                   |                    |        |
    | Wallis and Futuna                             |                    |        |
    | West Bank                                     |                2.9 |   2017 |
    | World                                         |                6.4 |   2017 |
    | Yemen                                         |               20.3 |   2017 |
    | Zambia                                        |                7.5 |   2017 |
    | Zimbabwe                                      |                 12 |   2017 |
    
    


```python

```


```python
# Print the last few rows of the dataset
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Agricultural GDP</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>253</th>
      <td>West Bank</td>
      <td>2.9</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>254</th>
      <td>World</td>
      <td>6.4</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>255</th>
      <td>Yemen</td>
      <td>20.3</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>256</th>
      <td>Zambia</td>
      <td>7.5</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>257</th>
      <td>Zimbabwe</td>
      <td>12</td>
      <td>2017</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Copying 'df' to 'df2' # keep 'df' as the original version and here on use df2
df2 = df.copy()

df2

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Agricultural GDP</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>23</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Akrotiri</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Albania</td>
      <td>21.7</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Algeria</td>
      <td>13.3</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>4</th>
      <td>American Samoa</td>
      <td>27.4</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>253</th>
      <td>West Bank</td>
      <td>2.9</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>254</th>
      <td>World</td>
      <td>6.4</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>255</th>
      <td>Yemen</td>
      <td>20.3</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>256</th>
      <td>Zambia</td>
      <td>7.5</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>257</th>
      <td>Zimbabwe</td>
      <td>12</td>
      <td>2017</td>
    </tr>
  </tbody>
</table>
<p>258 rows × 3 columns</p>
</div>




```python
# Step 1: Replace Headers
new_headers = ["country", "gdp", "year"]
df2.columns = new_headers
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>gdp</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>23</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Akrotiri</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Albania</td>
      <td>21.7</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Algeria</td>
      <td>13.3</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>4</th>
      <td>American Samoa</td>
      <td>27.4</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>253</th>
      <td>West Bank</td>
      <td>2.9</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>254</th>
      <td>World</td>
      <td>6.4</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>255</th>
      <td>Yemen</td>
      <td>20.3</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>256</th>
      <td>Zambia</td>
      <td>7.5</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>257</th>
      <td>Zimbabwe</td>
      <td>12</td>
      <td>2017</td>
    </tr>
  </tbody>
</table>
<p>258 rows × 3 columns</p>
</div>




```python
import pandas as pd

# Assuming df2 is your DataFrame
print(df2.dtypes)

```

    country    object
    gdp        object
    year       object
    dtype: object
    


```python
# Step 2: Handling Missing Values
missing_values = df2.isnull().sum()
print("Missing values:\n", missing_values)
```

    Missing values:
     country     0
    gdp        34
    year       34
    dtype: int64
    


```python
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
```

                country  year   gdp  gdp_squared  gdp_square_root   gdp_log  \
    0       Afghanistan  2016  23.0       529.00         4.795832  3.135494   
    1          Akrotiri  None   NaN          NaN              NaN       NaN   
    2           Albania  2017  21.7       470.89         4.658326  3.077312   
    3           Algeria  2017  13.3       176.89         3.646917  2.587764   
    4    American Samoa  2012  27.4       750.76         5.234501  3.310543   
    ..              ...   ...   ...          ...              ...       ...   
    253       West Bank  2017   2.9         8.41         1.702939  1.064711   
    254           World  2017   6.4        40.96         2.529822  1.856298   
    255           Yemen  2017  20.3       412.09         4.505552  3.010621   
    256          Zambia  2017   7.5        56.25         2.738613  2.014903   
    257        Zimbabwe  2017  12.0       144.00         3.464102  2.484907   
    
         gdp_zscore  gdp_normalized  
    0      0.970554        0.378913  
    1           NaN             NaN  
    2      0.863296        0.357496  
    3      0.170243        0.219110  
    4      1.333582        0.451400  
    ..          ...             ...  
    253   -0.687823        0.047776  
    254   -0.399051        0.105437  
    255    0.747787        0.334432  
    256   -0.308294        0.123558  
    257    0.062985        0.197694  
    
    [258 rows x 8 columns]
    


```python
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

```

                country    gdp  year gdp_squared gdp_square_root gdp_log  \
    0       Afghanistan  23.00  2016      529.00            4.80    3.14   
    1          Akrotiri   None  None        None            None    None   
    2           Albania  21.70  2017      470.89            4.66    3.08   
    3           Algeria  13.30  2017      176.89            3.65    2.59   
    4    American Samoa  27.40  2012      750.76            5.23    3.31   
    ..              ...    ...   ...         ...             ...     ...   
    253       West Bank   2.90  2017        8.41            1.70    1.06   
    254           World   6.40  2017       40.96            2.53    1.86   
    255           Yemen  20.30  2017      412.09            4.51    3.01   
    256          Zambia   7.50  2017       56.25            2.74    2.01   
    257        Zimbabwe  12.00  2017      144.00            3.46    2.48   
    
        gdp_zscore gdp_normalized  
    0         0.97           0.38  
    1         None           None  
    2         0.86           0.36  
    3         0.17           0.22  
    4         1.33           0.45  
    ..         ...            ...  
    253      -0.69           0.05  
    254      -0.40           0.11  
    255       0.75           0.33  
    256      -0.31           0.12  
    257       0.06           0.20  
    
    [258 rows x 8 columns]
    


```python
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

```

    DataFrame after removing NaN and None values:
                country    gdp  year gdp_squared gdp_square_root gdp_log  \
    0       Afghanistan  23.00  2016      529.00            4.80    3.14   
    1           Albania  21.70  2017      470.89            4.66    3.08   
    2           Algeria  13.30  2017      176.89            3.65    2.59   
    3    American Samoa  27.40  2012      750.76            5.23    3.31   
    4           Andorra  11.90  2015      141.61            3.45    2.48   
    ..              ...    ...   ...         ...             ...     ...   
    219       West Bank   2.90  2017        8.41            1.70    1.06   
    220           World   6.40  2017       40.96            2.53    1.86   
    221           Yemen  20.30  2017      412.09            4.51    3.01   
    222          Zambia   7.50  2017       56.25            2.74    2.01   
    223        Zimbabwe  12.00  2017      144.00            3.46    2.48   
    
        gdp_zscore gdp_normalized  
    0         0.97           0.38  
    1         0.86           0.36  
    2         0.17           0.22  
    3         1.33           0.45  
    4         0.05           0.20  
    ..         ...            ...  
    219      -0.69           0.05  
    220      -0.40           0.11  
    221       0.75           0.33  
    222      -0.31           0.12  
    223       0.06           0.20  
    
    [224 rows x 8 columns]
    


```python
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

```

    Outliers for 'gdp':
    0      False
    1      False
    2      False
    3      False
    4      False
           ...  
    219    False
    220    False
    221    False
    222    False
    223    False
    Name: gdp, Length: 224, dtype: bool
    Outliers for 'gdp_squared':
    0      False
    1      False
    2      False
    3      False
    4      False
           ...  
    219    False
    220    False
    221    False
    222    False
    223    False
    Name: gdp_squared, Length: 224, dtype: bool
    


```python

```


```python
# print last few rows of df2 dataset

df2.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>gdp</th>
      <th>year</th>
      <th>gdp_squared</th>
      <th>gdp_square_root</th>
      <th>gdp_log</th>
      <th>gdp_zscore</th>
      <th>gdp_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>219</th>
      <td>West Bank</td>
      <td>2.9</td>
      <td>2017</td>
      <td>8.41</td>
      <td>1.70</td>
      <td>1.06</td>
      <td>-0.69</td>
      <td>0.05</td>
    </tr>
    <tr>
      <th>220</th>
      <td>World</td>
      <td>6.4</td>
      <td>2017</td>
      <td>40.96</td>
      <td>2.53</td>
      <td>1.86</td>
      <td>-0.40</td>
      <td>0.11</td>
    </tr>
    <tr>
      <th>221</th>
      <td>Yemen</td>
      <td>20.3</td>
      <td>2017</td>
      <td>412.09</td>
      <td>4.51</td>
      <td>3.01</td>
      <td>0.75</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>222</th>
      <td>Zambia</td>
      <td>7.5</td>
      <td>2017</td>
      <td>56.25</td>
      <td>2.74</td>
      <td>2.01</td>
      <td>-0.31</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>223</th>
      <td>Zimbabwe</td>
      <td>12.0</td>
      <td>2017</td>
      <td>144.00</td>
      <td>3.46</td>
      <td>2.48</td>
      <td>0.06</td>
      <td>0.20</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
# Step 8: Fix Inconsistent Values: convert all strings to lowercase to address inconsistent capitalization

df2['country'] = df2['country'].str.lower()

print(df2)

```

                country   gdp  year  gdp_squared  gdp_square_root  gdp_log  \
    0       afghanistan  23.0  2016       529.00             4.80     3.14   
    1           albania  21.7  2017       470.89             4.66     3.08   
    2           algeria  13.3  2017       176.89             3.65     2.59   
    3    american samoa  27.4  2012       750.76             5.23     3.31   
    4           andorra  11.9  2015       141.61             3.45     2.48   
    ..              ...   ...   ...          ...              ...      ...   
    219       west bank   2.9  2017         8.41             1.70     1.06   
    220           world   6.4  2017        40.96             2.53     1.86   
    221           yemen  20.3  2017       412.09             4.51     3.01   
    222          zambia   7.5  2017        56.25             2.74     2.01   
    223        zimbabwe  12.0  2017       144.00             3.46     2.48   
    
         gdp_zscore  gdp_normalized  gdp_growth_rate  
    0          0.97            0.38              0.0  
    1          0.86            0.36              0.0  
    2          0.17            0.22              0.0  
    3          1.33            0.45              0.0  
    4          0.05            0.20              0.0  
    ..          ...             ...              ...  
    219       -0.69            0.05              0.0  
    220       -0.40            0.11              0.0  
    221        0.75            0.33              0.0  
    222       -0.31            0.12              0.0  
    223        0.06            0.20              0.0  
    
    [224 rows x 9 columns]
    


```python
# Step 9: Replace Inconsistent Values with Standardized Ones
# For example, replacing 'united states' with 'United States of America'
df2['country'].replace({'united states': 'United States of America'}, inplace=True)

print(df2)

```

                country   gdp  year  gdp_squared  gdp_square_root  gdp_log  \
    0       Afghanistan  23.0  2016       529.00             4.80     3.14   
    1           Albania  21.7  2017       470.89             4.66     3.08   
    2           Algeria  13.3  2017       176.89             3.65     2.59   
    3    American Samoa  27.4  2012       750.76             5.23     3.31   
    4           Andorra  11.9  2015       141.61             3.45     2.48   
    ..              ...   ...   ...          ...              ...      ...   
    219       West Bank   2.9  2017         8.41             1.70     1.06   
    220           World   6.4  2017        40.96             2.53     1.86   
    221           Yemen  20.3  2017       412.09             4.51     3.01   
    222          Zambia   7.5  2017        56.25             2.74     2.01   
    223        Zimbabwe  12.0  2017       144.00             3.46     2.48   
    
         gdp_zscore  gdp_normalized  
    0          0.97            0.38  
    1          0.86            0.36  
    2          0.17            0.22  
    3          1.33            0.45  
    4          0.05            0.20  
    ..          ...             ...  
    219       -0.69            0.05  
    220       -0.40            0.11  
    221        0.75            0.33  
    222       -0.31            0.12  
    223        0.06            0.20  
    
    [224 rows x 8 columns]
    


```python
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

```

                country   gdp  year  gdp_squared  gdp_square_root  gdp_log  \
    0       Afghanistan  23.0  2016       529.00             4.80     3.14   
    1           Albania  21.7  2017       470.89             4.66     3.08   
    2           Algeria  13.3  2017       176.89             3.65     2.59   
    3    American Samoa  27.4  2012       750.76             5.23     3.31   
    4           Andorra  11.9  2015       141.61             3.45     2.48   
    ..              ...   ...   ...          ...              ...      ...   
    219       West Bank   2.9  2017         8.41             1.70     1.06   
    220           World   6.4  2017        40.96             2.53     1.86   
    221           Yemen  20.3  2017       412.09             4.51     3.01   
    222          Zambia   7.5  2017        56.25             2.74     2.01   
    223        Zimbabwe  12.0  2017       144.00             3.46     2.48   
    
         gdp_zscore  gdp_normalized  
    0          0.97            0.38  
    1          0.86            0.36  
    2          0.17            0.22  
    3          1.33            0.45  
    4          0.05            0.20  
    ..          ...             ...  
    219       -0.69            0.05  
    220       -0.40            0.11  
    221        0.75            0.33  
    222       -0.31            0.12  
    223        0.06            0.20  
    
    [224 rows x 8 columns]
    


```python
pip install fuzzywuzzy
```

    Requirement already satisfied: fuzzywuzzy in c:\users\mariastella\anaconda3\lib\site-packages (0.18.0)Note: you may need to restart the kernel to use updated packages.
    
    


```python
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

```

    Fuzzy matches for 'United States':
    Micronesia, Federated States of (Similarity: 77%)
    United States (Similarity: 100%)
    Fuzzy matches for 'France':
    France (Similarity: 100%)
    Iran (Similarity: 75%)
    Ukraine (Similarity: 73%)
    Fuzzy matches for 'Germany':
    Germany (Similarity: 100%)
    Iran (Similarity: 75%)
    Oman (Similarity: 75%)
    Fuzzy matches for 'United Kingdom':
    United Kingdom (Similarity: 100%)
    Fuzzy matches for 'Japan':
    Japan (Similarity: 100%)
    


```python
# Step 12: Cleaned Dataset: Print the cleaned dataset

# Cleaned Dataset: Print the cleaned dataset
print("Cleaned Dataset:")
df2
```

    Cleaned Dataset:
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>gdp</th>
      <th>year</th>
      <th>gdp_squared</th>
      <th>gdp_square_root</th>
      <th>gdp_log</th>
      <th>gdp_zscore</th>
      <th>gdp_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>23.0</td>
      <td>2016</td>
      <td>529.00</td>
      <td>4.80</td>
      <td>3.14</td>
      <td>0.97</td>
      <td>0.38</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>21.7</td>
      <td>2017</td>
      <td>470.89</td>
      <td>4.66</td>
      <td>3.08</td>
      <td>0.86</td>
      <td>0.36</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>13.3</td>
      <td>2017</td>
      <td>176.89</td>
      <td>3.65</td>
      <td>2.59</td>
      <td>0.17</td>
      <td>0.22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>American Samoa</td>
      <td>27.4</td>
      <td>2012</td>
      <td>750.76</td>
      <td>5.23</td>
      <td>3.31</td>
      <td>1.33</td>
      <td>0.45</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Andorra</td>
      <td>11.9</td>
      <td>2015</td>
      <td>141.61</td>
      <td>3.45</td>
      <td>2.48</td>
      <td>0.05</td>
      <td>0.20</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>219</th>
      <td>West Bank</td>
      <td>2.9</td>
      <td>2017</td>
      <td>8.41</td>
      <td>1.70</td>
      <td>1.06</td>
      <td>-0.69</td>
      <td>0.05</td>
    </tr>
    <tr>
      <th>220</th>
      <td>World</td>
      <td>6.4</td>
      <td>2017</td>
      <td>40.96</td>
      <td>2.53</td>
      <td>1.86</td>
      <td>-0.40</td>
      <td>0.11</td>
    </tr>
    <tr>
      <th>221</th>
      <td>Yemen</td>
      <td>20.3</td>
      <td>2017</td>
      <td>412.09</td>
      <td>4.51</td>
      <td>3.01</td>
      <td>0.75</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>222</th>
      <td>Zambia</td>
      <td>7.5</td>
      <td>2017</td>
      <td>56.25</td>
      <td>2.74</td>
      <td>2.01</td>
      <td>-0.31</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>223</th>
      <td>Zimbabwe</td>
      <td>12.0</td>
      <td>2017</td>
      <td>144.00</td>
      <td>3.46</td>
      <td>2.48</td>
      <td>0.06</td>
      <td>0.20</td>
    </tr>
  </tbody>
</table>
<p>224 rows × 8 columns</p>
</div>




```python
# Step 13: Save the DataFrame as a CSV file in the current directory
df2.to_csv("df2.csv", index=False)

# Print a message indicating successful saving
print("df2 dataset saved as df2.csv in the current directory.")

```

    df2 dataset saved as df2.csv in the current directory.
    


```python
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

```

    df2 dataset moved to: C:\Users\MariaStella\Downloads
    

# Responses to the questions:


What changes were made to the data?
Replacing previously used 'non JSON file' by 'Kaggle JSON (countries.json)' dataset. 
Replacing headers, formatting data, identifying outliers, finding duplicates, fixing inconsistent values, creating new variables, conducting feature engineering, and standardizing country names were among the changes made to the data.

Are there any legal or regulatory guidelines for your data or project topic?
Yes, compliance with data protection laws (such as GDPR or HIPAA) and any industry-specific regulations is crucial to ensure data privacy and integrity.

What risks could be created based on the transformations done?
Risks include unintentional data loss, misinterpretation of transformed data, potential breaches of data privacy regulations if not handled carefully, and introducing bias through assumptions made during cleaning and transformation.

Did you make any assumptions in cleaning/transforming the data?
Yes, assumptions were made regarding outlier thresholds, data formats based on common conventions, and the standardization of country names.

How was your data sourced/verified for credibility?
Data credibility was ensured by verifying the reputation of the data source, cross-referencing with other reliable sources, conducting data quality checks, and applying domain knowledge expertise where applicable.

Was your data acquired in an ethical way?
Yes, data acquisition followed ethical guidelines, including obtaining consent where necessary, respecting data privacy rights, and ensuring transparency in data collection practices.

How would you mitigate any of the ethical implications you have identified?
Mitigation strategies include anonymizing sensitive data, obtaining explicit consent for data usage, implementing strict access controls to safeguard privacy, conducting regular audits for compliance with regulations, and promoting transparency in data handling practices.

Ethical Implications:

In cleaning the dataset, several changes were made to enhance its readability and integrity. These changes included replacing headers with more descriptive names, removing duplicate entries, and ensuring consistency in data representation. While there are no specific legal guidelines for this project topic, ethical considerations revolve around maintaining data accuracy, integrity, and privacy. Risks associated with data transformations include unintentional errors or biases that could influence decision-making processes. Assumptions were made during the cleaning process, such as assuming that duplicate entries were due to data entry errors. The dataset was sourced from Kaggle, a reputable platform known for its high-quality datasets, and steps were taken to verify its credibility by cross-referencing with other reliable sources. The data acquisition process followed ethical guidelines, and measures were taken to ensure data privacy and integrity. To mitigate ethical implications, transparency in data handling and documentation of all cleaning steps were maintained throughout the process. Additionally, sensitivity to privacy concerns and ethical considerations was prioritized in all data-related decisions.



Project title: Trend Analysis on Global Live Animals Import and Export Marketing and Impact of GDP and Population Density

Milestone 2: Cleaning/Formatting Flat File Source

Summary: The second milestone of this project involved several data transformation and cleansing steps on the flat file dataset. A total of eleven transformations were applied to ensure the dataset is clean and formatted correctly. These transformations included replacing headers, creating new variables, feature engineering, formatting data, handling missing values, converting variables to numeric, fixing inconsistent values, replacing inconsistent values with standardized ones, making country names start with a capital letter, and conducting fuzzy matching analysis. The goal was to achieve a clean dataset ready for further analysis.

Introduction: Data cleaning and formatting are critical steps in preparing a dataset for analysis. In this milestone, the focus was on cleaning and formatting a flat file dataset to ensure consistency, accuracy, and readiness for analysis. By applying various transformation techniques, the aim was to address issues such as missing data, outliers, inconsistent formatting, and inconsistent values, ultimately producing a clean and standardized dataset.

Statement of the Problem: The Agricultural GDP (% out of the total GDP) dataset obtained from the Kaggle JSON API (countries.json) source may contain errors, inconsistencies, or missing values that could compromise the integrity of the analysis. Therefore, it was essential to perform data cleaning and formatting to ensure the dataset's accuracy and reliability. Ethical considerations such as data privacy, integrity, and transparency must be upheld throughout the data wrangling process.

Methodology: Eleven data transformation and cleansing steps were applied to the flat file dataset. These steps included replacing headers, creating new variables based on existing columns, feature engineering, formatting data into a more readable format, handling missing values by replacing 'None' with NaN and removing rows with NaN values, converting variables to numeric, fixing inconsistent values by converting all country names to lowercase and replacing inconsistent country names with standardized ones, making country names start with a capital letter, and conducting fuzzy matching analysis to find similar country names. Each step was clearly labeled and described to provide transparency and clarity in the data wrangling process.

Results: Upon completion of the data transformation and cleansing steps, the Agricultural GDP dataset was found to be clean, consistent, and formatted correctly. The human-readable dataset printed at the end of the milestone demonstrated the effectiveness of the applied transformations, with improved readability and accuracy. The dataset was saved as a CSV file named "df2.csv" and exported to the local computer for further analysis.

Discussion: The data transformation and cleansing steps are essential for ensuring the integrity and reliability of the dataset. By addressing issues such as outliers, duplicates, inconsistent formatting, and inconsistent values, the quality of the data was improved, minimizing the risk of erroneous conclusions. Ethical implications such as data privacy and integrity were carefully considered throughout the process to uphold ethical standards and maintain trust in the analysis.

Conclusion: In conclusion, the data transformation and cleansing steps applied in this milestone play a crucial role in preparing the flat file dataset for analysis. By identifying and addressing issues such as outliers, duplicates, inconsistent formatting, and inconsistent values, the dataset was cleaned, consistent, and ready for further exploration. Moving forward, the clean dataset will serve as the foundation for subsequent analyses and insights in the project.

The Way Forward: The next steps will involve conducting exploratory data analysis (EDA) and visualization to gain insights into the relationships and patterns within the dataset. By analyzing the cleaned dataset, trends, correlations, and anomalies can be uncovered, providing valuable insights into the subject area. Ethical considerations will continue to be prioritized, with a focus on maintaining data privacy, integrity, and transparency throughout the analysis process.


```python

```
