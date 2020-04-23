#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:26:11 2020

@author: parasnandwani10
"""

"""
In this file we are generating UI with flasgger package
"""

import pickle
from flask import Flask,request
from flasgger import Swagger
import numpy as np

with open('rf.pkl','rb') as model_pkl:#reead binary raed as binary file not as usual file
    model=pickle.load(model_pkl)#loading model pickel file
    #perfectly train model ready to predictions
    


app=Flask(__name__)
swagger=Swagger(app)# swaggerify flask application

@app.route('/predict')
def predict():
    
    """Example endpoint returning a prediction of iris
    ---
    parameters :
    - name:s_length
      in:query
      type:number
      required:true
    - name:s_width
     in:query
     type:number
     required:true
    - name:p_length
     in:query
     type:number
     required:true
    - name:p_width
     in:query
     type:number
     required:true
"""
    s_length=request.args.get("s_length")
    s_width=request.args.get("s_width")
    p_length=request.args.get("p_length")
    p_width=request.args.get("p_width")
    print(np.array([[s_length,s_width,p_length,p_width]]))
    predcition=model.predict(np.array([[s_length,s_width,p_length,p_width]]))
    return str(predcition)
    

if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)
