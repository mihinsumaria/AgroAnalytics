from data import *
import numpy as np
import pandas as pd
# Nagpur '2002','2004','2011','2014'
# Pune '2001','2002','2003','2009','2011','2012','2014'
# Nashik '2001','2002','2003','2004','2009','2011','2012','2014'
# Aurangabad '2001','2002','2003','2009','2012','2014'
# Amravati '2002','2004','2009','2011','2014'
# Solapur '2001','2002','2003','2009','2011','2012'
# Yavatmal '2002','2004','2009','2014'
# Latur '2001','2002','2003','2004','2009','2011','2012','2014'
droughtdeclarations=[[1,3,10,13],
[0,1,2,8,10,11,13],
[0,1,2,3,8,10,11,13],
[0,1,2,8,11,13],
[1,3,8,10,13],
[0,1,2,8,10,11],
[2,3,8,13],
[0,1,2,3,8,10,11,13]
]

def droughtlabelassignment(years,rfdistrict):
	district=[]
	for year in years:
	#for year in range(16):
		dyear=[]
		for month in rfdistrict:
			label=0
			if(rfdistrict.ix[year,month]<0.8*rfdistrict[month].mean()):
				label=1
			dyear.append(label)
		district.append(dyear)
	return district

def structuring(district,years):
	districtdroughtyn=np.zeros((16,12))
	for i in district:
		for k in years:
			districtdroughtyn[k]=i
	return districtdroughtyn

def writing(districtdroughtyn,writer,sheetname):
	months=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
	districtdroughtyn=pd.DataFrame(np.transpose(districtdroughtyn),columns=months)
	districtdroughtyn.to_excel(writer,sheetname)

nagpur=droughtlabelassignment(droughtdeclarations[0],rfnagpur)
pune=droughtlabelassignment(droughtdeclarations[1],rfpune)
nashik=droughtlabelassignment(droughtdeclarations[2],rfnashik)
aurangabad=droughtlabelassignment(droughtdeclarations[3],rfaurangabad)
amravati=droughtlabelassignment(droughtdeclarations[4],rfamravati)
solapur=droughtlabelassignment(droughtdeclarations[5],rfsolapur)
yavatmal=droughtlabelassignment(droughtdeclarations[6],rfyavatmal)
latur=droughtlabelassignment(droughtdeclarations[7],rflatur)

nagpurdroughtyn=structuring(nagpur,droughtdeclarations[0])
punedroughtyn=structuring(pune,droughtdeclarations[1])
nashikdroughtyn=structuring(nashik,droughtdeclarations[2])
aurangabaddroughtyn=structuring(aurangabad,droughtdeclarations[3])
amravatidroughtyn=structuring(amravati,droughtdeclarations[4])
solapurdroughtyn=structuring(solapur,droughtdeclarations[5])
yavatmaldroughtyn=structuring(yavatmal,droughtdeclarations[6])
laturdroughtyn=structuring(latur,droughtdeclarations[7])

writer = pd.ExcelWriter('DroughtYN_pandas_labels.xlsx')
writing(nagpurdroughtyn,writer,'Nagpur')
writing(punedroughtyn,writer,'Pune')
writing(nashikdroughtyn,writer,'Nashik')
writing(aurangabaddroughtyn,writer,'Aurangabad')
writing(amravatidroughtyn,writer,'Amravati')
writing(solapurdroughtyn,writer,'Solapur')
writing(yavatmaldroughtyn,writer,'Yavatmal')
writing(laturdroughtyn,writer,'Latur')
