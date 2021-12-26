FROM jupyter/base-notebook

MAINTAINER "Vitalii Zhuk <zhuk2205@gmail.com>"

RUN \
    pip install pandas && \
    pip install matplotlib seaborn && \
    pip install scikit-learn

WORKDIR /code
