import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import VotingClassifier
from sklearn import model_selection
url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names=['sepal-length','sepal-width','petal-length','petal-width']
dataset=read_csv(url,names)
print(dataset.shape)
print(dataet.head())
print(dataset.describe())
print(dataset.groupby("class").size())
dataset.plot(kind="box",subplots="True",layout=(2,2),sharex="False",sharey="False")
pyplot.show()
dataset.hist()
pyplot.show()
scatter_matrix(dataset)
pyplot.show()
array=dataset.values
x=array[:,0:4]
y=array[:,4]
x_train,X_valudation,Y_train,Y_validation=train_test_split(X,y,test_size=0.2,random_state=1)
models=[]
models.append(('LR',LogisticRegression(solver='liblinear',multi_class='ovr')))
models.append(('KNN',KNeighborsClassifier()))
models.append(('NB',GaussianDB()))
models.append(('SVM',SVC(gamma='auto')))
results=[]
names=[]
for name , model in models:
  kfold= StratifiedKFold(n_splits=10,random_state=1)
  cv_results=cross_val_score(model,X_train,Y_train,cv=kfold,scoring='accuracy')
  results.append(cv_results)
  names.append(name)
  print("%s:%f(%f)" %(name,cv_results.mean(),cv_results.std()))
  pyplot.boxplot(results,labels=names)
  pyplot.title("algorithm comparison")
  pyplot.show()
  model=SVC(gamma="auto")
  model.fit(X_train,Y_train)
  predictions=model.predict(X_validation)
  print(accuracy_score(Y_validation,predictions))
  print(confusion_matrix(Y_validation,predictions))
  print(classification_report(Y_validation,predictions))
  
       

  

              
