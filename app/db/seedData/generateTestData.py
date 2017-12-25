from app.db.database import Shooter, Member, DropIn, Match, Competitor, Stage, db
from sqlalchemy import Column, Integer, Float, Date, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
import random
import pandas as pd
from app.db.enums import Status, Pal, Division
import time
from datetime import date, datetime, timedelta

rowNumbers = 5


def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.
    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y', prop)

def make():
    data = json.load(open('names.json'))
    seedSize = len(data)
    print("Size of name seed input: " + str(seedSize))

    shooters = pd.DataFrame()
    members = pd.DataFrame()
    dropIn = pd.DataFrame()

    shooters_names = []
    shooters_sid = [] #foreignKey
    members_mid = []
    members_status = []
    members_email = []
    members_ubcID = []
    members_phone = []
    members_startDate = []
    members_endDate = []
    dropIn_did = []

    for x in range(rowNumbers):
        i = random.randint(0, seedSize)
        name = data[i]
        shooters_names.append(name)
        shooters_sid.append(random.randint(0, seedSize))

        if random.random() < 100:
            members_mid.append(random.randint(0, seedSize))
            members_status.append(random.choice(list(Status)).name)
            members_email.append(name + "@gmail.com")
            members_ubcID.append(random.randint(10000000, 99999999))
            members_phone.append(random.randint(1000000000, 9999999999))
            startTimeStr = randomDate("1/1/2014", "1/1/2016", random.random())
            startTimeDate = datetime.strptime(startTimeStr, '%m/%d/%Y')
            members_startDate.append(startTimeStr)
            endTimeDate = startTimeDate + timedelta(days=360)
            endTimeDateStr = (endTimeDate.date().strftime('%m/%d/%Y'))
            members_endDate.append(endTimeDateStr)

        else:
            dropIn_did.append(random.randint(0, seedSize))

    shooters['name'] = shooters_names
    shooters['sid'] = shooters_sid

    members['mid'] = members_mid
    members['sid'] = shooters['sid']
    members['status'] = members_status
    members['email'] = members_email
    members['ubcID'] = members_ubcID
    members['phone'] = members_phone
    members['startDate'] = members_startDate
    members['endDate'] = members_endDate
    dropIn['did'] = dropIn_did
    dropIn['sid'] = shooters['sid']

    print(shooters)
    print(members)
    print(dropIn)



def toSqlTable(shooter, member, dropin, match, competitor, stage):
    shooter.to_sql(con=db.engine, name=Shooter.__tablename__, if_exists='replace')
    # member.to_sql(con=db.engine, name=Member.__tablename__, if_exists='replace')
    # dropin.to_sql(con=db.engine, name=DropIn.__tablename__, if_exists='replace')
    # match.to_sql(con=db.engine, name=Match.__tablename__, if_exists='replace')
    # competitor.to_sql(con=db.engine, name=Competitor.__tablename__, if_exists='replace')
    # stage.to_sql(con=db.engine, name=Stage.__tablename__, if_exists='replace')


make()
print("Finished generating test data")