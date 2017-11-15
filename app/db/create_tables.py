from app.db.database import db

db.engine.execute('''CREATE TABLE Athlete (
                      ID INT,
                      teamID INT , 
                      Salary INT ,
                      Name VARCHAR ,
                      DOB DATE , 
                      Status VARCHAR ,
                      placeOfBirth VARCHAR ,
                      countryID VARCHAR ,
                      Goals INT ,
                      Assists INT ,
                      Wins INT ,
                      Losses INT)''')

db.engine.execute('''CREATE TABLE Coach (
                      ID INT, 
                      Salary INT,
                      Name VARCHAR,
                      DOB DATE, 
                      Status VARCHAR,
                      placeOfBirth VARCHAR,
                      countryID VARCHAR)''')

db.engine.execute('''CREATE TABLE Competition (
                      Name VARCHAR , 
                      Winner VARCHAR)''')

db.engine.execute('''CREATE TABLE Game (
                      Score VARCHAR ,
                      gameID INT ,
                      Round INT ,
                      WinningTeamID INT ,
                      LosingTeamID INT ,
                      competitionID INT ,
                      seasonID INT ,
                      goals INT)''')

db.engine.execute('''CREATE TABLE GameGoal (
                        gameID INT ,
                        athleteID INT)''')

db.engine.execute('''CREATE TABLE Season (
                      SeasonID INT ,
                      Year INT ,
                      Location VARCHAR )''')

db.engine.execute('''CREATE TABLE Stadium (
                      Name VARCHAR ,
                      Location VARCHAR)''')

db.engine.execute('''CREATE TABLE Team (
                      TeamID INT ,
                      Location VARCHAR ,
                      DateCreated DATE ,
                      Goals INT ,
                      Assists INT ,
                      Wins INT ,
                      Losses INT)''')