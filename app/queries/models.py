import collections


"""SELECT Query Helpers """


def select_athlete_table(data):
    json_data = collections.OrderedDict({})
    for i in data:
        json_data.update({
            i[0]:
                [{
                    'salary': i[1],                     # index of list used is determined by SQL query statement
                    'name': i[2],                       # athlete.salary = i[1] because it's the second field selected
                    'dob': i[3],
                    'status': i[4],
                    'placeOfBirth': i[5],
                    'countryID': i[6],
                    'goals': i[7],
                    'assists': i[8],
                    'wins': i[9],
                    'losses': i[10]
                }]
        })

    return json_data


def select_team_table(data):
    json_data = collections.OrderedDict({})
    for i in data:
        json_data.update({
            i[0]:
                [{
                    'name': i[1],
                    'location': i[2],
                    'dateCreated': i[3],
                    'goals': i[4],
                    'assists': i[5],
                    'wins': i[6],
                    'losses': i[7],
                }]
        })

    return json_data


def select_coach_table(data):
    json_data = collections.OrderedDict({})
    for i in data:
        json_data.update({
            i[0]:
                [{
                    'salary': i[1],
                    'name': i[2],
                    'dob': i[3],
                    'status': i[4],
                    'placeOfBirth': i[5],
                    'countryID': i[6]
                }]
        })

    return json_data


def select_groupby_table(data):
    json_data = collections.OrderedDict({})
    for i in data:
        json_data.update({
            i[0]:
                [{
                    'Team ID': i[1],
                    'Number Players': i[2],
                }]
        })

    return json_data


"""INSERT Query Helpers """

