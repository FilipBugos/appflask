apt-get update -y && \
    apt-get install -y python3-pip && \
    apt install -y libpq-dev

pip3 install -r requirements.txt

export FLASK_APP=app/flask_app.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_ENV=development

flask run
