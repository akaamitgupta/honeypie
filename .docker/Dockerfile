FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN adduser -D user
USER user
