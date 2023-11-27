# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
RUN pip install psycopg2
RUN pip install psycopg2[binary]
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

ENTRYPOINT ["/docker-entrypoint.sh"]
