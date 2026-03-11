import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
dataset=load_iris()
x_train, x_test,y_train, y_test=train_test_split(dataset["data"], dataset["target"], random_state=0)
kn=KNeighborsClassifier(n_neighbors=1)
kn.fit(x_train, y_train)
correct=0
wrong=0
for i in range(len(x_test)):
    x=x_test[i]
    x_new=np.array([x])
    prediction=kn.predict(x_new)
    print("TARGET=", y_test[i], dataset["target_names"][y_test[i]],"PREDICTED=", prediction, dataset["target_names"] [prediction])
    if y_test[i] == prediction:
        correct+=1
    else:
        wrong+=1
print("Correct=", correct)
print("Wrong=",wrong)
print("Accuracy=",kn.score(x_test,y_test))