import collections


"""SELECT Query Helpers """


def select_athlete_table(data):
    json_data = collections.OrderedDict({})
    for i in data:
        json_data.update({
            i[0]:
                [{
                    'id': i[0],
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
                    'name': i[0],
                    'location': i[1],
                    'dateCreated': i[2],
                    'goals': i[3],
                    'assists': i[4],
                    'wins': i[5],
                    'losses': i[6],
                }]
        })

    return json_data


def select_coach_table(data):
    json_data = collections.OrderedDict({})
    for i in data:
        json_data.update({
            i[0]:
                [{
                    'id': i[0],
                    'salary': i[1],
                    'name': i[2],
                    'dob': i[3],
                    'placeOfBirth': i[4],
                    'status': i[5],
                    'countryID': i[6]
                }]
        })

    return json_data


def select_groupby_table(data):
    json_data = collections.OrderedDict({})

    for num, i in enumerate(data):
        json_data.update({
            num:
                [{
                    'Team ID': i[0],
                    'Number Players': i[1]
                }]
        })

    return json_data


"""INSERT Query Helpers """

