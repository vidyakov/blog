FROM python:3.8.3-slim

WORKDIR /app

COPY project/requirements.txt .
RUN pip install -r requirements.txt
COPY project/ .

RUN chmod 777 ./create_models.sh

EXPOSE 5000