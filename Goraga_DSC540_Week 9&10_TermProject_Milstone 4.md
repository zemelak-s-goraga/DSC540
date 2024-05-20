# DSC540-T301_2245_1 Data Preparation

Assignment Week 9 & 10 Term Project Milstone 4;

Author: Zemelak Goraga;

Date: 5/18/2024

# Milstone 4: Connecting to an API/Pulling in the Data and Cleaning/Formatting

# The dataset:

In this milstone 4 of the term project, the FAOSTAT historical dataset on LiveAnimals was obtained from Kaggle using this API Command (kaggle datasets download -d unitednations/global-food-agriculture-statistics) following the undermentioned procedures. The dataset represent over 200 countries with more than 25 primary products and inputs that were collected in between 1961 to 2013 years. Key variables include in the dataset are Area or Country, Item (Agricult.Products, Cattle, Sheep, Chicken, Crops, etc), Element (Import Quantity, Export Quantity, Import Value, Export Value), Year (1961 – 2013), and Value. 

# Step 1: Connecting to an API/Pulling in the Data and Cleaning/Formatting


```python
# Import required libraries
import subprocess
import os
import zipfile
import pandas as pd
from zipfile import ZipFile
import warnings
warnings.filterwarnings('ignore')
```


```python
# Execute the Kaggle API command to download the dataset
command = "kaggle datasets download -d unitednations/global-food-agriculture-statistics"
subprocess.run(command.split())
```




    CompletedProcess(args=['kaggle', 'datasets', 'download', '-d', 'unitednations/global-food-agriculture-statistics'], returncode=0)




```python
# Step 2: Check if the download was successful
if os.path.exists("global-food-agriculture-statistics.zip"):
    print("Dataset downloaded successfully!")
```

    Dataset downloaded successfully!
    


```python
# Step 3: Unzip the downloaded file
with zipfile.ZipFile("global-food-agriculture-statistics.zip", "r") as zip_ref:
    zip_ref.extractall("data")
```


```python
# Step 4: Optionally, list the contents of the extracted directory
extracted_files = os.listdir("data")
print("Extracted files:", extracted_files)
```

    Extracted files: ['car_price8.json', 'countries.csv', 'countries.json', 'current_FAO', 'fao_data_crops_data.csv', 'fao_data_fertilizers_data.csv', 'fao_data_forest_data.csv', 'fao_data_land_data.csv', 'fao_data_production_indices_data.csv', 'LICENSE.md', 'nutrients.json', 'original', 'README.md', 'README.txt', 'test', 'train_validate', 'us-usda-gov-3d6e899c-ce46-4998-ab3f-ad228d7f3888', 'words.txt', 'words_alpha.txt', 'words_dictionary.json']
    


```python
    # Step 5: Download a specific table to work with
    # Specify the CSV file to read from the ZIP archive
    csv_file_to_read = "current_FAO/raw_files/Trade_LiveAnimals_E_All_Data_(Normalized).csv"

    # Read the ZIP archive
    with ZipFile("global-food-agriculture-statistics.zip", 'r') as zip_file:
        # List the files within the ZIP archive (to double-check paths)
        print(zip_file.namelist())

        # Read the CSV file from the ZIP archive with the specified encoding and delimiter
        with zip_file.open(csv_file_to_read) as csv_file:
            df = pd.read_csv(csv_file, encoding='ISO-8859-1')
```

    ['current_FAO/__MACOSX/raw_files/._ASTI_Research_Spending_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._ASTI_Researchers_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._CommodityBalances_Crops_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._CommodityBalances_LivestockFish_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._ConsumerPriceIndices_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Deflators_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Agriculture_Agriculture_total_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Agriculture_Burning_Savanna_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Agriculture_Burning_crop_residues_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Agriculture_Crop_Residues_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Agriculture_Cultivated_Organic_Soils_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Agriculture_Energy_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Agriculture_Enteric_Fermentation_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Agriculture_Manure_Management_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Agriculture_Manure_applied_to_soils_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Agriculture_Manure_left_on_pasture_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Agriculture_Rice_Cultivation_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Agriculture_Synthetic_Fertilizers_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Land_Use_Burning_Biomass_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Land_Use_Cropland_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Land_Use_Forest_Land_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Land_Use_Grassland_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Emissions_Land_Use_Land_Use_Total_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Employment_Indicators_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Environment_AirClimateChange_E_All_Data.csv', 'current_FAO/__MACOSX/raw_files/._Environment_Emissions_by_Sector_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Environment_Emissions_intensities_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Environment_Energy_E_All_Data.csv', 'current_FAO/__MACOSX/raw_files/._Environment_Fertilizers_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Environment_LandCover_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Environment_LandUse_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Environment_LivestockPatterns_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Environment_Livestock_E_All_Data.csv', 'current_FAO/__MACOSX/raw_files/._Environment_Pesticides_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Environment_Soil_E_All_Data.csv', 'current_FAO/__MACOSX/raw_files/._Environment_Temperature_change_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Environment_Water_E_All_Data.csv', 'current_FAO/__MACOSX/raw_files/._Exchange_rate_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._FoodSupply_Crops_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._FoodSupply_LivestockFish_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Food_Aid_Shipments_WFP_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Food_Security_Data_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Forestry_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Forestry_Trade_Flows_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Indicators_from_Household_Surveys_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Inputs_FertilizersTradeValues_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Inputs_Fertilizers_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Inputs_Land_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Inputs_Pesticides_Trade_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Inputs_Pesticides_Use_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Investment_CapitalStock_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Investment_CountryInvestmentStatisticsProfile__E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Investment_CreditAgriculture_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Investment_ForeignDirectInvestment_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Investment_GovernmentExpenditure_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Investment_MachineryArchive_E_All_Data.csv', 'current_FAO/__MACOSX/raw_files/._Investment_Machinery_E_All_Data.csv', 'current_FAO/__MACOSX/raw_files/._Macro-Statistics_Key_Indicators_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Population_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Population_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Price_Indices_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._PricesArchive_E_All_Data.csv', 'current_FAO/__MACOSX/raw_files/._Prices_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Prices_Monthly_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Production_CropsProcessed_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Production_Crops_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Production_Indices_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Production_LivestockPrimary_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Production_LivestockProcessed_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Production_Livestock_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Resources_FertilizersArchive_E_All_Data.csv', 'current_FAO/__MACOSX/raw_files/._Trade_Crops_Livestock_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Trade_Indices_E_All_Data_(Norm).csv', 'current_FAO/__MACOSX/raw_files/._Trade_LiveAnimals_E_All_Data_(Normalized).csv', 'current_FAO/__MACOSX/raw_files/._Value_of_Production_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/ASTI_Research_Spending_E_All_Data_(Norm).csv', 'current_FAO/raw_files/ASTI_Researchers_E_All_Data_(Norm).csv', 'current_FAO/raw_files/CommodityBalances_Crops_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/CommodityBalances_LivestockFish_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/ConsumerPriceIndices_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Deflators_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Emissions_Agriculture_Agriculture_total_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Agriculture_Burning_Savanna_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Agriculture_Burning_crop_residues_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Agriculture_Crop_Residues_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Agriculture_Cultivated_Organic_Soils_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Agriculture_Energy_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Agriculture_Enteric_Fermentation_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Agriculture_Manure_Management_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Agriculture_Manure_applied_to_soils_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Agriculture_Manure_left_on_pasture_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Agriculture_Rice_Cultivation_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Agriculture_Synthetic_Fertilizers_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Land_Use_Burning_Biomass_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Land_Use_Cropland_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Land_Use_Forest_Land_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Land_Use_Grassland_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Emissions_Land_Use_Land_Use_Total_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Employment_Indicators_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Environment_AirClimateChange_E_All_Data.csv', 'current_FAO/raw_files/Environment_Emissions_by_Sector_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Environment_Emissions_intensities_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Environment_Energy_E_All_Data.csv', 'current_FAO/raw_files/Environment_Fertilizers_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Environment_LandCover_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Environment_LandUse_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Environment_LivestockPatterns_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Environment_Livestock_E_All_Data.csv', 'current_FAO/raw_files/Environment_Pesticides_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Environment_Soil_E_All_Data.csv', 'current_FAO/raw_files/Environment_Temperature_change_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Environment_Water_E_All_Data.csv', 'current_FAO/raw_files/Exchange_rate_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/FoodSupply_Crops_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/FoodSupply_LivestockFish_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Food_Aid_Shipments_WFP_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Food_Security_Data_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Forestry_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Forestry_Trade_Flows_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Indicators_from_Household_Surveys_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Inputs_FertilizersTradeValues_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Inputs_Fertilizers_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Inputs_Land_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Inputs_Pesticides_Trade_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Inputs_Pesticides_Use_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Investment_CapitalStock_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Investment_CountryInvestmentStatisticsProfile__E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Investment_CreditAgriculture_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Investment_ForeignDirectInvestment_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Investment_GovernmentExpenditure_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Investment_MachineryArchive_E_All_Data.csv', 'current_FAO/raw_files/Investment_Machinery_E_All_Data.csv', 'current_FAO/raw_files/Macro-Statistics_Key_Indicators_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Population_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Population_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Price_Indices_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/PricesArchive_E_All_Data.csv', 'current_FAO/raw_files/Prices_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Prices_Monthly_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Production_CropsProcessed_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Production_Crops_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Production_Indices_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Production_LivestockPrimary_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Production_LivestockProcessed_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Production_Livestock_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Resources_FertilizersArchive_E_All_Data.csv', 'current_FAO/raw_files/Trade_Crops_Livestock_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Trade_Indices_E_All_Data_(Norm).csv', 'current_FAO/raw_files/Trade_LiveAnimals_E_All_Data_(Normalized).csv', 'current_FAO/raw_files/Value_of_Production_E_All_Data_(Normalized).csv', 'fao_data_crops_data.csv', 'fao_data_fertilizers_data.csv', 'fao_data_forest_data.csv', 'fao_data_land_data.csv', 'fao_data_production_indices_data.csv']
    


```python
# Print the first few rows of the dataset
df.head()
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
      <th>Area Code</th>
      <th>Area</th>
      <th>Item Code</th>
      <th>Item</th>
      <th>Element Code</th>
      <th>Element</th>
      <th>Year Code</th>
      <th>Year</th>
      <th>Unit</th>
      <th>Value</th>
      <th>Flag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1961</td>
      <td>1961</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1962</td>
      <td>1962</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1963</td>
      <td>1963</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1964</td>
      <td>1964</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1965</td>
      <td>1965</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
  </tbody>
</table>
</div>




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
      <th>Area Code</th>
      <th>Area</th>
      <th>Item Code</th>
      <th>Item</th>
      <th>Element Code</th>
      <th>Element</th>
      <th>Year Code</th>
      <th>Year</th>
      <th>Unit</th>
      <th>Value</th>
      <th>Flag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>662953</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2009</td>
      <td>2009</td>
      <td>1000 US$</td>
      <td>456293.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662954</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2010</td>
      <td>2010</td>
      <td>1000 US$</td>
      <td>421311.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662955</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2011</td>
      <td>2011</td>
      <td>1000 US$</td>
      <td>649321.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662956</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2012</td>
      <td>2012</td>
      <td>1000 US$</td>
      <td>778317.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662957</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2013</td>
      <td>2013</td>
      <td>1000 US$</td>
      <td>1038636.0</td>
      <td>A</td>
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
      <th>Area Code</th>
      <th>Area</th>
      <th>Item Code</th>
      <th>Item</th>
      <th>Element Code</th>
      <th>Element</th>
      <th>Year Code</th>
      <th>Year</th>
      <th>Unit</th>
      <th>Value</th>
      <th>Flag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1961</td>
      <td>1961</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1962</td>
      <td>1962</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1963</td>
      <td>1963</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1964</td>
      <td>1964</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1965</td>
      <td>1965</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
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
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>662953</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2009</td>
      <td>2009</td>
      <td>1000 US$</td>
      <td>456293.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662954</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2010</td>
      <td>2010</td>
      <td>1000 US$</td>
      <td>421311.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662955</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2011</td>
      <td>2011</td>
      <td>1000 US$</td>
      <td>649321.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662956</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2012</td>
      <td>2012</td>
      <td>1000 US$</td>
      <td>778317.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662957</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2013</td>
      <td>2013</td>
      <td>1000 US$</td>
      <td>1038636.0</td>
      <td>A</td>
    </tr>
  </tbody>
</table>
<p>662958 rows × 11 columns</p>
</div>




```python
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
      <th>Area Code</th>
      <th>Area</th>
      <th>Item Code</th>
      <th>Item</th>
      <th>Element Code</th>
      <th>Element</th>
      <th>Year Code</th>
      <th>Year</th>
      <th>Unit</th>
      <th>Value</th>
      <th>Flag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>662953</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2009</td>
      <td>2009</td>
      <td>1000 US$</td>
      <td>456293.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662954</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2010</td>
      <td>2010</td>
      <td>1000 US$</td>
      <td>421311.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662955</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2011</td>
      <td>2011</td>
      <td>1000 US$</td>
      <td>649321.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662956</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2012</td>
      <td>2012</td>
      <td>1000 US$</td>
      <td>778317.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662957</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2013</td>
      <td>2013</td>
      <td>1000 US$</td>
      <td>1038636.0</td>
      <td>A</td>
    </tr>
  </tbody>
</table>
</div>




# Perform at least 5 data transformation and/or cleansing steps to your API data. 



```python
# Step 1: Replace Headers
new_headers = ["area_code","area", "item_code", "item", "element_code",	"element", "year_code", "year", "unit", "value", "flag"]
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
      <th>area_code</th>
      <th>area</th>
      <th>item_code</th>
      <th>item</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1961</td>
      <td>1961</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1962</td>
      <td>1962</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1963</td>
      <td>1963</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1964</td>
      <td>1964</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1965</td>
      <td>1965</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
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
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>662953</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2009</td>
      <td>2009</td>
      <td>1000 US$</td>
      <td>456293.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662954</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2010</td>
      <td>2010</td>
      <td>1000 US$</td>
      <td>421311.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662955</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2011</td>
      <td>2011</td>
      <td>1000 US$</td>
      <td>649321.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662956</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2012</td>
      <td>2012</td>
      <td>1000 US$</td>
      <td>778317.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662957</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2013</td>
      <td>2013</td>
      <td>1000 US$</td>
      <td>1038636.0</td>
      <td>A</td>
    </tr>
  </tbody>
</table>
<p>662958 rows × 11 columns</p>
</div>




```python
# renaming 'area' and 'item' columns

# Renaming columns 'area' to 'country' and 'item' to 'animal_category'
df2 = df2.rename(columns={'area': 'country', 'item': 'animal_category'})

df2.head()

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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1961</td>
      <td>1961</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1962</td>
      <td>1962</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1963</td>
      <td>1963</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1964</td>
      <td>1964</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1965</td>
      <td>1965</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>662953</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2009</td>
      <td>2009</td>
      <td>1000 US$</td>
      <td>456293.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662954</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2010</td>
      <td>2010</td>
      <td>1000 US$</td>
      <td>421311.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662955</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2011</td>
      <td>2011</td>
      <td>1000 US$</td>
      <td>649321.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662956</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2012</td>
      <td>2012</td>
      <td>1000 US$</td>
      <td>778317.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>662957</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2013</td>
      <td>2013</td>
      <td>1000 US$</td>
      <td>1038636.0</td>
      <td>A</td>
    </tr>
  </tbody>
</table>
</div>




```python
# data types
print(df2.dtypes)

```

    area_code            int64
    country             object
    item_code            int64
    animal_category     object
    element_code         int64
    element             object
    year_code            int64
    year                 int64
    unit                object
    value              float64
    flag                object
    dtype: object
    


```python
# Step 2: Handling Missing Values
missing_values = df2.isnull().sum()
print("Missing values:\n", missing_values)
```

    Missing values:
     area_code               0
    country                 0
    item_code               0
    animal_category         0
    element_code            0
    element                 0
    year_code               0
    year                    0
    unit                    0
    value              135190
    flag               203064
    dtype: int64
    


```python
# Step 3:Data Transformation: creating new variables using the 'gdp' variable

import pandas as pd  # Importing the pandas library and aliasing it as 'pd'
import numpy as np  # Importing the numpy library and aliasing it as 'np'

# Step 3: Data Transformation: creating new variables using the 'value' variable

# Convert 'value' column to numeric
df2['value'] = pd.to_numeric(df2['value'], errors='coerce')

# Create new variables
df2['value_squared'] = df2['value'] ** 2  # Creating a new column 'value_squared' which contains the square of the 'value' column
df2['value_square_root'] = np.sqrt(df2['value'])  # Creating a new column 'value_square_root' which contains the square root of the 'value' column
df2['value_log'] = np.log(df2['value'])  # Creating a new column 'value_log' which contains the natural logarithm of the 'value' column
df2['value_zscore'] = (df2['value'] - df2['value'].mean()) / df2['value'].std()  # Creating a new column 'value_zscore' which contains the Z-score standardized version of the 'value' column

# Min-max normalization
min_value = df2['value'].min()  # Finding the minimum value of the 'value' column
max_value = df2['value'].max()  # Finding the maximum value of the 'value' column
df2['value_normalized'] = (df2['value'] - min_value) / (max_value - min_value)  # Creating a new column 'value_normalized' which contains the min-max normalized version of the 'value' column

#print(df2[['country', 'animal_category', 'year', 'value', 'value_squared', 'value_square_root', 'value_log', 'value_zscore', 'value_normalized']])  # Printing the DataFrame with selected columns

df2[['country', 'animal_category', 'element', 'year', 'value', 'value_squared', 'value_square_root', 'value_log', 'value_zscore', 'value_normalized']]  # Printing the DataFrame with selected columns

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
      <th>animal_category</th>
      <th>element</th>
      <th>year</th>
      <th>value</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>Cattle</td>
      <td>Import Quantity</td>
      <td>1961</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Afghanistan</td>
      <td>Cattle</td>
      <td>Import Quantity</td>
      <td>1962</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Afghanistan</td>
      <td>Cattle</td>
      <td>Import Quantity</td>
      <td>1963</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Afghanistan</td>
      <td>Cattle</td>
      <td>Import Quantity</td>
      <td>1964</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Afghanistan</td>
      <td>Cattle</td>
      <td>Import Quantity</td>
      <td>1965</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>662953</th>
      <td>Net Food Importing Developing Countries</td>
      <td>Sheep and Goats</td>
      <td>Export Value</td>
      <td>2009</td>
      <td>456293.0</td>
      <td>2.082033e+11</td>
      <td>675.494634</td>
      <td>13.030890</td>
      <td>-0.035645</td>
      <td>0.000024</td>
    </tr>
    <tr>
      <th>662954</th>
      <td>Net Food Importing Developing Countries</td>
      <td>Sheep and Goats</td>
      <td>Export Value</td>
      <td>2010</td>
      <td>421311.0</td>
      <td>1.775030e+11</td>
      <td>649.084740</td>
      <td>12.951127</td>
      <td>-0.035913</td>
      <td>0.000022</td>
    </tr>
    <tr>
      <th>662955</th>
      <td>Net Food Importing Developing Countries</td>
      <td>Sheep and Goats</td>
      <td>Export Value</td>
      <td>2011</td>
      <td>649321.0</td>
      <td>4.216178e+11</td>
      <td>805.804567</td>
      <td>13.383682</td>
      <td>-0.034167</td>
      <td>0.000035</td>
    </tr>
    <tr>
      <th>662956</th>
      <td>Net Food Importing Developing Countries</td>
      <td>Sheep and Goats</td>
      <td>Export Value</td>
      <td>2012</td>
      <td>778317.0</td>
      <td>6.057774e+11</td>
      <td>882.222761</td>
      <td>13.564889</td>
      <td>-0.033180</td>
      <td>0.000041</td>
    </tr>
    <tr>
      <th>662957</th>
      <td>Net Food Importing Developing Countries</td>
      <td>Sheep and Goats</td>
      <td>Export Value</td>
      <td>2013</td>
      <td>1038636.0</td>
      <td>1.078765e+12</td>
      <td>1019.134927</td>
      <td>13.853419</td>
      <td>-0.031187</td>
      <td>0.000055</td>
    </tr>
  </tbody>
</table>
<p>662958 rows × 10 columns</p>
</div>




```python
import pandas as pd

# Convert 'value' and its derived new variables to numeric using the given formula
df2['value'] = pd.to_numeric(df2['value'], errors='coerce')
df2['value_squared'] = pd.to_numeric(df2['value_squared'], errors='coerce')
df2['value_square_root'] = pd.to_numeric(df2['value_square_root'], errors='coerce')
df2['value_log'] = pd.to_numeric(df2['value_log'], errors='coerce')
df2['value_zscore'] = pd.to_numeric(df2['value_zscore'], errors='coerce')
df2['value_normalized'] = pd.to_numeric(df2['value_normalized'], errors='coerce')
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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1961</td>
      <td>1961</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1962</td>
      <td>1962</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1963</td>
      <td>1963</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1964</td>
      <td>1964</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>1965</td>
      <td>1965</td>
      <td>Head</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
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
      <th>662953</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2009</td>
      <td>2009</td>
      <td>1000 US$</td>
      <td>456293.0</td>
      <td>A</td>
      <td>2.082033e+11</td>
      <td>675.494634</td>
      <td>13.030890</td>
      <td>-0.035645</td>
      <td>0.000024</td>
    </tr>
    <tr>
      <th>662954</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2010</td>
      <td>2010</td>
      <td>1000 US$</td>
      <td>421311.0</td>
      <td>A</td>
      <td>1.775030e+11</td>
      <td>649.084740</td>
      <td>12.951127</td>
      <td>-0.035913</td>
      <td>0.000022</td>
    </tr>
    <tr>
      <th>662955</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2011</td>
      <td>2011</td>
      <td>1000 US$</td>
      <td>649321.0</td>
      <td>A</td>
      <td>4.216178e+11</td>
      <td>805.804567</td>
      <td>13.383682</td>
      <td>-0.034167</td>
      <td>0.000035</td>
    </tr>
    <tr>
      <th>662956</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2012</td>
      <td>2012</td>
      <td>1000 US$</td>
      <td>778317.0</td>
      <td>A</td>
      <td>6.057774e+11</td>
      <td>882.222761</td>
      <td>13.564889</td>
      <td>-0.033180</td>
      <td>0.000041</td>
    </tr>
    <tr>
      <th>662957</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2013</td>
      <td>2013</td>
      <td>1000 US$</td>
      <td>1038636.0</td>
      <td>A</td>
      <td>1.078765e+12</td>
      <td>1019.134927</td>
      <td>13.853419</td>
      <td>-0.031187</td>
      <td>0.000055</td>
    </tr>
  </tbody>
</table>
<p>662958 rows × 16 columns</p>
</div>




```python
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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>662953</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2009</td>
      <td>2009</td>
      <td>1000 US$</td>
      <td>456293.0</td>
      <td>A</td>
      <td>2.082033e+11</td>
      <td>675.494634</td>
      <td>13.030890</td>
      <td>-0.035645</td>
      <td>0.000024</td>
    </tr>
    <tr>
      <th>662954</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2010</td>
      <td>2010</td>
      <td>1000 US$</td>
      <td>421311.0</td>
      <td>A</td>
      <td>1.775030e+11</td>
      <td>649.084740</td>
      <td>12.951127</td>
      <td>-0.035913</td>
      <td>0.000022</td>
    </tr>
    <tr>
      <th>662955</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2011</td>
      <td>2011</td>
      <td>1000 US$</td>
      <td>649321.0</td>
      <td>A</td>
      <td>4.216178e+11</td>
      <td>805.804567</td>
      <td>13.383682</td>
      <td>-0.034167</td>
      <td>0.000035</td>
    </tr>
    <tr>
      <th>662956</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2012</td>
      <td>2012</td>
      <td>1000 US$</td>
      <td>778317.0</td>
      <td>A</td>
      <td>6.057774e+11</td>
      <td>882.222761</td>
      <td>13.564889</td>
      <td>-0.033180</td>
      <td>0.000041</td>
    </tr>
    <tr>
      <th>662957</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2013</td>
      <td>2013</td>
      <td>1000 US$</td>
      <td>1038636.0</td>
      <td>A</td>
      <td>1.078765e+12</td>
      <td>1019.134927</td>
      <td>13.853419</td>
      <td>-0.031187</td>
      <td>0.000055</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


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
df2

```

    DataFrame after removing NaN and None values:
    




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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>2000</td>
      <td>2000</td>
      <td>Head</td>
      <td>2600.0</td>
      <td>R</td>
      <td>6.760000e+06</td>
      <td>50.990195</td>
      <td>7.863267</td>
      <td>-0.039119</td>
      <td>1.381600e-07</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>2001</td>
      <td>2001</td>
      <td>Head</td>
      <td>3600.0</td>
      <td>R</td>
      <td>1.296000e+07</td>
      <td>60.000000</td>
      <td>8.188689</td>
      <td>-0.039111</td>
      <td>1.912985e-07</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>2002</td>
      <td>2002</td>
      <td>Head</td>
      <td>850.0</td>
      <td>R</td>
      <td>7.225000e+05</td>
      <td>29.154759</td>
      <td>6.745236</td>
      <td>-0.039132</td>
      <td>4.516770e-08</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>2003</td>
      <td>2003</td>
      <td>Head</td>
      <td>25376.0</td>
      <td>R</td>
      <td>6.439414e+08</td>
      <td>159.298462</td>
      <td>10.141559</td>
      <td>-0.038945</td>
      <td>1.348442e-06</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>2004</td>
      <td>2004</td>
      <td>Head</td>
      <td>2791.0</td>
      <td>R</td>
      <td>7.789681e+06</td>
      <td>52.829916</td>
      <td>7.934155</td>
      <td>-0.039118</td>
      <td>1.483095e-07</td>
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
      <th>324699</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2009</td>
      <td>2009</td>
      <td>1000 US$</td>
      <td>456293.0</td>
      <td>A</td>
      <td>2.082033e+11</td>
      <td>675.494634</td>
      <td>13.030890</td>
      <td>-0.035645</td>
      <td>2.424671e-05</td>
    </tr>
    <tr>
      <th>324700</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2010</td>
      <td>2010</td>
      <td>1000 US$</td>
      <td>421311.0</td>
      <td>A</td>
      <td>1.775030e+11</td>
      <td>649.084740</td>
      <td>12.951127</td>
      <td>-0.035913</td>
      <td>2.238782e-05</td>
    </tr>
    <tr>
      <th>324701</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2011</td>
      <td>2011</td>
      <td>1000 US$</td>
      <td>649321.0</td>
      <td>A</td>
      <td>4.216178e+11</td>
      <td>805.804567</td>
      <td>13.383682</td>
      <td>-0.034167</td>
      <td>3.450392e-05</td>
    </tr>
    <tr>
      <th>324702</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2012</td>
      <td>2012</td>
      <td>1000 US$</td>
      <td>778317.0</td>
      <td>A</td>
      <td>6.057774e+11</td>
      <td>882.222761</td>
      <td>13.564889</td>
      <td>-0.033180</td>
      <td>4.135857e-05</td>
    </tr>
    <tr>
      <th>324703</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2013</td>
      <td>2013</td>
      <td>1000 US$</td>
      <td>1038636.0</td>
      <td>A</td>
      <td>1.078765e+12</td>
      <td>1019.134927</td>
      <td>13.853419</td>
      <td>-0.031187</td>
      <td>5.519152e-05</td>
    </tr>
  </tbody>
</table>
<p>324704 rows × 16 columns</p>
</div>




```python
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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>324699</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2009</td>
      <td>2009</td>
      <td>1000 US$</td>
      <td>456293.0</td>
      <td>A</td>
      <td>2.082033e+11</td>
      <td>675.494634</td>
      <td>13.030890</td>
      <td>-0.035645</td>
      <td>0.000024</td>
    </tr>
    <tr>
      <th>324700</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2010</td>
      <td>2010</td>
      <td>1000 US$</td>
      <td>421311.0</td>
      <td>A</td>
      <td>1.775030e+11</td>
      <td>649.084740</td>
      <td>12.951127</td>
      <td>-0.035913</td>
      <td>0.000022</td>
    </tr>
    <tr>
      <th>324701</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2011</td>
      <td>2011</td>
      <td>1000 US$</td>
      <td>649321.0</td>
      <td>A</td>
      <td>4.216178e+11</td>
      <td>805.804567</td>
      <td>13.383682</td>
      <td>-0.034167</td>
      <td>0.000035</td>
    </tr>
    <tr>
      <th>324702</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2012</td>
      <td>2012</td>
      <td>1000 US$</td>
      <td>778317.0</td>
      <td>A</td>
      <td>6.057774e+11</td>
      <td>882.222761</td>
      <td>13.564889</td>
      <td>-0.033180</td>
      <td>0.000041</td>
    </tr>
    <tr>
      <th>324703</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2013</td>
      <td>2013</td>
      <td>1000 US$</td>
      <td>1038636.0</td>
      <td>A</td>
      <td>1.078765e+12</td>
      <td>1019.134927</td>
      <td>13.853419</td>
      <td>-0.031187</td>
      <td>0.000055</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
# Step 5: Format Data

# Format 'value' columns into a readable format (e.g., adding commas for thousands separator)
df2['value'] = df2['value'].apply(lambda x: '{:,.2f}'.format(x) if isinstance(x, (float, int)) and pd.notnull(x) else None)
df2['value_squared'] = df2['value_squared'].apply(lambda x: '{:,.2f}'.format(x) if isinstance(x, (float, int)) and pd.notnull(x) else None)
df2['value_square_root'] = df2['value_square_root'].apply(lambda x: '{:,.2f}'.format(x) if isinstance(x, (float, int)) and pd.notnull(x) else None)
df2['value_log'] = df2['value_log'].apply(lambda x: '{:,.2f}'.format(x) if isinstance(x, (float, int)) and pd.notnull(x) else None)
df2['value_zscore'] = df2['value_zscore'].apply(lambda x: '{:,.2f}'.format(x) if isinstance(x, (float, int)) and pd.notnull(x) else None)
df2['value_normalized'] = df2['value_normalized'].apply(lambda x: '{:,.2f}'.format(x) if isinstance(x, (float, int)) and pd.notnull(x) else None)

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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>2000</td>
      <td>2000</td>
      <td>Head</td>
      <td>2,600.00</td>
      <td>R</td>
      <td>6,760,000.00</td>
      <td>50.99</td>
      <td>7.86</td>
      <td>-0.04</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>2001</td>
      <td>2001</td>
      <td>Head</td>
      <td>3,600.00</td>
      <td>R</td>
      <td>12,960,000.00</td>
      <td>60.00</td>
      <td>8.19</td>
      <td>-0.04</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>2002</td>
      <td>2002</td>
      <td>Head</td>
      <td>850.00</td>
      <td>R</td>
      <td>722,500.00</td>
      <td>29.15</td>
      <td>6.75</td>
      <td>-0.04</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>2003</td>
      <td>2003</td>
      <td>Head</td>
      <td>25,376.00</td>
      <td>R</td>
      <td>643,941,376.00</td>
      <td>159.30</td>
      <td>10.14</td>
      <td>-0.04</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5608</td>
      <td>Import Quantity</td>
      <td>2004</td>
      <td>2004</td>
      <td>Head</td>
      <td>2,791.00</td>
      <td>R</td>
      <td>7,789,681.00</td>
      <td>52.83</td>
      <td>7.93</td>
      <td>-0.04</td>
      <td>0.00</td>
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
      <th>324699</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2009</td>
      <td>2009</td>
      <td>1000 US$</td>
      <td>456,293.00</td>
      <td>A</td>
      <td>208,203,301,849.00</td>
      <td>675.49</td>
      <td>13.03</td>
      <td>-0.04</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>324700</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2010</td>
      <td>2010</td>
      <td>1000 US$</td>
      <td>421,311.00</td>
      <td>A</td>
      <td>177,502,958,721.00</td>
      <td>649.08</td>
      <td>12.95</td>
      <td>-0.04</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>324701</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2011</td>
      <td>2011</td>
      <td>1000 US$</td>
      <td>649,321.00</td>
      <td>A</td>
      <td>421,617,761,041.00</td>
      <td>805.80</td>
      <td>13.38</td>
      <td>-0.03</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>324702</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2012</td>
      <td>2012</td>
      <td>1000 US$</td>
      <td>778,317.00</td>
      <td>A</td>
      <td>605,777,352,489.00</td>
      <td>882.22</td>
      <td>13.56</td>
      <td>-0.03</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>324703</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2013</td>
      <td>2013</td>
      <td>1000 US$</td>
      <td>1,038,636.00</td>
      <td>A</td>
      <td>1,078,764,740,496.00</td>
      <td>1,019.13</td>
      <td>13.85</td>
      <td>-0.03</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>324704 rows × 16 columns</p>
</div>




```python
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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>324699</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2009</td>
      <td>2009</td>
      <td>1000 US$</td>
      <td>456,293.00</td>
      <td>A</td>
      <td>208,203,301,849.00</td>
      <td>675.49</td>
      <td>13.03</td>
      <td>-0.04</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>324700</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2010</td>
      <td>2010</td>
      <td>1000 US$</td>
      <td>421,311.00</td>
      <td>A</td>
      <td>177,502,958,721.00</td>
      <td>649.08</td>
      <td>12.95</td>
      <td>-0.04</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>324701</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2011</td>
      <td>2011</td>
      <td>1000 US$</td>
      <td>649,321.00</td>
      <td>A</td>
      <td>421,617,761,041.00</td>
      <td>805.80</td>
      <td>13.38</td>
      <td>-0.03</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>324702</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2012</td>
      <td>2012</td>
      <td>1000 US$</td>
      <td>778,317.00</td>
      <td>A</td>
      <td>605,777,352,489.00</td>
      <td>882.22</td>
      <td>13.56</td>
      <td>-0.03</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>324703</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1922</td>
      <td>Sheep and Goats</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>2013</td>
      <td>2013</td>
      <td>1000 US$</td>
      <td>1,038,636.00</td>
      <td>A</td>
      <td>1,078,764,740,496.00</td>
      <td>1,019.13</td>
      <td>13.85</td>
      <td>-0.03</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Outlier detection

import pandas as pd

# Step 7: Converting each variable to numeric

# Convert 'value' and its derived new variables to numeric using the given formula
df2['value'] = pd.to_numeric(df2['value'].str.replace(',', ''), errors='coerce')
df2['value_squared'] = pd.to_numeric(df2['value_squared'].str.replace(',', ''), errors='coerce')
df2['value_square_root'] = pd.to_numeric(df2['value_square_root'], errors='coerce')
df2['value_log'] = pd.to_numeric(df2['value_log'], errors='coerce')
df2['value_zscore'] = pd.to_numeric(df2['value_zscore'], errors='coerce')
df2['value_normalized'] = pd.to_numeric(df2['value_normalized'], errors='coerce')

# Calculate z-score for the 'value' column
z_scores_value = ((df2['value'] - df2['value'].mean()) / df2['value'].std()).abs()
outliers_value = z_scores_value > 3

# Calculate z-score for the 'value_squared' column
z_scores_value_squared = ((df2['value_squared'] - df2['value_squared'].mean()) / df2['value_squared'].std()).abs()
outliers_value_squared = z_scores_value_squared > 3

# Print outliers for each variable
print("Outliers for 'value':")
print(outliers_value)

print("Outliers for 'value_squared':")
print(outliers_value_squared)

```

    Outliers for 'value':
    0          True
    1         False
    2         False
    3         False
    4         False
              ...  
    111851    False
    111852    False
    111853    False
    111854    False
    111855    False
    Name: value, Length: 111856, dtype: bool
    Outliers for 'value_squared':
    0          True
    1         False
    2         False
    3         False
    4         False
              ...  
    111851    False
    111852    False
    111853    False
    111854    False
    111855    False
    Name: value_squared, Length: 111856, dtype: bool
    


```python

```


```python
# Step 8: Fix Inconsistent Values: convert all strings to lowercase to address inconsistent capitalization

df2['country'] = df2['country'].str.lower()

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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5622</td>
      <td>Import Value</td>
      <td>2005</td>
      <td>2005</td>
      <td>1000 US$</td>
      <td>28.0</td>
      <td>R</td>
      <td>784.0</td>
      <td>5.29</td>
      <td>3.33</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1997</td>
      <td>1997</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1998</td>
      <td>1998</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1999</td>
      <td>1999</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>2000</td>
      <td>2000</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
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
      <th>111851</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1986</td>
      <td>1986</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111852</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1987</td>
      <td>1987</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111853</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1988</td>
      <td>1988</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111854</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1989</td>
      <td>1989</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111855</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1992</td>
      <td>1992</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>111856 rows × 16 columns</p>
</div>




```python
# Step 9: Replace Inconsistent Values with Standardized Ones
# For example, replacing 'united states' with 'United States of America'
df2['country'].replace({'united states': 'United States of America'}, inplace=True)

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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5622</td>
      <td>Import Value</td>
      <td>2005</td>
      <td>2005</td>
      <td>1000 US$</td>
      <td>28.0</td>
      <td>R</td>
      <td>784.0</td>
      <td>5.29</td>
      <td>3.33</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1997</td>
      <td>1997</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1998</td>
      <td>1998</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1999</td>
      <td>1999</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>2000</td>
      <td>2000</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
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
      <th>111851</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1986</td>
      <td>1986</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111852</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1987</td>
      <td>1987</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111853</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1988</td>
      <td>1988</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111854</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1989</td>
      <td>1989</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111855</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1992</td>
      <td>1992</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>111856 rows × 16 columns</p>
</div>




```python
# Step 9: Replace Inconsistent Values with Standardized Ones
# For example, replacing 'united states' with 'United States of America'
df2['country'].replace({'afghanistan': 'Afghanistan'}, inplace=True)

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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5622</td>
      <td>Import Value</td>
      <td>2005</td>
      <td>2005</td>
      <td>1000 US$</td>
      <td>28.0</td>
      <td>R</td>
      <td>784.0</td>
      <td>5.29</td>
      <td>3.33</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1997</td>
      <td>1997</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1998</td>
      <td>1998</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1999</td>
      <td>1999</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>2000</td>
      <td>2000</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
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
      <th>111851</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1986</td>
      <td>1986</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111852</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1987</td>
      <td>1987</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111853</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1988</td>
      <td>1988</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111854</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1989</td>
      <td>1989</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111855</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1992</td>
      <td>1992</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>111856 rows × 16 columns</p>
</div>




```python
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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>111851</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1986</td>
      <td>1986</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111852</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1987</td>
      <td>1987</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111853</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1988</td>
      <td>1988</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111854</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1989</td>
      <td>1989</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111855</th>
      <td>5817</td>
      <td>net food importing developing countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1992</td>
      <td>1992</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




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
df2.head()

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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5622</td>
      <td>Import Value</td>
      <td>2005</td>
      <td>2005</td>
      <td>1000 US$</td>
      <td>28.0</td>
      <td>R</td>
      <td>784.0</td>
      <td>5.29</td>
      <td>3.33</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1997</td>
      <td>1997</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1998</td>
      <td>1998</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1999</td>
      <td>1999</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>2000</td>
      <td>2000</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>111851</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1986</td>
      <td>1986</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111852</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1987</td>
      <td>1987</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111853</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1988</td>
      <td>1988</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111854</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1989</td>
      <td>1989</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111855</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1992</td>
      <td>1992</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




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
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    United States of America (Similarity: 100%)
    Fuzzy matches for 'France':
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    France (Similarity: 100%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Ukraine (Similarity: 73%)
    Fuzzy matches for 'Germany':
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Germany (Similarity: 100%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Oman (Similarity: 75%)
    Fuzzy matches for 'United Kingdom':
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    United Kingdom (Similarity: 100%)
    Fuzzy matches for 'Japan':
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
    Japan (Similarity: 100%)
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
      <th>area_code</th>
      <th>country</th>
      <th>item_code</th>
      <th>animal_category</th>
      <th>element_code</th>
      <th>element</th>
      <th>year_code</th>
      <th>year</th>
      <th>unit</th>
      <th>value</th>
      <th>flag</th>
      <th>value_squared</th>
      <th>value_square_root</th>
      <th>value_log</th>
      <th>value_zscore</th>
      <th>value_normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>866</td>
      <td>Cattle</td>
      <td>5622</td>
      <td>Import Value</td>
      <td>2005</td>
      <td>2005</td>
      <td>1000 US$</td>
      <td>28.0</td>
      <td>R</td>
      <td>784.0</td>
      <td>5.29</td>
      <td>3.33</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1997</td>
      <td>1997</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1998</td>
      <td>1998</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>1999</td>
      <td>1999</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Afghanistan</td>
      <td>1057</td>
      <td>Chickens</td>
      <td>5609</td>
      <td>Import Quantity</td>
      <td>2000</td>
      <td>2000</td>
      <td>1000 Head</td>
      <td>0.0</td>
      <td>F</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
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
      <th>111851</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1986</td>
      <td>1986</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111852</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1987</td>
      <td>1987</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111853</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1988</td>
      <td>1988</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111854</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1989</td>
      <td>1989</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>111855</th>
      <td>5817</td>
      <td>Net Food Importing Developing Countries</td>
      <td>1079</td>
      <td>Turkeys</td>
      <td>5922</td>
      <td>Export Value</td>
      <td>1992</td>
      <td>1992</td>
      <td>1000 US$</td>
      <td>0.0</td>
      <td>A</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>-inf</td>
      <td>-0.04</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>111856 rows × 16 columns</p>
</div>




```python

```


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
    


```python

```

# 1 paragraph of the ethical implications of data wrangling specific to the datasource 


Ethical Implications of Data Wrangling for the FAOSTAT Live Animals Dataset:

In the process of data wrangling the FAOSTAT Live Animals dataset, ethical implications arise concerning data privacy, integrity, and transparency. Given the extensive historical data spanning over 50 years and covering over 200 countries, it is crucial to ensure that the data remains anonymized and that no sensitive information about individuals or specific entities is exposed. The integrity of the data must be maintained by accurately handling outliers and inconsistencies without introducing biases or errors that could misrepresent trends or patterns. Transparency in the data wrangling process is also essential, as stakeholders must be able to trust the methods used to clean and format the data. Clear documentation of the transformations and decisions made during data wrangling ensures that the dataset can be reliably used for further analysis and that the findings derived from it are credible and ethically sound.


```python

```

# Responses to the questions based on Milestone 4 project activities:

What changes were made to the data?

Various data transformation and cleansing steps were applied to the FAOSTAT Live Animals dataset. These steps included replacing headers with more descriptive names, reformatting the data into a more readable structure, identifying and handling outliers and erroneous values, removing duplicate entries, and standardizing inconsistent casing or values across the dataset.

Are there any legal or regulatory guidelines for your data or project topic?

The FAOSTAT Live Animals dataset is publicly available and provided by the United Nations, which ensures compliance with international data sharing standards. However, the use of this data must still adhere to general data privacy regulations such as the General Data Protection Regulation (GDPR) in Europe, ensuring that no personal data is inadvertently disclosed or misused.

What risks could be created based on the transformations done?

The transformations could introduce risks such as data distortion if not executed carefully. For instance, improper handling of outliers could lead to the loss of significant data points, and mismanagement of duplicates could result in inflated or deflated statistical analyses. These risks could potentially lead to erroneous conclusions and misinformed decisions based on the dataset.

Did you make any assumptions in cleaning/transforming the data?

Yes, certain assumptions were made during the data cleaning process. For example, it was assumed that missing values in specific fields should be treated as nulls rather than zeroes to avoid skewing the data. Additionally, it was assumed that certain inconsistencies in casing and value formatting were unintentional errors rather than meaningful distinctions.

How was your data sourced/verified for credibility?

The dataset was sourced from FAOSTAT, a reputable and reliable provider of global food and agriculture statistics managed by the United Nations. The credibility of the data was further verified by cross-referencing key statistics with other authoritative sources in agricultural research to ensure consistency and accuracy.

Was your data acquired in an ethical way?

Yes, the data was acquired ethically, following the proper procedures for accessing and using publicly available datasets. The data is openly shared by FAOSTAT for research and analysis purposes, ensuring that the use of this data adheres to ethical standards and promotes transparency.

How would you mitigate any of the ethical implications you have identified?

To mitigate ethical implications, several measures can be taken. First, maintaining transparency in the data wrangling process through thorough documentation of all transformations ensures accountability. Second, implementing rigorous validation checks during the data cleaning process helps maintain data integrity. Third, ensuring that any sensitive or potentially identifiable information is anonymized protects privacy. Lastly, adhering to legal and regulatory guidelines while engaging in continuous ethical reviews ensures that the data handling process remains compliant with ethical standards.


```python

```

# Short Report on Term Project Milstone 4:


Milestone 4: Connecting to an API/Pulling in the Data and Cleaning/Formatting

Summary:

Milestone 4 involves connecting to an API, pulling in the data, and performing at least five data transformation and cleansing steps to ensure a clean dataset at the end of the milestone. The Kaggle API data was subjected to various transformation techniques such as replacing headers, formatting data into a more readable format, identifying outliers, finding duplicates, and fixing casing or inconsistent values.

Introduction:

Data obtained from APIs often require cleaning and formatting to prepare them for analysis. In this milestone 4, I connected to Kaggle API and pulled the LiveAnimals Dataset by applying various transformation techniques to ensure the dataset is clean, consistent, and formatted correctly. By performing these steps, I aimed to improve the quality and reliability of the data for subsequent analysis.

Statement of the Problem:

The data obtained from the API may contain errors, inconsistencies, or missing values that could affect the accuracy of the analysis. Therefore, it is essential to perform data cleaning and formatting to ensure the dataset is reliable and suitable for analysis. Ethical considerations such as data privacy, integrity, and transparency must be upheld throughout the data wrangling process.

About the Dataset:

In this Milestone 4 of the term project, the FAOSTAT historical dataset on Live Animals was obtained from Kaggle using this API Command: kaggle datasets download -d unitednations/global-food-agriculture-statistics. The dataset represents over 200 countries with more than 25 primary products and inputs collected between 1961 and 2013. Key variables in the dataset include Area or Country, Item (Agricultural Products, Cattle, Sheep, Chicken, Crops, etc.), Element (Import Quantity, Export Quantity, Import Value, Export Value), Year (1961 – 2013), and Value.

Methodology:

More than 10 data transformation and cleansing steps were applied to the API data:

Replacing Headers: Standardized the headers to ensure they are descriptive and consistent.
Formatting Data: Reformatted data into a more readable and consistent structure.
Identifying Outliers: Detected and handled outliers to maintain data integrity.
Finding Duplicates: Identified and removed duplicate entries to ensure data accuracy.
Fixing Casing/Inconsistent Values: Corrected casing issues and ensured uniformity in data values.
& others.

Each step was clearly labeled and described to provide transparency and clarity in the data wrangling process.


Results:

Upon completion of the data transformation and cleansing steps, the API dataset was clean, consistent, and formatted correctly. The human-readable dataset printed at the end of the milestone demonstrated the effectiveness of the applied transformations, with improved readability and accuracy. The dataset is now ready for further analysis in subsequent milestones.

Discussion:

The data transformation and cleansing steps are essential for ensuring the integrity and reliability of the dataset. By addressing issues such as outliers, duplicates, and inconsistent values, I improved the quality of the data and minimized the risk of erroneous conclusions. Ethical implications such as data privacy and integrity were carefully considered throughout the process to uphold ethical standards and maintain trust in the analysis.

Conclusion:

In conclusion, the data transformation and cleansing steps applied in this milestone played a crucial role in preparing the API dataset for analysis. By identifying and addressing issues such as outliers, duplicates, and inconsistent values, I ensured the dataset is clean, consistent, and ready for further exploration. Moving forward, the clean dataset will serve as the foundation for subsequent analyses and insights in the project.

The Way Forward:

The next steps will involve conducting exploratory data analysis (EDA) and visualization to gain insights into the relationships and patterns within the dataset. By analyzing the cleaned dataset, I can uncover trends, correlations, and anomalies that provide valuable insights into the subject area. Ethical considerations will continue to be prioritized, with a focus on maintaining data privacy, integrity, and transparency throughout the analysis process.


```python

```
