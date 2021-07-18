# pull official base image
FROM python:3.9.5-slim-buster


# set working directory and copy files over
WORKDIR /app
COPY . .

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install packages
RUN pip3 install -r requirements.txt


CMD flask run
