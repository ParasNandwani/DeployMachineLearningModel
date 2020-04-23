FROM continuumio/anaconda3:4.4.0

MAINTAINER UNP, https://unp.education

EXPOSE 8000

RUN apt-get update && apt-get install -y apache2 \ 
	apache2-dev \
	vim \
&& apt-get clean \
&& apt-get autoremove \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/flaskpredict/


COPY ./flaskpredictapi.wsgi  /var/www/flaskpredict/flaskpredictapi.wsgi

COPY ./flaskpredictapi  /var/www/flaskpredict/

RUN pip install -r requirements.txt

RUN /opt/conda/bin/mod_wsgi-express install-module

RUN mod_wsgi-express setup-server flaskpredictapi.wsgi --port=8000 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80

CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND
