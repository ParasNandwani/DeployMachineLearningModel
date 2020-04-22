#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 08:16:01 2020

@author: parasnandwani10
"""


#Random Forest Classifier to Classify Iris flower


from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

#loading data set

iris=load_iris()
X=iris.data
Y=iris.target


#split data into train test
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42,test_size=0.5)

#Build the model
clf=RandomForestClassifier(n_estimators=10)

#Model training
clf.fit(X_train,Y_train)

#Predictions
Y_Pred=clf.predict(X_test)

#check accuracy
print(accuracy_score(Y_Pred,Y_test))