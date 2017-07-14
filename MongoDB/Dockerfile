FROM resin/raspberry-pi3-python:3.6-slim

RUN apt-get update
RUN apt-get upgrade
RUN apt-get install mongodb

RUN mkdir -p /data/db/

RUN mongod --repair

EXPOSE 27017
CMD ["mongod"]