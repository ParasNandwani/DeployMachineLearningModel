#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:01:41 2020

@author: parasnandwani10
"""


import pickle
import pandas as pd
import numpy as np
from flask import Flask,request


with open('rf.pkl','rb') as model_pkl:
    model=pickle.load(model_pkl)
    
    
    
app=Flask(__name__)

@app.route('/predict_file',methods=["POST"])
def predict_iris_file():
    input_data=pd.read_csv(request.files.get('input_file'),header=None)
    prediction = model.predict(input_data)
    return str(list(prediction))



if __name__=='__main__':
    app.run()
