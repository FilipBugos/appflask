sudo apt-get update -y && \
    apt-get install -y python3-pip python3-flask && \
    apt install -y libpq-dev

pip3 install -r app/requirements.txt

export FLASK_APP=app/flask_app.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_ENV=development

flask run
