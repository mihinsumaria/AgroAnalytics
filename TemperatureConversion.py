from data import *
np.set_printoptions(threshold=np.inf)
pd.set_option('display.max_colwidth', -1)
labels=['1','2','3','4','5']
months=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
#months=['January','February','March','April','May','June','July','August','September','October','November','December']
temp=np.ravel(np.array([tempnagpur.values,temppune.values,tempnashik.values,tempaurangabad.values,tempamravati.values,tempsolapur.values,tempyavatmal.values,templatur.values]))
temp=pd.cut(temp,5,right=False,labels=labels)
temp3=[]
j=0
for k in range(8):
	temp2=[]
	for i in range(16):
		temp2.append(temp[j:j+12])
		j+=12
	temp3.append(temp2)

tempnagpur=pd.DataFrame(temp3[0],columns=months)
temppune=pd.DataFrame(temp3[1],columns=months)
tempnashik=pd.DataFrame(temp3[2],columns=months)
tempaurangabad=pd.DataFrame(temp3[3],columns=months)
tempamravati=pd.DataFrame(temp3[4],columns=months)
tempsolapur=pd.DataFrame(temp3[5],columns=months)
tempyavatmal=pd.DataFrame(temp3[6],columns=months)
templatur=pd.DataFrame(temp3[7],columns=months)
writer = pd.ExcelWriter('Temperature_pandas_labels.xlsx')
tempnagpur.to_excel(writer,'Nagpur')
temppune.to_excel(writer,'Pune')
tempnashik.to_excel(writer,'Nashik')
tempaurangabad.to_excel(writer,'Aurangabad')
tempamravati.to_excel(writer,'Amravati')
tempsolapur.to_excel(writer,'Solapur')
tempyavatmal.to_excel(writer,'Yavatmal')
templatur.to_excel(writer,'Latur')
"""
temp=np.sort(temp)
tempstd=np.std(temp)
tempmean=np.mean(temp)
tempmedian=np.median(temp)
print temp
print tempmean
print tempstd
print tempstd**2/len(temp)
print tempmedian
"""
