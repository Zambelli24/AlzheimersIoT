FROM resin/raspberry-pi3-python:3.6-slim

ADD . /code

WORKDIR /code

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python3", "backup_api.py"]