from data import *
from datalabels import *
import pandas as pd
import numpy as np
years=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
months=['January','February','March','April','May','June','July','August','September','October','November','December']
Classifier1Data=pd.DataFrame(np.zeros((1536,10)),columns=['District','Year','Month','Rainfall','Average Rainfall','Temperature','Average Temperature','Pressure','Average Pressure','Drought Classification'])
count=0

def avglabel(value,mini,maxi,classes):
	increment=(maxi-mini)/classes
	lb=mini
	label=1
	while(True):
		if(value>=lb and value<(lb+increment)):
			break
		label+=1
		lb+=increment
	return label

def integrate(district,rfdistrict,pressdistrict,tempdistrict,rfdistrictl,pressdistrictl,tempdistrictl,districtdroughtyn):
	global count
	for year in range(16):
		for month in range(12):
			rfaverage=avglabel(rfdistrict[rfdistrict.columns[month].encode('ascii')].mean(),0,615.40,10)
			rf=rfdistrictl.ix[month,years[year]]
			pressaverage=avglabel(pressdistrict[pressdistrict.columns[month].encode('ascii')].mean(),1000,1017,6)
			press=pressdistrictl.ix[month,years[year]]
			tempaverage=avglabel(tempdistrict[tempdistrict.columns[month].encode('ascii')].mean(),18,39,5)
			temp=tempdistrictl.ix[month,years[year]]
			drought=districtdroughtyn.ix[month,years[year]]
			Classifier1Data.ix[count]=[district,years[year],months[month],rf,rfaverage,press,pressaverage,temp,tempaverage,drought]
			count+=1

integrate('Nagpur',rfnagpur,pressnagpur,tempnagpur,rfnagpurl,pressnagpurl,tempnagpurl,nagpurdroughtyn)
integrate('Pune',rfpune,presspune,temppune,rfpunel,presspunel,temppunel,punedroughtyn)
integrate('Nashik',rfnashik,pressnashik,tempnashik,rfnashikl,pressnashikl,tempnashikl,nashikdroughtyn)
integrate('Aurangabad',rfaurangabad,pressaurangabad,tempaurangabad,rfaurangabadl,pressaurangabadl,tempaurangabadl,aurangabaddroughtyn)
integrate('Amravati',rfamravati,pressamravati,tempamravati,rfamravatil,pressamravatil,tempamravatil,amravatidroughtyn)
integrate('Solapur',rfsolapur,presssolapur,tempsolapur,rfsolapurl,presssolapurl,tempsolapurl,solapurdroughtyn)
integrate('Yavatmal',rfyavatmal,pressyavatmal,tempyavatmal,rfyavatmall,pressyavatmall,tempyavatmall,yavatmaldroughtyn)
integrate('Latur',rflatur,presslatur,templatur,rflaturl,presslaturl,templaturl,laturdroughtyn)

writer=pd.ExcelWriter('Classifier1Data.xlsx')
Classifier1Data.to_excel(writer)