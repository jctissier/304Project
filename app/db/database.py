from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from app import app


# Define the blueprint: 'highlights', set its url prefix: app.url/highlights
db_setup = Blueprint('dbsetup', __name__)


# Create database instance
db = SQLAlchemy(app)


class Athlete(db.Model):
    """
    Create database table to store Athlete table  data
    """
    __tablename__ = 'Athlete'

    id = db.Column('id', db.Integer, primary_key=True)
    salary = db.Column('salary', db.Integer)
    name = db.Column('name', db.String(100))
    dob = db.Column('dob', db.Date)
    status = db.Column('status', db.String(100))
    placeOfBirth = db.Column('placeOfBirth', db.String(100))
    countryID = db.Column('countryID', db.String(100))
    teamID = db.Column('teamID', db.String, db.ForeignKey('team.teamID'))
    goals = db.Column('goals', db.Integer)
    assists = db.Column('assists', db.Integer)
    wins = db.Column('wins', db.Integer)
    losses = db.Column('losses', db.Integer)
    position = db.Column('position', db.String(50))

    def __init__(self, id, salary, name, dob, status, placeOfBirth, countryID, teamID, goals, assists, wins, losses, position):
        self.id = id
        self.salary = salary
        self.name = name
        self.dob = dob
        self.status = status
        self.placeOfBirth = placeOfBirth
        self.countryID = countryID
        self.teamID = teamID
        self.goals = goals
        self.assists = assists
        self.wins = wins
        self.losses = losses
        self.position = position


class Coach(db.Model):
    __tablename__ = 'Coach'

    id = db.Column('id', db.Integer, primary_key=True)
    salary = db.Column('salary', db.Integer)
    name = db.Column('name', db.String(100))
    dob = db.Column('dob', db.Date)
    status = db.Column('status', db.String(100))
    placeOfBirth = db.Column('placeOfBirth', db.String(100))
    countryID = db.Column('countryID', db.String(100))
    teamID = db.Column('teamID', db.String, db.ForeignKey('team.teamID'))

    def __init__(self, id, salary, name, dob, status, placeOfBirth, countryID, teamID):
        self.id = id
        self.salary = salary
        self.name = name
        self.dob = dob
        self.status = status
        self.placeOfBirth = placeOfBirth
        self.countryID = countryID
        self.teamID = teamID


class Competition(db.Model):
    __tablename__ = 'Competition'

    name = db.Column('name', db.String(100), primary_key=True)
    winner = db.Column('winner', db.String(100))
    comp_type = db.Column('compType', db.String(100))

    def __init__(self, name, winner, type):
        self.name = name
        self.winner = winner
        self.comp_type = type


class Game(db.Model):
    __tablename__ = 'Game'

    score = db.Column('score', db.String(100))
    gameID = db.Column('gameID', db.Integer, primary_key=True)
    winningTeamID = db.Column('winningTeamID', db.Integer, db.ForeignKey('team.teamID'))
    losingTeamID = db.Column('losingTeamID', db.Integer, db.ForeignKey('team.teamID'))
    competitionID = db.Column('competitionID', db.Integer, db.ForeignKey('competition.name'))
    seasonID = db.Column('stadiumID', db.Integer, db.ForeignKey('season.seasonID'))

    def __init__(self, score, gameID, winngingTeamID, losingTeamID, seasonID):
        self.score = score
        self.gameID = gameID
        self.winningTeamID = winngingTeamID
        self.losingTeamID = losingTeamID
        self.seasonID = seasonID


class GameGoal(db.Model):
    __tablename__ = 'GameGoal'

    gameID = db.Column('gameID', db.Integer, db.ForeignKey('game.gameID'), primary_key=True)
    athleteID = db.Column('id', db.Integer, db.ForeignKey('athlete.id'), nullable=False)
    name = db.Column('name', db.String(100))

    def __init__(self, gameID, athleteID, name):
        self.gameID = gameID
        self.athleteID = athleteID
        self.name = name


class Season(db.Model):
    __tablename__ = 'Season'

    seasonID = db.Column('seasonID', db.Integer, primary_key=True)
    location = db.Column('location', db.String(100))

    def __init__(self, seasonID, location):
        self.seasonID = seasonID
        self.location = location


class Stadium(db.Model):
    __tablename__ = 'Stadium'

    name = db.Column('name', db.String(100), primary_key=True)
    location = db.Column('location', db.String(100), primary_key=True)

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Team(db.Model):
    __tablename__ = 'Team'

    teamID = db.Column('teamID', db.String, primary_key=True)
    location = db.Column('location', db.String(100))
    dateCreated = db.Column('dateCreated', db.Date)
    goals = db.Column('goals', db.Integer)
    assists = db.Column('assists', db.Integer)
    wins = db.Column('wins', db.Integer)
    losses = db.Column('losses', db.Integer)

    def __init__(self, teamID, location, dateCreated, goals, assists, wins, losses):
        self.teamID = teamID
        self.location = location
        self.dateCreated = dateCreated
        self.goals = goals
        self.assists = assists
        self.wins = wins
        self.losses = losses