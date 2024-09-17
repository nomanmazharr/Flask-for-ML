from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///psl.db"

db = SQLAlchemy(app)

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    teams = db.Column(db.String(50), nullable=False, unique=True)
    city = db.Column(db.String(50), nullable=False)
    # members = db.Column()

    def __repr__(self):
        return f'Team {self.teams} have city {self.city}'
    

if __name__ == '__main__':
    app.run(debug=True)