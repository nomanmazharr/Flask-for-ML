from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'

db = SQLAlchemy(app)

customer_product = db.Table(
    'association_table',
    db.Column('customers_id', db.Integer, db.ForeignKey('customers.id')),
    db.Column('products_id', db.Integer, db.ForeignKey('products.id'))
)

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), unique=True)
    items = db.relationship('Product', backref='seller', secondary=customer_product)

    def __repr__(self):
        return f'{self.name} bought {self.items}'

class Product(db.Model):
    __tablename__ =  'products'
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(40), nullable= False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Price of {self.product} is {self.price}'


if __name__ == '__main__':
    app.run(debug=True)