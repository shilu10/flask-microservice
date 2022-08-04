FROM python:3.10.0-alpine

WORKDIR /app 

COPY requirements.txt /app/requirements.txt 

RUN pip install -r requirements.txt

COPY tests/ /app/tests

CMD pytest tests/
