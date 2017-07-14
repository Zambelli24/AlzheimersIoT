FROM resin/raspberry-pi3-python:3.6-slim

VOLUME /config
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY virtualization/Docker/ virtualization/Docker/
RUN virtualization/Docker/setup_docker_prereqs

COPY requirements_all.txt requirements_all.txt

RUN pip3 install --no-cahce-dir -r requirements_all.txt && \
    pip3 install --no-cache-dir mysqlclient psycopg2 uvloop cchardet

COPY . .

CMD [ "python", "-m", "homeassistant", "--config", "/config"]