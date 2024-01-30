FROM python:3.11.5-slim-bullseye

ENV PYTHONUNBUFFERED=

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .