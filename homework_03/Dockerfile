FROM python:3.9-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --editable .

ENTRYPOINT [ "webapp" ]

EXPOSE 8000
