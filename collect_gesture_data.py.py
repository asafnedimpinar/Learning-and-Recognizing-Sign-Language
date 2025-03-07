import  pandas as pd 
import os 
import pickle  
import mediapipe as mp 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
import numpy as np

data_dict = pickle.load(open("data.pickle", "rb"))

data = np.asarray(data_dict["data"])
labels = np.asarray(data_dict["labels"])

print(data.shape)  
print(labels.shape)  

x = data
y = labels
x_train, x_test, y_train, y_test = train_test_split(x ,y , train_size=0.70, shuffle=True)


model = RandomForestClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
score = accuracy_score(y_test, y_pred)

print("Başarı:", score * 100)

f = open("model.p", "wb")
pickle.dump({"model": model}, f)
f.close()
