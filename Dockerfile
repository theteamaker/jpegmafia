FROM python:3-slim-buster

COPY peggy.py /app/
COPY requirements.txt /app/
COPY .env.dist /app/.env

WORKDIR /app

RUN pip install -r requirements.txt

CMD python peggy.py