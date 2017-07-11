FROM resin/raspberry-pi3-python:3.6-slim

# Copy sourcefiles
COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Run the app
CMD [ "python", "./googleSender.py" ]
