from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
import enums
from app import app


# Define the blueprint: 'highlights', set its url prefix: app.url/highlights
db_setup = Blueprint('dbsetup', __name__)


# Create database instance
db = SQLAlchemy(app)


class Shooter(db.Model):
    """
    Create database table to store Shooter table data
    Shooter ISA Member or DropIn
    """
    __tablename__ = 'Shooter'

    sid = db.Column('sid', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100), nullable=False)

    def __init__(self, sid, name):
        self.sid = sid
        self.name = name


class Member(db.Model):
    """
    ISA Shooter
    """
    __tablename__ = 'Member'

    mid = db.Column('mid', db.Integer, primary_key=True)
    sid = db.Column('sid', db.Integer, db.ForeignKey('Shooter.sid'))
    status = db.Column('status', db.Enum(enums.Status), nullable=False)
    pal = db.Column('pal', db.Enum(enums.Pal), nullable=False)
    email = db.Column('email', db.String(100))
    ubcID = db.Column('UBCid', db.String(15)) #no need to pad 0s
    phone = db.Column('phone', db.String(15)) #international numbers, no need to pad 0s
    startDate = db.Column('startDate', db.Date, nullable=False)
    endDate = db.Column('endDate', db.Date)

    def __init__(self, mid, sid, status, pal, email, ubcID, phone, startDate, endDate):
        self.mid = mid
        self.sid = sid
        self.status = status
        self.pal = pal
        self.email = email
        self.ubcID = ubcID
        self.phone = phone
        self.startDate = startDate
        self.endDate = endDate


class DropIn(db.Model):
    """
    ISA Shooter
    """
    __tablename__ = 'DropIn'

    did = db.Column('did', db.Integer, primary_key=True)
    sid = db.Column('sid', db.Integer, db.ForeignKey('Shooter.sid'))

    def __init__(self, did, sid):
        self.did = did
        self.sid = sid


class Match(db.Model):
    __tablename__ = 'Match'

    mid = db.Column('mid', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100), nullable=False)
    date = db.Column('date', db.Date, nullable=False)
    isDQ = db.Column('isDQ', db.Boolean, nullable=False)

    def __init__(self, mid, name, date, isDQ):
        self.mid = mid
        self.name = name
        self.date = date
        self.isDQ = isDQ


class Competitor(db.Model):
    __tablename__ = 'Competitor'

    sid = db.Column('sid', db.Integer, db.ForeignKey('Shooter.sid'), primary_key=True)
    mid = db.Column('mid', db.Integer, db.ForeignKey('Match.id'), primary_key=True)
    division = db.Column('division', db.Enum(enums.Division), nullable=False)

    def __init__(self, sid, mid, division):
        self.sid = sid
        self.mid = mid
        self.division = division


class Stage(db.Model):
    __tablename__ = 'Stage'

    stageid = db.Column('stageid', db.Integer, primary_key=True)
    mid = db.Column('mid', db.ForeignKey(Match.mid), primary_key=True)
    s1 = db.Column('s1', db.Numeric) #need to support to 2 decimal spaces example: 5.23s
    s2 = db.Column('s2', db.Numeric)
    s3 = db.Column('s3', db.Numeric)
    s4 = db.Column('s4', db.Numeric)
    s5 = db.Column('s5', db.Numeric)

    def __init__(self, stageid, mid, s1, s2, s3, s4, s5):
        self.stageid = stageid
        self.mid = mid
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5