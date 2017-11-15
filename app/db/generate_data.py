#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:45:01 2017

@author: Isaac
"""

import pandas as pd
import random
import numpy as np
from datetime import datetime
from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


stadiums = pd.read_csv('dataSeed/stadiums.csv')
locations = [stadiums['City'][i].strip() + ', ' + stadiums['Country'][i].strip() for i in range(len(stadiums))]
stadiums['Team'] = stadiums['Team'].apply(lambda x: x.strip())
stadiums['Location'] = locations
stadiums_filtered = stadiums[['Stadium', 'Location']]
stadiums_filtered.columns = ['name', 'location']
countriesPopulation = pd.read_csv('dataSeed/countriesPopulation.csv')
playersData = pd.read_csv('dataSeed/players.csv')
players = playersData



nationalities = ['Brazil', 'Argentina', 'Colombia', 'France', 'Italy', 'Spain', 'Germany', 'England', 'Portugal',
                 'Ivory Coast', 'Nigeria', 'Japan', 'United States']
continents = ['South America', 'South America', 'South America', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe',
              'Europe', 'Africa', 'Africa', 'Asia', 'North America']

population = []
for nationality in nationalities:
    pop = countriesPopulation[countriesPopulation['Country Name'] == nationality]['2016']
    pop = pop.astype(int).tolist()
    if len(pop) == 0:
        print(nationality)
        population.append(55000000)
    else:
        population.append(pop[0])

population[9] = 23000000

countries = pd.DataFrame()
random.seed(17)
countryIDs = random.sample(range(1, len(nationalities) + 1), len(nationalities))
countries['id'] = nationalities
countries['population'] = population
countries['continent'] = continents
countries['activePlayerCount'] = np.zeros(len(nationalities))

nationalTeam = pd.DataFrame()
nationalTeam['teamID'] = nationalities
nationalTeam['location'] = nationalities
nationalTeam['dateCreated'] = 'N/A'
nationalTeam['goals'] = 0
nationalTeam['assists'] = 0
nationalTeam['wins'] = 0
nationalTeam['losses'] = 0

clubs_of_interest = ['Real Madrid', 'FC Barcelona', 'Manchester Utd', 'Manchester City', 'FC Bayern', 'Chelsea',
                     'Juventus', 'PSG', 'Arsenal', 'Spurs', 'Atlético Madrid', 'Bor. Dortmund', 'Inter', 'Liverpool']

club_locations = ['Madrid, Spain', 'Barcelona, Spain', 'Manchester, England', 'Manchester, England', 'Munich, Germany',
                  'London, England', 'Turin, Italy', 'Paris, France', 'London, England', 'London, England',
                  'Madrid, Spain', 'Dortmund, Germany', 'Milan, Italy', 'Liverpool, England']
clubIDs = random.sample(range(len(nationalities) + 1, len(nationalities) + len(clubs_of_interest) + 1),
                        len(clubs_of_interest))

random.seed(175)
date_created = random.sample(range(1890, 1920), len(clubs_of_interest))
teamIDs = clubIDs + countries['id'].tolist()
rows = [players['Nationality'][i] in nationalities and players['Club'][i] in clubs_of_interest for i in
        range(len(players))]
athletes = players[rows]
random.seed(76)
athletesIDs = random.sample(range(1, len(athletes) + 1), len(athletes))
athletes['id'] = athletesIDs
athletes['teamID'] = [clubs_of_interest[clubs_of_interest.index(athletes['Club'][i])] for i in athletes.index]
athletes['countryID'] = [nationalities[nationalities.index(athletes['Nationality'][i])] for i in athletes.index]
athletes['dob'] = [datetime.strptime(athletes['Birth_Date'][i], '%m/%d/%Y').date() for i in athletes.index]
athletes['status'] = 'Active'
athletes['goals'] = 0
athletes['assists'] = 0
athletes['wins'] = 0
athletes['losses'] = 0
athletes['placeOfBirth'] = athletes['countryID']
athletes['salary'] = [np.random.choice(range(1, 4)) * 10000000 if i < 30 else np.random.choice(range(1, 400)) * 10000
                      for i in athletes.index]
athletes = athletes[
    ['id', 'salary', 'Name', 'dob', 'status', 'placeOfBirth', 'countryID', 'teamID', 'goals', 'assists', 'wins',
     'losses', 'Club_Position']]
athletes.columns = ['id', 'salary', 'name', 'dob', 'status', 'placeOfBirth', 'countryID', 'teamID', 'goals', 'assists',
                    'wins', 'losses', 'position']

athletes.at[284, 'status'] = 'Retired'
athletes.at[385, 'status'] = 'Retired'
athletes.at[28, 'status'] = 'Retired'
atheletes = athletes.head(15)
clubs = pd.DataFrame()
clubs['teamID'] = clubs_of_interest
clubs['location'] = club_locations
clubs['dateCreated'] = date_created
clubs['goals'] = 0
clubs['assists'] = 0
clubs['wins'] = 0
clubs['losses'] = 0

countries['activePlayerCount'] = [np.sum(athletes['countryID'] == countries['id'][i]) for i in countries.index]

coaches_of_interest = ['Zinedine Zidane', 'Ernesto Valverde', 'Jose Mourinho', 'Pep Guardiola', 'Jupp Heynckes',
                       'Antonio Conte', 'Max Allegri', 'Unai Emery', 'Arsene Wenger', 'Mauricio Pocchetino',
                       'Diego Simeone', 'Peter Bosz', 'Luciano Spaletti', 'Jurgen Klopp',
                       'Tite', 'Jorge Sampaoli', 'Jose Pekerman', 'Didier Deschamps', 'Gian Piero Ventura',
                       'Julen Lopetegui', 'Joachim Low', 'Gareth Southgate', 'Fernando Santos', 'Marc Wilmots',
                       'Gernot Rohr', 'Vahid Halilodzic', 'Dave Sarachan']

coaches_nationalities = ['France', 'Spain', 'Portugal', 'Spain', 'Germany', 'Italy', 'Italy', 'Spain', 'France',
                         'Argentina', 'Argentina', 'Netherlands', 'Italy', 'Germany', 'Brazil', 'Argentina',
                         'Argentina', 'France', 'Italy', 'Spain', 'Germany', 'England', 'Portugal', 'Belgium',
                         'Germany', 'Bosnia', 'USA']

import random
import time


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

#   Range below 1970 throws error with Windows when running script
coaches_dob = [randomDate("1/1/1971", "1/1/1980", random.random()) for i in range(len(coaches_of_interest))]
teams = clubs_of_interest + nationalities
coaches = pd.DataFrame()
coachIDs = random.sample(range(len(athletes) + 1, len(athletes) + len(coaches_of_interest) + 1),
                         len(coaches_of_interest))
coaches['id'] = coachIDs
coaches['salary'] = [np.random.choice(range(1, 10)) * 1000000 for i in range(len(coaches))]
coaches['name'] = coaches_of_interest
coaches['dob'] = coaches_dob
coaches['status'] = 'Active'
coaches['placeOfBirth'] = coaches_nationalities
coaches['countryID'] = coaches_nationalities
coaches['teamID'] = teams



competition = pd.DataFrame()
competition['name'] = ['UEFA Champions League', 'UEFA Champions League', 'FIFA World Cup', 'FIFA World Cup']
competition['year'] = ['2016', '2017', '2014', '2018']
competition['type'] = ['club', 'club', 'international', 'international']

season = pd.DataFrame()
season['seasonID'] = competition['year']

gameGoal = pd.DataFrame()
gameGoal['gameID'] = []
gameGoal['athleteID'] = []
gameGoal['name'] = []
gameIDs = []


def generateCompetitiveMatches(teams, competition, num_games=20):
    matches_team1 = []
    matches_team2 = []
    matches_team1ID = []
    matches_team2ID = []
    scores = []
    winners = []
    losers = []
    seasonID = []
    locations = []
    competitionID = []
    gameCompetitionID = []
    teamGoals = np.zeros(len(teams))
    teamAssists = np.zeros(len(teams))
    teamWins = np.zeros(len(teams))
    teamLosses = np.zeros(len(teams))
    count = 0
    np.random.seed(17)
    random.seed(17)
    for j in range(len(competition)):
        competitionHost = random.sample(nationalTeam['teamID'].tolist(), 1)[0]
        competitionID.append(competition['name'][j] + ' ' + competition['year'][j])
        for i in range(num_games):
            count += 1
            gameIDs.append(count)
            seasonID.append(competition['year'][j])
            gameCompetitionID.append(competition['name'][j] + ' ' + competition['year'][j])

            if competition['type'][j] == 'club':
                #                stadium = stadiums[stadiums['Team']==team1]
                opponents = random.sample(clubs['teamID'].tolist(), 2)
                team1 = opponents[0]
                team2 = opponents[1]
                locations.append(clubs['location'][teams.index(team1)])
                team1Players = athletes[athletes['teamID'] == team1]
                team2Players = athletes[athletes['teamID'] == team2]
                team = clubs
            else:

                locations.append(competitionHost)
                opponents = random.sample(nationalTeam['teamID'].tolist(), 2)
                team1 = opponents[0]
                team2 = opponents[1]
                team = nationalTeam
                team1Players = athletes[athletes['countryID'] == team1]
                team2Players = athletes[athletes['countryID'] == team2]

            matches_team1.append(opponents[0])
            matches_team2.append(opponents[1])
            matches_team1ID.append(teams[teams.index(team1)])
            matches_team2ID.append(teams[teams.index(team1)])
            team1_goals = np.random.choice(5)
            team2_goals = np.random.choice(5)
            team1_assists = min(np.random.choice(5), team1_goals)
            team2_assists = min(np.random.choice(5), team2_goals)

            scores.append(team1 + ' ' + str(team1_goals) + ' - ' + str(team2_goals) + ' ' + team2)

            if team1_goals > 0:

                for goal_scorerID in np.random.choice(team1Players[team1Players['position'] != 'GK']['id'][:8],
                                                      team1_goals):
                    athletes.loc[athletes['id'] == goal_scorerID, 'goals'] += 1
                    gameGoal.at[len(gameGoal), ['gameID', 'athleteID', 'name']] = [count, goal_scorerID, athletes[
                        athletes['id'] == goal_scorerID]['name'].tolist()[0]]
                for passerID in np.random.choice(team2Players[team2Players['position'] != 'GK']['id'][:8],
                                                 team1_assists):
                    athletes.loc[athletes['id'] == goal_scorerID, 'assists'] += 1
            if team2_goals > 0:
                for goal_scorerID in np.random.choice(team1Players[team1Players['position'] != 'GK']['id'][:8],
                                                      team2_goals):
                    athletes.loc[athletes['id'] == goal_scorerID, 'goals'] += 1
                    gameGoal.at[len(gameGoal), ['gameID', 'athleteID', 'name']] = [count, goal_scorerID, athletes[
                        athletes['id'] == goal_scorerID]['name'].tolist()[0]]
                for passerID in np.random.choice(team2Players[team2Players['position'] != 'GK']['id'][:8],
                                                 team2_assists):
                    athletes.loc[athletes['id'] == goal_scorerID, 'assists'] += 1

            if team1_goals > team2_goals:
                winner = team1
                loser = team2
            elif team2_goals >= team1_goals:
                winner = team2
                loser = team1
                teamWins[teams.index(team2)] += 1
                teamLosses[teams.index(team1)] += 1

            team.loc[team['teamID'] == winner, 'wins'] += 1
            team.loc[team['teamID'] == loser, 'losses'] += 1

            if competition['type'][j] == 'club':
                athletes.loc[athletes['teamID'] == loser, 'losses'] += 1
                athletes.loc[athletes['teamID'] == winner, 'wins'] += 1
            else:
                athletes.loc[athletes['countryID'] == loser, 'losses'] += 1
                athletes.loc[athletes['countryID'] == winner, 'wins'] += 1

            winners.append(winner)
            losers.append(loser)
            team.loc[team['teamID'] == team1, 'goals'] += team1_goals
            team.loc[team['teamID'] == team2, 'goals'] += team2_goals
            team.loc[team['teamID'] == team1, 'assists'] += team1_assists
            team.loc[team['teamID'] == team2, 'assists'] += team2_assists

            gameID = range(1, count + 1)
    return competitionID, gameCompetitionID, seasonID, gameID, matches_team1ID, matches_team2ID, winners, losers, scores, locations

competitionID, gameCompetitionID, year, gameID, c1, c2, winners, losers, scoresClub, locations = generateCompetitiveMatches(
    teams, competition, num_games=20)
competition['competitionID'] = competitionID

matches = pd.DataFrame()
matches['teamID1'] = c1
matches['teamID2'] = c2
matches['winningTeamID'] = winners
matches['losingTeamID'] = losers
matches['competitionID'] = gameCompetitionID
matches['score'] = scoresClub
matches['location'] = locations
matches['seasonID'] = year

random.seed(17)
matches['gameID'] = gameID


def most_common(lst):
    return max(set(lst), key=lst.count)


competition['winner'] = [most_common(matches[matches['competitionID'] == edition]['winningTeamID'].tolist()) for edition
                         in competition['competitionID']]

competitiveMatches = matches[
    ['gameID', 'teamID1', 'teamID2', 'winningTeamID', 'losingTeamID', 'competitionID', 'seasonID', 'score']]
gameInfo = matches[['gameID', 'score', 'location', 'seasonID']]




coaches.to_csv('Coach.csv')
athletes.to_csv('Athlete.csv')
season.to_csv('Season.csv')
competition.to_csv('Competition.csv')
gameGoal.to_csv('GameGoal.csv')
team = clubs.append(nationalTeam)
team.to_csv('Team.csv')
matches.to_csv('Game.csv')
stadiums_filtered.to_csv('Stadium.csv')

Base = declarative_base()

coach = coaches
athlete = athletes
team = team
game = matches
stadium = stadiums_filtered
gameGoal = gameGoal
competition = competition
season = season

from app.db.database import Athlete, Coach, Competition,GameGoal, Game, Season, Stadium, Team, db

coach.to_sql(con=db.engine, name=Coach.__tablename__, if_exists='replace')
athlete.to_sql(con=db.engine, name=Athlete.__tablename__, if_exists='replace')
team.to_sql(con=db.engine, name=Team.__tablename__, if_exists='replace')
game.to_sql(con=db.engine, name=Game.__tablename__, if_exists='replace')
stadium.to_sql(con=db.engine, name=Stadium.__tablename__, if_exists='replace')
gameGoal.to_sql(con=db.engine, name=GameGoal.__tablename__, if_exists='replace')
competition.to_sql(con=db.engine, name=Competition.__tablename__, if_exists='replace')
season.to_sql(con=db.engine, name=Season.__tablename__, if_exists='replace')

