from data import *
from datalabels import *
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score
import matplotlib.pyplot as plt
import seaborn as sns

C1Data=pd.read_excel(io='Data\Classifier1Data.xlsx')
#C1Data.drop(['District','Month','Year'],axis=1,inplace=True)
Districts=['Nagpur','Pune','Nashik','Aurangabad','Amravati','Solapur','Yavatmal','Latur']
train=pd.DataFrame()
test=pd.DataFrame()
for district in Districts:
	train=train.append(C1Data[C1Data['District']==district][:150])
	test=test.append(C1Data[C1Data['District']==district][150:])
"""
train=C1Data.ix[:1229]
test=C1Data.ix[1229:]
"""
train.drop(['District','Month','Year'],axis=1,inplace=True)
test.drop(['District','Month','Year'],axis=1,inplace=True)

clf=SVC(kernel='rbf')
clf.fit(train.drop(['Drought Classification'],axis=1),train['Drought Classification'])
C1Output=clf.predict(test.drop(['Drought Classification'],axis=1))
accuracy=accuracy_score(test['Drought Classification'],C1Output)
precision=precision_score(test['Drought Classification'],C1Output,average='macro')
recall=recall_score(test['Drought Classification'],C1Output,average='macro')
cm=confusion_matrix(test['Drought Classification'],C1Output)
dfcm=pd.DataFrame(cm)
plt.figure(1)
sns.heatmap(dfcm,annot=True)
plt.title('Classifier 1 SVC RBF Kernel Confusion Matrix, Accuracy=%f, Precision=%f, Recall=%f'%(accuracy,precision,recall))
plt.show()