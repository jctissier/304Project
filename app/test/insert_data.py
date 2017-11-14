from app.db.database import Athlete, Coach, Competition, Game, Season, Stadium, Team, db
from sqlalchemy import text


def insert(query_table):

    if query_table == "Athlete":
        table = 'Athlete (Salary, Name, DOB, Status, placeOfBirth, countryID, goals, assists, wins, losses)'
        vals = 'VALUES (39843, "Robben", "1972-01-30", "Active", "HOL", "GER", 32, 98, 84, 1)'
    elif query_table == "Team":
        table = 'Team (teamID, location, dateCreated, goals, assists, wins, losses)'
        vals = 'VALUES ("Real Madrid", "Spain", "1940-01-01", 93843, 234, 1231, 333)'
    elif query_table == "Coach":
        table = 'Coach (salary, name, dob, status, placeOfBirth, countryID)'
        vals = 'VALUES (8000000, "Zinedine Zidane", "1975-03-01", "Active", "France", "SPN")'
    else:
        exit("This should never happen")

    sql = text('''INSERT INTO ''' + table + vals)
    db.engine.execute(sql)


insert("Athlete")
insert("Coach")
