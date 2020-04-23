#!/usr/bin/env python3


import sys

sys.path.insert(0,"/Users/parasnandwani10/Documents/DeployModel/DeployMachineLearningModel/var/www/flask_predict_api")
sys.path.insert(0,"/opt/conda/lib/python3.6/site-packages")
sys.path.insert(0,"/opt/conda/bin")

import os
os.environ['PYTHONPATH']='/opt/conda/bin/python'

from flaskpredictapi import app as application