from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from app import app


"""
TODO
    -Set clear objectives
    -Define mission and what is the tracking related to
    -Expected time vs completion time

"""

# Define the blueprint: 'highlights', set its url prefix: app.url/highlights
db_setup = Blueprint('dbsetup', __name__)


# Create database instance
db = SQLAlchemy(app)


class ZeiDB(db.Model):
    """
    Create database table to store Zei data
    """
    __tablename__ = 'ZeiTracking'

    id = db.Column(db.Integer, primary_key=True)
    zei_id = db.Column('zei_id', db.Integer, unique=True)
    start_time = db.Column('start_time', db.DateTime)
    end_time = db.Column('end_time', db.DateTime)
    project = db.Column('project', db.String(100))
    activity_id = db.Column('activity_id', db.Integer)
    duration = db.Column('duration', db.Integer)
    notes = db.Column('notes', db.String(1000))

    def __init__(self, zei_id, start_time, end_time, project, a_id, duration, notes):
        self.zei_id = zei_id                # Unique Tracking ID
        self.start_time = start_time
        self.end_time = end_time
        self.project = project
        self.activity_id = a_id             # Zei activity ID
        self.duration = duration
        self.notes = notes
