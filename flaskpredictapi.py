#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 08:43:37 2020

@author: parasnandwani10
"""

import pickle
from flask import Flask,request
import numpy as np

with open('rf.pkl','rb') as model_file:#reead binary read as binary file not as usual file
    model=pickle.load(model_file)#loading model pickel file
    #perfectly train model ready to predictions
    


app=Flask(__name__)

@app.route('/predict')
def predict():
    s_length=request.args.get("s_length")
    s_width=request.args.get("s_width")
    p_length=request.args.get("p_length")
    p_width=request.args.get("p_width")
    predcition=model.predict(np.array([[s_length,s_width,p_length,p_width]]))
    return str(predcition)
    

if __name__=='__main__':
    app.run()