FROM resin/raspberry-pi3-python:3.6-slim

ADD . /code

WORKDIR /code

RUN pip3 install -r requirements.txt

ENV FLASK_APP=__init__.py

CMD ["flask", "run"]