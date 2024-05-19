FROM python:latest
RUN apt-get update
WORKDIR /app
COPY . /app
RUN python3 -m pip install -r requirements.txt