FROM python:3.9-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --editable .

RUN pwd && ls -laR && pip list
