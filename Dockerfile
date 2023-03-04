# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

RUN chmod u+x ./start.sh
ENTRYPOINT ["./start.sh"]