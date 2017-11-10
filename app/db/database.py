from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from app import app


# Define the blueprint: 'highlights', set its url prefix: app.url/highlights
db_setup = Blueprint('dbsetup', __name__)


# Create database instance
db = SQLAlchemy(app)


class Athlete(db.Model):
    """
    Create database table to store Athlete table data
    """
    __tablename__ = 'Athlete'

    id = db.Column('id', db.Integer, primary_key=True)
    salary = db.Column('salary', db.Integer)
    name = db.Column('name', db.String(100))
    dob = db.Column('dob', db.Date)
    status = db.Column('status', db.String(100))
    placeOfBirth = db.Column('placeOfBirth', db.String(100))
    countryID = db.Column('countryID', db.String(100))
    goals = db.Column('goals', db.Integer)
    assists = db.Column('assists', db.Integer)
    wins = db.Column('wins', db.Integer)
    losses = db.Column('losses', db.Integer)

    def __init__(self, id, salary, name, dob, status, placeOfBirth, countryID, goals, assists, wins, losses):
        self.id = id
        self.salary = salary
        self.name = name
        self.dob = dob
        self.status = status
        self.placeOfBirth = placeOfBirth
        self.countryID = countryID
        self.goals = goals
        self.assists = assists
        self.wins = wins
        self.losses = losses


class Coach(db.Model):
    __tablename__ = 'Coach'

    id = db.Column('id', db.Integer, primary_key=True)
    salary = db.Column('salary', db.Integer)
    name = db.Column('name', db.String(100))
    dob = db.Column('dob', db.Date)
    status = db.Column('status', db.String(100))
    placeOfBirth = db.Column('placeOfBirth', db.String(100))
    countryID = db.Column('countryID', db.String(100))

    def __init__(self, id, salary, name, dob, status, placeOfBirth, countryID):
        self.id = id
        self.salary = salary
        self.name = name
        self.dob = dob
        self.status = status
        self.placeOfBirth = placeOfBirth
        self.countryID = countryID


class Competition(db.Model):
    __tablename__ = 'Competition'

    name = db.Column('name', db.String(100), primary_key=True)
    winner = db.Column('winner', db.String(100))

    def __init__(self, name, winner):
        self.name = name
        self.winner = winner
        self.name = name


class Game(db.Model):
    __tablename__ = 'Game'

    score = db.Column('score', db.String(100))
    gameID = db.Column('gameID', db.Integer, primary_key=True)
    round = db.Column('column', db.Integer)
    winningTeamID = db.Column('winningTeamID', db.Integer)
    losingTeamID = db.Column('losingTeamID', db.Integer)

    def __init__(self, score, gameID, round, winngingTeamID, losingTeamID):
        self.score = score
        self.gameID = gameID
        self.round = round
        self.winningTeamID = winngingTeamID
        self.losingTeamID = losingTeamID


class Season(db.Model):
    __tablename__ = 'Season'

    seasonID = db.Column('seasonID', db.Integer, primary_key=True)
    year = db.Column('year', db.Integer)

    def __init__(self, seasonID, year):
        self.seasonID = seasonID
        self.year = year


class Stadium(db.Model):
    __tablename__ = 'Stadium'

    name = db.Column('name', db.String(100), primary_key=True)
    location = db.Column('location', db.String(100), primary_key=True)

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Team(db.Model):
    __tablename__ = 'Team'

    name = db.Column('name', db.String(100))
    teamID = db.Column('teamID', db.Integer, primary_key=True)
    location = db.Column('location', db.String(100))
    dateCreated = db.Column('dateCreated', db.Date)
    goals = db.Column('goals', db.Integer)
    assists = db.Column('assists', db.Integer)
    wins = db.Column('wins', db.Integer)
    losses = db.Column('losses', db.Integer)

    def __init__(self, name, teamID, location, dateCreated, goals, assists, wins, losses):
        self.name = name
        self.teamID = teamID
        self.location = location
        self.dateCreated = dateCreated
        self.goals = goals
        self.assists = assists
        self.wins = wins
        self.losses = losses