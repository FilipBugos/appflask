# flask-postgres-app

Simple Flask app using Postgres as database

Author: Matej Kleman

## How to deploy
1. Install docker:
    $ sudo snap install docker

2. Replace <backend_ip> in your connection string in app/flask_app.py with IP of your backend VM

3. Build flask docker image:
    $ sudo docker build -t flaskapp .

4. Run your app:
    $ sudo docker run -name flaskapp -p 5000:5000 flaskapp
