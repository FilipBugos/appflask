from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    shop = db.Column(db.String)
    cost = db.Column(db.String)

    def __init__(self, name, shop, cost):
        self.name = name
        self.shop = shop
        self.cost = cost

    def __repr__(self):
        return "Name: {}, Shop: {}, Cost: {}\n".format(self.name, self.shop, self.cost)