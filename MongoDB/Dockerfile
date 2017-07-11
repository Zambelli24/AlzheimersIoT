FROM resin/rpi-raspbian:wheezy

RUN apt-get install mongodb-server

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb \
    && mkdir -p /data/db

WORKDIR /usr/local/bin

COPY mongod .

EXPOSE 27017
CMD ["mongod"]