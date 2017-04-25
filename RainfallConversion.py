from data import *
import numpy as np
import pandas as pd
np.set_printoptions(threshold=np.inf)
pd.set_option('display.max_colwidth', -1)
labels=['1','2','3','4','5','6','7','8','9','10']
months=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
#months=['January','February','March','April','May','June','July','August','September','October','November','December']
rf=np.ravel(np.array([rfnagpur.values,rfpune.values,rfnashik.values,rfaurangabad.values,rfamravati.values,rfsolapur.values,rfyavatmal.values,rflatur.values]))
rf=pd.cut(rf,10,right=False,labels=labels)
rf3=[]
j=0
for k in range(8):
	rf2=[]
	for i in range(16):
		rf2.append(rf[j:j+12])
		j+=12
	rf3.append(rf2)

rfnagpur=pd.DataFrame(rf3[0],columns=months)
rfpune=pd.DataFrame(rf3[1],columns=months)
rfnashik=pd.DataFrame(rf3[2],columns=months)
rfaurangabad=pd.DataFrame(rf3[3],columns=months)
rfamravati=pd.DataFrame(rf3[4],columns=months)
rfsolapur=pd.DataFrame(rf3[5],columns=months)
rfyavatmal=pd.DataFrame(rf3[6],columns=months)
rflatur=pd.DataFrame(rf3[7],columns=months)
writer = pd.ExcelWriter('Rainfall_pandas_labels.xlsx')
rfnagpur.to_excel(writer,'Nagpur')
rfpune.to_excel(writer,'Pune')
rfnashik.to_excel(writer,'Nashik')
rfaurangabad.to_excel(writer,'Aurangabad')
rfamravati.to_excel(writer,'Amravati')
rfsolapur.to_excel(writer,'Solapur')
rfyavatmal.to_excel(writer,'Yavatmal')
rflatur.to_excel(writer,'Latur')