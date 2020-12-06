FROM python:3.8-slim-buster

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc libpq-dev python-dev && \
    apt-get clean

LABEL maintainer="Nkoli Okafor <nkoli_o@pm.me>"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir -p /food_vendor_project
WORKDIR /food_vendor_project
COPY ./requirements.txt /food_vendor_project/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /food_vendor_project/

ENTRYPOINT ["/food_vendor_project/entrypoint.sh"]