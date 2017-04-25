# AgroAnalytics
Agro Analytics - Data Mining/Machine Learning Project based on Agricultural datasets. For more info, go to www.agroanalytics.info 

## Data
1. Rainfall - Raw Rainfall Data (From http://maharain.gov.in/)
2. Temperature_pandas - Raw Temperature Data (From https://www.timeanddate.com/ and http://www.indiawaterportal.org/met_data/)
3. Pressure_pandas - Raw Pressure Data (From https://www.timeanddate.com/)
4. CropProject - https://data.gov.in/catalog/district-wise-season-wise-crop-production-statistics
5. Rainfall_pandas_labels - Labelled Rainfall Data
6. Temperature_pandas_labels - Labelled Temperature Data
7. Pressure_pandas_labels - Labelled Pressure Data
8. Drought_10_pandas_labels - Drought Training Data Labels
9. Crop Labels - Crop Productivity Labels
10. Classifier1Data - Integrated Data for Classifier 1
11. Classifier2Data - Integrated Data for Classifier 2

## Code
1. scrape.py - Scraping data off timeanddate (For Temperature and Pressure)
2. RainfallConversion.py - Labeling temperature data
3. TemperatureConversion.py - Labeling temperature data
4. PressureConversion.py - Labeling temperature data
5. data.py - Importing raw data
6. datalabels.py - Importing labeled data
7. datacrops.py - Importing crop data, and labeling it
8. DroughtYN.py - Finding Drought Labels
9. IntegrationC1.py - Integrating data for Classifier 1 
10. C1ID3/SVCRBF/RFC.py - Classifier 1 
11. IntegrationC2.py - Integrating data for Classifier 2 
12. C2ID3/SVCRBF/RFC.py - Classifier 2 

## Results - Confusion Matrices for both classifiers
