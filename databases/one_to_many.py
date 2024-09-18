from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///psl.db"

db = SQLAlchemy(app)

class Teams(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key = True)
    teams = db.Column(db.String(50), nullable=False, unique=True)
    city = db.Column(db.String(50), nullable=False)
    members = db.relationship("Players", backref='team') # helps to populate the team id according to the team we don't need to remeber the id for each team while entering data for players

    def __repr__(self):
        return f'Team {self.teams} have city {self.city}'
    
class Players(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    nationality = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))    

    def __repr__(self):
        return f'Player {self.name} is from {self.nationality}'


if __name__ == '__main__':
    app.run(debug=True)