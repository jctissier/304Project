import collections
from sqlalchemy import text


# """ SELECT Query Helpers """
#
#
# def select_athlete_table(data):
#     json_data = collections.OrderedDict({})
#     for i in data:
#         json_data.update({
#             i[0]:
#                 [{
#                     'id': i[0],
#                     'salary': i[1],                     # index of list used is determined by SQL query statement
#                     'name': i[2],                       # athlete.salary = i[1] because it's the second field selected
#                     'dob': i[3],
#                     'status': i[4],
#                     'placeOfBirth': i[5],
#                     'countryID': i[6],
#                     'goals': i[7],
#                     'assists': i[8],
#                     'wins': i[9],
#                     'losses': i[10]
#                 }]
#         })
#
#     return json_data
#
#
# def select_team_table(data):
#     json_data = collections.OrderedDict({})
#     for i in data:
#         json_data.update({
#             i[0]:
#                 [{
#                     'name': i[0],
#                     'location': i[1],
#                     'dateCreated': i[2],
#                     'goals': i[3],
#                     'assists': i[4],
#                     'wins': i[5],
#                     'losses': i[6],
#                 }]
#         })
#
#     return json_data
#
#
# def select_coach_table(data):
#     json_data = collections.OrderedDict({})
#     for i in data:
#         json_data.update({
#             i[0]:
#                 [{
#                     'id': i[0],
#                     'salary': i[1],
#                     'name': i[2],
#                     'dob': i[3],
#                     'placeOfBirth': i[4],
#                     'status': i[5],
#                     'countryID': i[6]
#                 }]
#         })
#
#     return json_data
#
#
# def select_groupby_table(data):
#     json_data = collections.OrderedDict({})
#
#     for num, i in enumerate(data):
#         json_data.update({
#             num:
#                 [{
#                     'Team ID': i[0],
#                     'Number Players': i[1]
#                 }]
#         })
#
#     return json_data
#
#
# """ JOIN Query Helpers """
#
#
# def join_2_query1():
#     """Find all the teams that play in the 2017 edition of the Champions League that have scored at least 5 goals"""
#
#     desired_year = 2017
#     desired_leaguename = "UEFA Champions League"
#     desired_goals = 4
#
#     sql = text('''SELECT distinct t.teamID, t.location, t.dateCreated
#                   FROM Team t, Game g, Competition c, Season s
#                   WHERE g.seasonID = s.seasonID AND g.competitionID = c.competitionID AND
#                         (g.winningTeamID = t.teamID OR g.losingTeamID = t.teamID) AND t.goals > ''' +
#                         str(desired_goals) + ''' AND c.name = "''' + desired_leaguename + '''"''' +
#                         ''' AND s.seasonID = ''' + str(desired_year))
#
#     return sql
#
#
# def join_2_query2():
#     """Find all the players who have scored at least 10 goals and won a trophy in a certain city"""
#
#     desired_goals = 2
#     desired_city = "Europe"
#
#     sql = text('''SELECT distinct a.name, a.teamID, a.status, a.salary
#                   FROM Athlete a, Competition c, Game g, Season s
#                   WHERE c.winner = a.teamID AND g.competitionID = c.competitionID AND g.seasonID = s.seasonID AND
#                         a.goals > ''' + str(desired_goals) + ''' AND s.location = "''' + desired_city + '''"''')
#
#     return sql
#
#
# def join_3_query():
#     """Finds all players from country X who scored at least one goal in a game played in Y city and Z year."""
#     desired_country = "Brazil"
#     desired_gameDest = "Europe"
#     desired_gameYear = 2017
#
#     sql = text('''SELECT distinct a.name, a.teamID, a.status, a.salary
#                   FROM Athlete a, GameGoal gg, Game g, Season s
#                   WHERE a.id = gg.athleteID AND gg.gameID = g.gameID AND s.seasonID = g.seasonID AND a.countryID
#                         LIKE "''' + desired_country + '''"''' + ''' AND s.seasonID = ''' + str(desired_gameYear) +
#                         ''' AND s.location LIKE "''' + desired_gameDest + '''"''')
#
#     return sql
