FROM python:latest

RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .


RUN python3 models.py
RUN python3 main.py