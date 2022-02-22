FROM python:3.9

MAINTAINER "Vitalii Zhuk <zhuk2205@gmail.com>"

RUN \
    pip install pandas && \
    pip install matplotlib seaborn && \
    pip install scikit-learn && \
    pip install requests && \
    pip install bs4 && \
    pip install lxml

WORKDIR /code
