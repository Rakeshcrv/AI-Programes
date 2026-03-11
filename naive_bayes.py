import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
iris=load_iris()
data=pd. DataFrame(data=iris.data, columns=iris. feature_names)
data['species' ]=iris.target
x=data.iloc[:, :- 1]
y=data.iloc[:, -1]
x_train, x_test, y_train, y_test=train_test_split( x, y, test_size=0.2,random_state=42)
scalar=StandardScaler()
x_train_scaled=scalar.fit_transform(x_train)
x_test_scaled=scalar.transform(x_test)
naive_bayes=GaussianNB()
naive_bayes. fit(x_train_scaled, y_train)
y_pred=naive_bayes.predict(x_test_scaled)
acc=accuracy_score(y_test,y_pred)
print("accuracy=", acc)
con_mat=confusion_matrix(y_test,y_pred)
print("confusion matrix=", con_mat)
plt.figure(figsize=(5,5))
plt.imshow(con_mat, interpolation='nearest', cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.colorbar()
tick_marks=np.arange(len(iris.target_names))
plt.xticks(tick_marks,iris. target_names, rotation=45)
plt.yticks(tick_marks, iris.target_names)
plt.xlabel("predicted")
plt.ylabel("true value")
plt.tight_layout()
plt.show()