FROM python:3.9.2-alpine
# MAINTAINER Omambia M. Dauglous

#Unbuffered varaible

ENV PYTHONUNBUFFERED 1

COPY requirements.txt  /requirements.txt 
RUN pip install -r requirements.txt

# make directory where to store out application with docker
RUN mkdir /app
WORKDIR /app
# copy local app to docker app working directly 
COPY ./app /app


## create user who runs only application. 
# for security reasons - so that none can access the application
RUN adduser -D user
USER user

