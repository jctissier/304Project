from flask import Flask, render_template, jsonify, make_response, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import extract
from app.util.util import gzipped
import collections
from datetime import datetime, timedelta
from flask import Blueprint, request, render_template, make_response, jsonify
from app.db.database import Athlete, Coach, Competition, Game, Season, Stadium, Stats, Team, db
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

@queries.route('/set_testDB', methods=['GET', 'POST']) #set data in test db
@gzipped
def set_testDB():
    sql = text('''UPDATE ZeiTracking SET project = "TEST" WHERE project = "TB Database"''')
    result = db.engine.execute(sql)