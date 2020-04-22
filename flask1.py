#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 07:40:02 2020

@author: parasnandwani10
"""

"""
Flask is microservice web based framework which allows us to expose our business logic through api.
"""
#import flask library
from flask import Flask,request

#create an app
app =Flask(__name__)

#Request Mapping
@app.route('/')
def add():
    #getting request params
    #localhost:5000?a=10&b=20
    a=request.args.get("a")
    b=request.args.get("b")
    return str(int(a)+int(b))

#running application
if __name__=='__main__':
        app.run()