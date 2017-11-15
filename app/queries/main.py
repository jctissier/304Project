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
        a_sql = text('''SELECT Athlete.id, Athlete.salary, Athlete.name, Athlete.dob, Athlete.status, Athlete.placeOfBirth,
                        Athlete.countryID, Athlete.goals, Athlete.assists, Athlete.wins, Athlete.losses
                        FROM Athlete''')
        data = db.engine.execute(a_sql)
        a_data = [list(row) for row in data]                # Python list comprehension
        json_data = helper.select_athlete_table(data=a_data)
    elif select_table == "Team":                            # Query Team table
        a_sql = text('''SELECT Team.TeamID, Team.location, Team.dateCreated, Team.goals,
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

    # Athlete fields
    a_name = request.form['a_name']
    a_status = request.form['a_status']
    # Team fields
    t_name = request.form['t_name']
    t_loc = request.form['t_location']

    if insert_table == "Athlete":
        table = 'Athlete (Salary, Name, DOB, Status, placeOfBirth, countryID, goals, assists, wins, losses)'
        vals = 'VALUES (999999, "' + a_name + '", "1970-01-05", "' + a_status + '", "Canada", "Canada", 15, 10, 10, 0)'
    elif insert_table == "Team":
        table = 'Team (teamID, location, dateCreated, goals, assists, wins, losses)'
        vals = 'VALUES ("' + t_name + '", "' + t_loc + '", "2018", 168, 153, 55, 20)'
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
        last_vals = [[r.teamID, r.location, r.dateCreated, r.goals, r.assists, r.wins, r.losses] for r in row]

    return jsonify({
        'query_type': 'INSERT',
        'table': insert_table,
        'Code': 200,
        'last_5_rows': last_vals
    })


""" DELETE QUERIES """


@queries.route('/delete_query', methods=['GET', 'POST'])
@gzipped
def delete_query():
    """Delete from Stadium or Team"""

    delete_table = request.form['table_name']

    # Stadium fields
    s_name = request.form['s_name']
    s_location = request.form['s_location']
    # Team fields
    t_name = request.form['t_name']

    if delete_table == "Stadium":
        sql = text('''DELETE FROM Stadium WHERE name = ''' + s_name + ''' AND location = ''' + s_location)
    elif delete_table == "Team":
        sql = text('''DELETE FROM Team WHERE teamID = ''' + t_name)
    else:
        return jsonify({'error': "Invalid Table Name"})

    # db.engine.execute(sql)
    print(sql)

    return jsonify({
        'query_type': 'DELETE',
        'table': delete_table,
        'Code': 200
    })


""" UPDATE QUERIES """


@queries.route('/update_player_stats', methods=['GET', 'POST'])
@gzipped
def update_player_stats():
    """updates the stats of a certain player"""

    goals = 10
    assists = 12
    wins = 50
    losses = 50
    main_pk = 1000

    sql = text('''UPDATE Player SET goals = ''' + goals + ''', assists = ''' + assists
               + ''', wins = ''' + wins + ''', losses = ''' + losses + ''' WHERE id = ''' + main_pk)

    db.engine.execute(sql)

    return jsonify({
        'query_type': 'UPDATE',
        'table': "Athlete",
        'Code': 200
    })


@queries.route('/update_player_country', methods=['GET', 'POST'])
@gzipped
def update_player_country():
    """Update the country of a certain player."""

    main_pk = 5000
    new_country = "Congo"

    sql = text('''UPDATE Player Set countryID = ''' + new_country + ''' WHERE id = +''' + main_pk)

    db.engine.execute(sql)

    return jsonify({
        'query_type': 'UPDATE',
        'table': "Athlete",
        'Code': 200
    })


@queries.route('/groupby_query', methods=['GET', 'POST'])
@gzipped
def groupby_query():
    """Find the number of players in each club team who are not born in the country the club is located in"""

    sql = text('''SELECT t.teamID, count(*) FROM Athlete a, Team t
                  WHERE a.teamID = t.teamID AND t.location <> a.countryID
                  GROUP BY t.teamID''')

    data = db.engine.execute(sql)
    a_data = [list(row) for row in data]
    print(a_data)

    return jsonify({'entries': helper.select_groupby_table(data=a_data)})
