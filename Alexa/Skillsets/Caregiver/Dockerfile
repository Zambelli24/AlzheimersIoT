FROM resin/raspberry-pi3-python:3.6-slim

# dependencies need to run
RUN apt-get update -y
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
#RUN apt-get install -y python3-pip python3.5

# update the pip3 
RUN pip3 install --upgrade pip

RUN pip3 install flask-ask requests

COPY . /usr/src/Caregiver

CMD ["python3", "/usr/src/Caregiver/caregiver.py"]
