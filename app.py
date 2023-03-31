from flask import Flask, render_template, request

app = Flask(__name__)

app.config.from_object('config.config')
# app.config["SQLALCHEMY_DATABASE_URI"] = \
#    'postgresql://postgres:postgres@localhost:5432/my_flask_db'
    # If you run postgres in container and app locally
    # 'postgresql://postgres:postgres@localhost:5432/my_flask_db'

app.config.update(
    SQLALCHEMY_DATABASE_URI=app.config.get('DATABASE_URI'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

from models import db, Item

db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()


@app.route('/')
def main():
    return render_template('index.html')

@app.route("/add", methods=['POST'])
def add_item_from_form():
    name = str(request.form['name'])
    shop = str(request.form['shop'])
    cost = str(request.form['cost'])

    new_item = Item(name=name, shop=shop, cost=cost)
    db.session.add(new_item)
    db.session.commit()
    
    data = Item.query.all()
    items = ((item.name, item.shop, item.cost) for item in data)
    print(type(items))
    headings = ("Name", "Shop", "Cost")
    return render_template('index.html', items=items, headings=headings)

@app.route("/items", methods=['GET'])
def get_items():
	items = Item.query.all()
	return str([str(item) + '\n' for item in items])

@app.route("/delete")
def delete_items():
    db.session.query(Item).delete()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
