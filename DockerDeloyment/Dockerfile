FROM continuumio/anaconda3:4.4.0

MAINTAINER UNP, https://unp.education

COPY . /Users/parasnandwani10/Documents/DeployModel/DeployMachineLearningModel

EXPOSE 5000

WORKDIR /Users/parasnandwani10/Documents/DeployModel/DeployMachineLearningModel

RUN pip install -r requirements.txt

CMD python flaskswagger.py
