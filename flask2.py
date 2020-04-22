#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 08:05:59 2020

@author: parasnandwani10
"""

#flask post request
from flask import Flask , request
 
app=Flask(__name__)
 
 
# Define Request Method As Post
@app.route('/',methods=['POST'])
def addPost():
    #Get Form-Data as request Body
    a=request.form["a"]
    b=request.form["b"]
    return str(int(a)+int(b))
 
if __name__=='__main__':
     app.run()