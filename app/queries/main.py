from app.util.util import gzipped
import collections
from flask import Blueprint, request, render_template, jsonify
from app.db.database import Athlete, Coach, Competition, Game, Season, Stadium, Team, db
from sqlalchemy import text
import app.queries.models as helper


# Define the blueprint: 'queries'
queries = Blueprint('queries', __name__)


@queries.route('/')
@gzipped
def load():
    """
    Loads the HTML template
    """
    return render_template("dashboard.html")


""" SELECT QUERIES """


@queries.route('/select_query', methods=['GET', 'POST'])         # Example
@gzipped
def select_athlete():
    """
    SELECT queries from table: Athlete, Team or Coach
    :return: JSON{} - entries in table
    """
    select_table = request.form['table_name']

    if select_table == "Athlete":                           # Query Athlete table
        a_sql = text('''SELECT athlete.id, athlete.salary, athlete.name, athlete.dob, athlete.status, athlete.placeOfBirth,
                        athlete.countryID, athlete.goals, athlete.assists, athlete.wins, athlete.losses
                        FROM Athlete''')
        data = db.engine.execute(a_sql)
        a_data = [list(row) for row in data]                # Python list comprehension
        """
        Example of how the data extract looks like for Athlete
            [[1, 123000, 'Edward C', '1991-05-24', 'Active', 'CA', 'CA', None, None, None, None],
            [5, 999, 'Test Dude3', '2017-9-11', 'Retired', 'CA', 'US', None, None, None, None],
            [6, 999, 'Test Dude4', '2017-9-11', 'Retired', 'CA', 'US', None, None, None, None],
            [7, 999, 'Test Dude5', '2017-9-11', 'Retired', 'CA', 'US', None, None, None, None]]
        """
        json_data = helper.select_athlete_table(data=a_data)
    elif select_table == "Team":                            # Query Team table
        a_sql = text('''SELECT Team.TeamID, Team.name, Team.location, Team.dateCreated, Team.goals,
                        Team.assists, Team.wins, Team.losses
                        FROM Team''')
        data = db.engine.execute(a_sql)
        t_data = [list(row) for row in data]
        json_data = helper.select_team_table(data=t_data)
    elif select_table == "Coach":                           # Query Coach table
        a_sql = text('''SELECT Coach.id, Coach.salary, Coach.name, Coach.dob, Coach.status, Coach.placeOfBirth,
                        Coach.countryID
                        FROM Coach''')
        data = db.engine.execute(a_sql)
        c_data = [list(row) for row in data]  # Python list comprehension
        json_data = helper.select_coach_table(data=c_data)
    else:
        exit("This should never happen")

    return jsonify({'entries': json_data})


""" INSERT QUERIES """


@queries.route('/insert_query', methods=['GET', 'POST'])
@gzipped
def insert_query():
    """Athlete, Team or Coach"""
    insert_table = request.form['table_name']

    if insert_table == "Athlete":
        a_name = request.form['a_name']
        a_status = request.form['a_status']
    elif insert_table == "Team":
        t_name = request.form['t_name']
        t_loc = request.form['t_location']

    if insert_table == "Athlete":
        table = 'Athlete (Salary, Name, DOB, Status, placeOfBirth, countryID, goals, assists, wins, losses)'
        vals = 'VALUES (1000000, "' + a_name + '", "1970-01-05", "' + a_status + '", "CAN", "CAN", 15, 10, 10, 0)'
    elif insert_table == "Team":
        table = 'Team (name, location, dateCreated, goals, assists, wins, losses)'
        vals = 'VALUES ("' + t_name + '", "' + t_loc + '", "2018-01-01", 168, 153, 55, 20)'
    else:
        return jsonify({'error': "Invalid Table Name"})

    sql = text('''INSERT INTO ''' + table + vals)
    db.engine.execute(sql)                                      # Runs the SQL INSERT

    if insert_table == "Athlete":
        row = db.session.query(Athlete).order_by(Athlete.id.desc()).limit(5).all()
        last_vals = [[r.id, r.salary, r.name, r.dob, r.status, r.placeOfBirth, r.countryID, r.goals, r.assists, r.wins, r.losses]
                     for r in row]
    elif insert_table == "Team":
        row = db.session.query(Team).order_by(Team.teamID.desc()).limit(5).all()
        last_vals = [[r.teamID, r.name, r.location, r.dateCreated, r.goals, r.assists, r.wins, r.losses] for r in row]

    return jsonify({
        'query_type': 'INSERT',
        'table': insert_table,
        'Code': 200,
        'last_5_rows': last_vals
    })
