# File name: oop4_9.py
# Author: Essi Peltola
# Description: An application for examining hockey league statistics

import json

class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.points()}"

def read_data(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return [Player(**entry) for entry in data]

def search_player(data, name):
    player = next((player for player in data if player.name == name), None)
    if player:
        print(player)
    else:
        print("Player not found.")

def list_teams(data):
    teams = sorted(set(player.team for player in data))
    for team in teams:
        print(team)

def list_countries(data):
    countries = sorted(set(player.nationality for player in data))
    for country in countries:
        print(country)

def list_players_in_team(data, team):
    players = sorted((player for player in data if player.team == team), key=lambda x: x.points(), reverse=True)
    for player in players:
        print(player)

def list_players_from_country(data, country):
    players = sorted((player for player in data if player.nationality == country), key=lambda x: x.points(), reverse=True)
    for player in players:
        print(player)

def most_points(data, n):
    players = sorted(data, key=lambda x: (x.points(), x.goals), reverse=True)[:n]
    for player in players:
        print(player)

def most_goals(data, n):
    players = sorted(data, key=lambda x: (x.goals, -x.games), reverse=True)[:n]
    for player in players:
        print(player)

def main():
    file_name = input("file name: ")
    data = read_data(file_name)
    print(f"read the data of {len(data)} players")

    while True:
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

        command = input("command: ")

        if command == '0':
            break
        elif command == '1':
            name = input("name: ")
            search_player(data, name)
        elif command == '2':
            list_teams(data)
        elif command == '3':
            list_countries(data)
        elif command == '4':
            team = input("team: ")
            list_players_in_team(data, team)
        elif command == '5':
            country = input("country: ")
            list_players_from_country(data, country)
        elif command == '6':
            n = int(input("how many: "))
            most_points(data, n)
        elif command == '7':
            n = int(input("how many: "))
            most_goals(data, n)

if __name__ == "__main__":
    main()
