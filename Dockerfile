FROM python:3.8

MAINTAINER "Vitalii Zhuk <zhuk2205@gmail.com>"

COPY requirements.txt requirements.txt

RUN \
    pip install -r requirements.txt

WORKDIR /code
