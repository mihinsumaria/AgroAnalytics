from data import *
from datacrops import *
import numpy as np
import pandas as pd

def writing(dc,writer,sheetname):
	dc.to_excel(writer,sheetname)

def TRImport(cropname):
	Crop=pd.read_excel(io="Data\CropLabels.xlsx",sheetname=cropname)
	k=[]
	t=[]
	for i in Crop.index:
		if(Crop.ix[i]['District']=='NAGPUR'):
			if(Crop.ix[i]['Season']=='Whole Year'):
				k.append(kharnagpur[Crop.ix[i]['Year']-2001])
			else:
				k.append(kharnagpur[Crop.ix[i]['Year']-2001])
			t.append(tknagpur[Crop.ix[i]['Year']-2001])
		elif(Crop.ix[i]['District']=='PUNE'):
			if(Crop.ix[i]['Season']=='Whole Year'):
				k.append(kharpune[Crop.ix[i]['Year']-2001])
			else:
				k.append(kharpune[Crop.ix[i]['Year']-2001])
			t.append(tkpune[Crop.ix[i]['Year']-2001])
		elif(Crop.ix[i]['District']=='NASHIK'):
			if(Crop.ix[i]['Season']=='Whole Year'):
				k.append(kharnashik[Crop.ix[i]['Year']-2001])
			else:
				k.append(kharnashik[Crop.ix[i]['Year']-2001])
			t.append(tknashik[Crop.ix[i]['Year']-2001])
		elif(Crop.ix[i]['District']=='AURANGABAD'):
			if(Crop.ix[i]['Season']=='Whole Year'):
				k.append(kharaurangabad[Crop.ix[i]['Year']-2001])
			else:
				k.append(kharaurangabad[Crop.ix[i]['Year']-2001])
			t.append(tkaurangabad[Crop.ix[i]['Year']-2001])
		elif(Crop.ix[i]['District']=='AMRAVATI'):
			if(Crop.ix[i]['Season']=='Whole Year'):
				k.append(kharamravati[Crop.ix[i]['Year']-2001])
			else:
				k.append(kharamravati[Crop.ix[i]['Year']-2001])
			t.append(tkamravati[Crop.ix[i]['Year']-2001])
		elif(Crop.ix[i]['District']=='SOLAPUR'):
			if(Crop.ix[i]['Season']=='Whole Year'):
				k.append(kharsolapur[Crop.ix[i]['Year']-2001])
			else:
				k.append(kharsolapur[Crop.ix[i]['Year']-2001])
			t.append(tksolapur[Crop.ix[i]['Year']-2001])
		elif(Crop.ix[i]['District']=='YAVATMAL'):
			if(Crop.ix[i]['Season']=='Whole Year'):
				k.append(kharyavatmal[Crop.ix[i]['Year']-2001])
			else:
				k.append(kharyavatmal[Crop.ix[i]['Year']-2001])
			t.append(tkyavatmal[Crop.ix[i]['Year']-2001])
		elif(Crop.ix[i]['District']=='LATUR'):
			if(Crop.ix[i]['Season']=='Whole Year'):
				k.append(kharlatur[Crop.ix[i]['Year']-2001])
			else:
				k.append(kharlatur[Crop.ix[i]['Year']-2001])
			t.append(tklatur[Crop.ix[i]['Year']-2001])
	m=preprocessing.MinMaxScaler(feature_range=(0,4))
	k=np.around(m.fit_transform(k))
	t=np.around(m.fit_transform(t))
	Crop['Rainfall']=k
	Crop['Temperature']=t
	return Crop

Jowar=TRImport('Jowar')
Bajra=TRImport('Bajra')
Sugarcane=TRImport('Sugarcane')
Soyabean=TRImport('Soyabean')

writer=pd.ExcelWriter('Classifier2Data.xlsx')
writing(Bajra,writer,'Bajra')
writing(Jowar,writer,'Jowar')
writing(Sugarcane,writer,'Sugarcane')
writing(Soyabean,writer,'Soyabean')