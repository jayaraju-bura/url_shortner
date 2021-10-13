FROM ubuntu:18.04

RUN apt-get update -y && \
apt-get install -y python-pip python-dev

RUN mkdir app

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]
