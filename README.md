# flask-postgres-app

Simple Flask app using Postgres as database

Author: Matej Kleman

## How to deploy Flask app
1. Install docker: \
    *$ sudo snap install docker*

2. Replace <backend_ip> in your connection string in app/flask_app.py with IP of your backend VM

3. Build flask docker image: \
    *$ sudo docker build -t flaskapp .*

4. Run your app: \
    *$ sudo docker run -n flaskapp -p 5000:5000 flaskapp*

## How to deploy Postgres DB
1. Install docker: \
    *$ sudo snap install docker*

2. Run this command: \
    *docker run --name my_postgres_container -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=my_flask_db -p 5432:5432 -d postgres*
