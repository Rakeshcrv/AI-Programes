import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
data=load_iris()
x=data.data
y=data. target
x_train, x_test, y_train, y_test=train_test_split( x,y,test_size=0.2,random_state=42)
scalar=StandardScaler()
x_train=scalar.fit_transform(x_train)
x_test=scalar. transform(x_test)
svm_classifier=SVC(kernel="linear",random_state=42)
svm_classifier.fit(x_train, y_train)
y_pred=svm_classifier.predict(x_test)
accuracy=accuracy_score(y_test, y_pred)
conf_mat=confusion_matrix(y_test, y_pred)
print("accuracy=", accuracy)
print("confusion matrix=\n",conf_mat)