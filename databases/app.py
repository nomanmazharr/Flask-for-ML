from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)


    def __repr__(self) -> str:
        return f'Employee {self.name} is {self.age} years old having email {self.email}'


if '__name__' == '__main__':
    app.run(debug=True)