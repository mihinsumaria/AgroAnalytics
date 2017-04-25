import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
#places=['nagpur','pune','nashik','aurangabad','amravati']
#writer=pd.ExcelWriter('pressure.xlsx')
#for place in places:
i=2009
j=9
d={'2001':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2002':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2003':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2004':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2005':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2006':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2007':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2008':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2009':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2010':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2011':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2012':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2013':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2014':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2015':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12']),
'2016':pd.Series([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],index=['1','2','3','4','5','6','7','8','9','10','11','12'])}
df=pd.DataFrame(d)
while(i<=2016 and j<=12):
	print i,j
	url="https://www.timeanddate.com/weather/india/amravati/historic?month="+str(j)+"&year="+str(i)
	r=requests.get(url)
	soup=BeautifulSoup(r.text,"lxml")
	table=soup.find('table',{'class':'zebra tb-wt fw tb-hover'})
	td=int(table.find('tbody').find('tr',{'class':'sep-t'}).find('th',text='Average').findNext('td').findNext('td').findNext('td').text.split()[0])
	print td
	df[str(i)][str(j)]=td
	j+=1
	if(j>12 and i<2016):
		j=1
		i+=1
df.to_csv('pressureamravat.cisv')
