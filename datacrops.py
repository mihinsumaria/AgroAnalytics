# Bajra, Jowar, Sugarcane, (Maize), Soyabean

import pandas as pd
import numpy as np
from sklearn import preprocessing
"""datacrops=pd.read_csv('Data\CropMaharashtra.csv')
datacrops=datacrops[datacrops['Crop_Year']>=2001]
datacrops=datacrops[(datacrops['Crop']=='Jowar') | (datacrops['Crop']=='Bajra') | (datacrops['Crop']=='Sugarcane') | (datacrops['Crop']=='Soyabean') | (datacrops['Crop']=='Cotton')]
datacrops['Productivity']=datacrops['Production (tonnes)']/datacrops['Area (ha)']
datacrops=datacrops.drop(['State_Name'],axis=1)
datacrops=datacrops[(datacrops['District_Name']=='NAGPUR') | (datacrops['District_Name']=='PUNE') | (datacrops['District_Name']=='NASHIK') | (datacrops['District_Name']=='AURANGABAD') | (datacrops['District_Name']=='AMRAVATI') | (datacrops['District_Name']=='SOLAPUR') | (datacrops['District_Name']=='YAVATMAL') | (datacrops['District_Name']=='LATUR')]
print datacrops"""

datacrops=pd.read_csv('Data\CropProject.csv')
datacrops=datacrops[datacrops.Season.str.contains("Rabi")==False]
def labelassignment(cropname):
	m=preprocessing.MinMaxScaler(feature_range=(0,4))
	dc=datacrops[(datacrops['Crop']==cropname)].dropna(how='any',axis=0,subset=['Productivity'])
	sdc=m.fit_transform(dc['Productivity'])
	sdc=np.around(sdc)
	dc['CropLabel']=sdc
	return dc

def writing(dc,writer,sheetname):
	dc.to_excel(writer,sheetname)

dcbajra=labelassignment('Bajra')
dcjowar=labelassignment('Jowar')
dcsugarcane=labelassignment('Sugarcane')
dcsoya=labelassignment('Soyabean')

"""writer = pd.ExcelWriter('CropLabels.xlsx')
writing(dcbajra,writer,'Bajra')
writing(dcjowar,writer,'Jowar')
writing(dcsugarcane,writer,'Sugarcane')
writing(dcsoya,writer,'Soyabean')"""