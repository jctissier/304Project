from flask import Blueprint, request, render_template, make_response, jsonify

from app.util.util import gzipped
from app.db.database import Athlete, Coach, Competition, Game, Season, Stadium, Team, db


# Define the blueprint: 'sunburst'
sunburst = Blueprint('sunburst', __name__)


@sunburst.route('/')
@sunburst.route('/dashboard')
@gzipped
def dashboard():
    return render_template('dashboard.html')


@sunburst.route('/load_sunburst', methods=['GET'])
@gzipped
def load_sunburst():
    data = db.query.all()

    return data
