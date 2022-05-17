FROM python:3.9.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apt update && apt upgrade -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

