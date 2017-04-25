from data import *
np.set_printoptions(threshold=np.inf)
pd.set_option('display.max_colwidth', -1)
labels=['1','2','3','4','5','6']
months=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
#months=['January','February','March','April','May','June','July','August','September','October','November','December']
press=np.ravel(np.array([pressnagpur.values,presspune.values,pressnashik.values,pressaurangabad.values,pressamravati.values,presssolapur.values,pressyavatmal.values,presslatur.values]))
press=pd.cut(press,6,right=False,labels=labels)
press3=[]
j=0
for k in range(8):
	press2=[]
	for i in range(16):
		press2.append(press[j:j+12])
		j+=12
	press3.append(press2)

pressnagpur=pd.DataFrame(press3[0],columns=months)
presspune=pd.DataFrame(press3[1],columns=months)
pressnashik=pd.DataFrame(press3[2],columns=months)
pressaurangabad=pd.DataFrame(press3[3],columns=months)
pressamravati=pd.DataFrame(press3[4],columns=months)
presssolapur=pd.DataFrame(press3[5],columns=months)
pressyavatmal=pd.DataFrame(press3[6],columns=months)
presslatur=pd.DataFrame(press3[7],columns=months)
writer = pd.ExcelWriter('Pressure_pandas_labels.xlsx')
pressnagpur.to_excel(writer,'Nagpur')
presspune.to_excel(writer,'Pune')
pressnashik.to_excel(writer,'Nashik')
pressaurangabad.to_excel(writer,'Aurangabad')
pressamravati.to_excel(writer,'Amravati')
presssolapur.to_excel(writer,'Solapur')
pressyavatmal.to_excel(writer,'Yavatmal')
presslatur.to_excel(writer,'Latur')