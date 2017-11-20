from app.db.database import Athlete, Coach, Competition, Game, Season, Stadium, Team, db
from sqlalchemy import text
from sqlite3 import OperationalError


def insert(query_table):

    if query_table == "Athlete":
        table = 'Athlete (Salary, Name, DOB, Status, placeOfBirth, countryID, goals, assists, wins, losses)'
        vals = 'VALUES (39843, "Robben", "1972-01-30", "Active", "HOL", "GER", 32, 98, 84, 1)'
    elif query_table == "Team":
        table = 'Team (name, location, dateCreated, goals, assists, wins, losses)'
        vals = 'VALUES ("Real Madrid", "Spain", "1940-01-01", 93843, 234, 1231, 333)'
    elif query_table == "Coach":
        table = 'Coach (salary, name, dob, status, placeOfBirth, countryID)'
        vals = 'VALUES (8000000, "Zinedine Zidane", "1975-03-01", "Active", "France", "SPN")'
    else:
        exit("This should never happen")

    sql = text('''INSERT INTO ''' + table + vals)
    db.engine.execute(sql)


# insert("Coach")

def get_table_columns():                    # Gets the names of each Table's columns
    print(Athlete.__table__.columns.keys())

# get_table_columns()


def delete_data():
    # TODO - Show count to show that it was deleted - remove table and re-render
    # TODO - show deletes for first 3 - easiest way to show
    key_name = "Allianz Arena "
    key_location = "Munich, Germany"

    # key_name = "Allianz Riviera "
    # key_location = "Nice, France"

    sql = text('''DELETE FROM Stadium WHERE name = "''' + key_name + '''" AND location = "''' + key_location + '"')
    db.engine.execute(sql)

    row = db.session.query(Stadium).all()
    for r in row:
        print(r)

# delete_data()             # Uncomment to run function


def update_data():
    main_pk = 238           # Lionel Messi = 238 id

    sql = text('''UPDATE Athlete SET salary=999999 WHERE name="Lionel Messi" AND id=238''')              # shouldnt be a string
    db.engine.execute(sql)

    lionel_update = db.session.query(Athlete).get(main_pk)
    print(lionel_update.salary)

# update_data()             # Uncomment to run function


# print(db.session.query(Team).order_by(Team.teamID.desc()).all())
# print(db.session.query(Athlete).order_by(Athlete.id.desc()).first())
# print(db.session.query(Team).order_by(Team.teamID.desc()).limit(5).all())


def get_any_table(t_name):
    sql = text('''SELECT * FROM ''' + t_name)  # shouldnt be a string
    rows = db.engine.execute(sql)
    data = [list(row) for row in rows]

    print(data)

# get_any_table("Team")



def join_2_query2():
    """Find all the players who have scored at least 10 goals and won a trophy in a certain city. d """

    desired_goals = 2
    desired_city = "Europe"

    sql = text('''SELECT distinct a.name, a.teamID, a.status, a.salary FROM Athlete a, Competition c, Game g, Season s WHERE c.winner = a.teamID AND
                      g.competitionID = c.competitionID AND g.seasonID = s.seasonID AND a.goals > ''' + str(desired_goals) + ''' AND
                      s.location = "''' + desired_city + '''"''')

    data = db.engine.execute(sql)
    a_data = [list(row) for row in data]
    print(a_data)


def join_3_query():
    """Finds all players from country X who scored at least one goal in a game played in Y city and Z year."""
    desired_country = "Brazil"
    desired_gameDest = "Europe"
    desired_gameYear = 2017

    sql = text('''SELECT distinct a.name, a.teamID, a.status, a.salary FROM Athlete a, GameGoal gg, Game g, Season s WHERE
            a.id = gg.athleteID AND gg.gameID = g.gameID AND s.seasonID = g.seasonID AND a.countryID LIKE "''' + desired_country + '''"'''
               ''' AND s.seasonID = ''' + str(desired_gameYear) + ''' AND s.location LIKE "''' + desired_gameDest + '''"''')

    data = db.engine.execute(sql)
    a_data = [list(row) for row in data]
    print(a_data)


def join_2_query1():
    """Find all the teams that play in the 2017 edition of the Champions League that have scored at least 5 goals"""

    desired_year = 2017
    desired_leaguename = "UEFA Champions League"
    desired_goals = 4

    sql = text('''SELECT distinct t.teamID, t.location, t.dateCreated FROM Team t, Game g, Competition c, Season s WHERE
          g.seasonID = s.seasonID AND g.competitionID = c.competitionID AND
          (g.winningTeamID = t.teamID OR g.losingTeamID = t.teamID) AND t.goals > ''' +
               str(desired_goals) + ''' AND c.name = "''' + desired_leaguename + '''"''' +
               ''' AND s.seasonID = ''' + str(desired_year))

    data = db.engine.execute(sql)
    a_data = [list(row) for row in data]
    print(a_data)


# join_2_query1()
# join_3_query()
# join_2_query2()

def createview():
    """Manager view - only care about player stats and position played. Name, age (DOB), place of birth
        & salary should not be accounted for when making team play decisions.
    """

    tb_exists = "SELECT count(*) FROM sqlite_master WHERE type='view' AND name='AthletePerformanceView'"
    row = db.engine.execute(tb_exists)
    if str(row.fetchone()) == '(1,)':
        print("Create View already created")

    else:
        sql = text('''CREATE VIEW AthletePerformanceView AS
                    SELECT Athlete.Goals, Athlete.Assists, Athlete.Wins, Athlete.Losses, Athlete.Position
                    FROM Athlete''')
        db.engine.execute(sql)

    qry_view = text('''SELECT * FROM AthletePerformanceView''')
    rows = db.engine.execute(qry_view)
    a_data = [list(row) for row in rows]
    print(a_data)

# createview()


def insert_new():
    t_name = "Test"
    t_loc = "France"
    table = 'Team (teamID, location, dateCreated, goals, assists, wins, losses)'
    vals = 'VALUES ("' + t_name + '", "' + t_loc + '", "2018-01-01", 168, 153, 55, 20)'

    row = db.session.query(Team).filter_by(teamID=t_name).count()
    print(row)
    # sql = text('''INSERT INTO ''' + table + vals)
    # db.engine.execute(sql)

insert_new()
