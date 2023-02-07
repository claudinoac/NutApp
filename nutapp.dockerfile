FROM python:3.8
RUN mkdir /code
COPY requirements.txt  /code
WORKDIR /code
RUN pip3 install -r requirements.txt
