from flask import Flask, render_template, jsonify, make_response, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import extract
from app.util.util import gzipped
import collections
from dateutil.parser import parse
from datetime import datetime, timedelta
from flask import Blueprint, request, render_template, make_response, jsonify
from app.db.database import ZeiDB, db


# Define the blueprint: 'queries'
queries = Blueprint('queries', __name__)


@queries.route('/get_entries', methods=['GET', 'POST'])         # Example
@gzipped
def load_pie():
    data = ZeiDB.query.all()

    # Number of entries (unique)
    entries = db.session.query(ZeiDB).count()

    json_data = collections.OrderedDict({})
    for i in data:
        json_data.update({
            i.id:
                [{
                     'id': i.id,
                     'zei_id': i.zei_id,
                     'activity_id': i.activity_id,
                     'start': i.start_time,
                     'end': i.end_time,
                     'project': i.project,
                     'duration': i.duration,
                     'notes': i.notes
                }]
            })

    return jsonify({'entries': json_data})
