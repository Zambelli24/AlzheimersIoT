FROM resin/raspberry-pi3-python:3.6-slim

RUN apt-get install mongodb

RUN mkdir -p /data/db

WORKDIR /usr/local/bin

EXPOSE 27017
CMD ["mongod"]