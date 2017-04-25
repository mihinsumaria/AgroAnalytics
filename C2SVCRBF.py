from data import *
from datalabels import *
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

C2Data=pd.read_excel(io='Data\Classifier2Data.xlsx',sheetname='Soyabean')
C2Data.drop(['District','Year','Season','Crop','Area','Production','Productivity'],axis=1,inplace=True)
train=C2Data.ix[:78]
test=C2Data.ix[78:]
clf=SVC(kernel='rbf')
clf.fit(train.drop(['CropLabel'],axis=1),train['CropLabel'])
C2Output=clf.predict(test.drop(['CropLabel'],axis=1))
accuracy=accuracy_score(test['CropLabel'],C2Output)
cm=confusion_matrix(test['CropLabel'],C2Output)
dfcm=pd.DataFrame(cm)
plt.figure(1)
sns.heatmap(dfcm,annot=True)
plt.title('Classifier 2 SVC RBF Kernel Confusion Matrix, Accuracy=%f'%(accuracy))
plt.show()