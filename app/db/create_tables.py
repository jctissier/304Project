from app.db.database import db


def create():

    db.engine.execute('''CREATE TABLE Shooter (
                          sid INT,
                          name VARCHAR)''')

    db.engine.execute('''CREATE TABLE Member (
                          mid INT,
                          sid INT,
                          status VARCHAR,
                          pal VARCHAR,
                          email VARCHAR,
                          ubcID VARCHAR,
                          phone VARCHAR,
                          startDate DATE,
                          endDate DATE)''')

    db.engine.execute('''CREATE TABLE DropIn (
                          did INT ,
                          sid INT)''')

    db.engine.execute('''CREATE TABLE Match (
                          mid INT ,
                          name VARCHAR ,
                          date DATE ,
                          isDQ BOOLEAN)''')

    db.engine.execute('''CREATE TABLE Competitor (
                            sid INT ,
                            mid INT,
                            division VARCHAR)''')

    db.engine.execute('''CREATE TABLE Stage (
                          stageid INT ,
                          mid INT ,
                          s1 NUMERIC ,
                          s2 NUMERIC ,
                          s3 NUMERIC ,
                          s4 NUMERIC ,
                          s5 NUMERIC)''')

    print("Tables have been created\n")
