from flask import Flask, render_template, jsonify, make_response, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import extract
from app.util.util import gzipped
import collections
from datetime import datetime, timedelta
from flask import Blueprint, request, render_template, make_response, jsonify
from app.db.database import Athlete, Coach, Competition, Game, Season, Stadium, Team, db
from sqlalchemy import text


# Define the blueprint: 'queries'
queries = Blueprint('queries', __name__)


@queries.route('/get_athlete_entries', methods=['GET', 'POST'])         # Example
@gzipped
def load_pie():
    data = Athlete.query.all()

    # Number of entries (unique)
    entries = db.session.query(Athlete).count()

    json_data = collections.OrderedDict({})
    for i in data:
        json_data.update({
            i.id:
                [{
                     'id': i.id,
                     'salary': i.salary,
                     'name': i.name,
                     'dob': i.dob,
                     'status': i.status,
                     'placeOfBirth': i.placeOfBirth,
                     'countryID': i.countryID
                }]
            })

    return jsonify({'entries': json_data})

@queries.route('/insert_athlete_entry', methods=['GET', 'POST']) #insert some row, change the sql statement
@gzipped
def set_testDB():
    sql = text('''INSERT INTO Athlete (ID, Salary, Name, DOB, Status, placeOfBirth, countryID, goals, assists, wins, losses) 
                  VALUES (11, 999, "Test Dude9", "2017-9-11", "Retired", "CA", "US", 1, 2, 3, 4)''')
    result = db.engine.execute(sql)

    data = Athlete.query.all()
    # Athlete.query.all()[7].salary
    json_data = collections.OrderedDict({})
    for i in data:
        json_data.update({
                [{
                     'id': i.id,
                     'salary': i.salary,
                     'name': i.name,
                     'dob': i.dob,
                     'status': i.status,
                     'placeOfBirth': i.placeOfBirth,
                     'countryID': i.countryID
                }]
            })

    return jsonify({'entries': json_data})