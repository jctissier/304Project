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
        exit("This should never happen. ")

    return jsonify({'entries': json_data})


@queries.route('/join_3_query', methods=['GET', 'POST'])
@gzipped
def join_3_query():
    """Finds all players from country X who scored at least one goal
    in a game played in Y city and Z year."""
    desired_country = "Brazil"
    desired_gameDest = "Paris"
    desired_gameYear = "Year"

    sql = text('''SELECT * FROM Athlete a, GameGoal gg, Game g, Season s WHERE 
            a.id = gg.athleteID AND gg.gameID = g.gameID AND s.seasonID = g.seasonID AND a.countryID = ''' + desired_country +
               ''' AND s.year = ''' + desired_gameYear + ''' AND s.location = ''' + desired_gameDest)

    data = db.engine.execute(sql)
    a_data = [list(row) for row in data]

    return jsonify({'entries': helper.select_athlete_table(data=a_data)})

""" INSERT QUERIES """


@queries.route('/insert_query', methods=['GET', 'POST'])
@gzipped
def insert_query():
    """Athlete, Team or Coach"""

    query_table = "Athlete"

    if query_table == "Athlete":
        table = 'Athlete (Salary, Name, DOB, Status, placeOfBirth, countryID, goals, assists, wins, losses)'
        vals = 'VALUES (39843, "Robben", "1972-01-30", "Active", "HOL", "GER", 32, 98, 84, 1)'
    elif query_table == "Team":
        table = 'Team (name, location, dateCreated, goals, assists, wins, losses)'
        vals = 'VALUES ()'
    elif query_table == "Coach":
        table = 'Coach (salary, name, dob, status, placeOfBirth, countryID)'
        vals = 'VALUES ()'
    else:
        return jsonify({'error': "Invalid Table Name"})

    sql = text('''INSERT INTO ''' + table + vals)
    db.engine.execute(sql)                                      # Runs the SQL INSERT

    return jsonify({
        'query_type': 'INSERT',
        'table': query_table,
        'Code': 200
    })


""" DELETE QUERIES """


@queries.route('/delete_query', methods=['GET', 'POST'])
@gzipped
def delete_query():
    """can delete from any table"""
    """Athlete, Coach, Competition, Game, Season, Stadium, or Team"""

    query_table = "placeholder for table selected"
    main_pk = "placeholder for pk insert field"

    if query_table == "Athlete":
        sql = text('''DELETE FROM Athlete WHERE id = ''' + main_pk)
    elif query_table == "Coach":
        sql = text('''DELETE FROM Coach WHERE id = ''' + main_pk)
    elif query_table == "Competition":
        sql = text('''DELETE FROM Competition WHERE name = ''' + main_pk)
    elif query_table == "Game":
        sql = text('''DELETE FROM Game WHERE gameID = ''' + main_pk)
    elif query_table == "Season":
        sql = text('''DELETE FROM Season WHERE seasonID = ''' + main_pk)
    elif query_table == "Stadium":
        composite_pk_additional = "placeholder for composite fields"
        sql = text('''DELETE FROM Stadium WHERE name = ''' + main_pk + ''' AND location = ''' + composite_pk_additional)
    elif query_table == "Team":
        sql = text('''DELETE FROM Team WHERE teamID = ''' + main_pk)
    else:
        return jsonify({'error': "Invalid Table Name"})

    db.engine.execute(sql)

    return jsonify({
        'query_type': 'DELETE',
        'table': query_table,
        'Code': 200
    })

""" UPDATE QUERIES """


@queries.route('/update_player', methods=['GET', 'POST'])
@gzipped
def update_player():
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




