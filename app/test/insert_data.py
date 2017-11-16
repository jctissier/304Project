from app.db.database import Athlete, Coach, Competition, Game, Season, Stadium, Team, db
from sqlalchemy import text


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

    sql = text('''UPDATE Athlete SET salary=999999 WHERE name="Lionel Messi"''')              # shouldnt be a string
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

get_any_table("Team")
