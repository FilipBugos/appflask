FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    apt install -y libpq-dev

ENV FLASK_APP=app/flask_app.py

ENV FLASK_RUN_HOST=0.0.0.0

ENV FLASK_ENV=development

COPY app/requirements.txt /app/requirements.txt

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run"]
