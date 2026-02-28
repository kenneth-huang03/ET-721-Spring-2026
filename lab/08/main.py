"""
Kenneth Huang
Lab 8 | API
Feb 24th, 2026
"""
import matplotlib.pyplot as pyplot
import pandas
import requests

from static import get_teams

dict_ = {
    "a": [11, 21, 31],
    "b": [12, 22, 32],
}

dict_data_frame = pandas.DataFrame(dict_)

print("Example 1: Simple API")
print(dict_data_frame.head())


print(f"The mean of each row of dict_ is: {dict_data_frame.mean()}")

print("Example 2: Get Teams from static.py")

teams = get_teams()

print(f"The first two teams: {teams[:2]}")

teams_data_frame = pandas.DataFrame(teams)
print(f"All Teams:\n{teams_data_frame.head()}")

teams_data_frame__warriors = teams_data_frame[teams_data_frame["nickname"] == "Warriors"]
print(f"Warriors:\n{teams_data_frame__warriors}")


print("Example 3: External APIs")

WARRIORS_DATA_URL = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"
WARRIORS_FILE_NAME = "GoldenState.pkl"

print("Downloading External File")
response = requests.get(WARRIORS_DATA_URL)

if response.status_code != 200:
    print("Error occurred")
else:
    with open(WARRIORS_FILE_NAME, "wb") as file:
        file.write(response.content)
    print("Download Complete and Saved")

    warriors_games = pandas.read_pickle(WARRIORS_FILE_NAME)

    warriors_vs_raptors = warriors_games[warriors_games["MATCHUP"].str.contains("TOR")]

    print("Golden State Warriors Games against Raptors")
    print(warriors_vs_raptors)

    warriors_vs_raptors_home = warriors_vs_raptors[warriors_vs_raptors["MATCHUP"].str.contains("vs")]
    warriors_vs_raptors_away = warriors_vs_raptors[warriors_vs_raptors["MATCHUP"].str.contains(" @ ")]

    print("Golden State Warriors Home Games against Raptors")
    print(warriors_vs_raptors_home)

    print("Golden State Warriors Away Games against Raptors")
    print(warriors_vs_raptors_away)

    home_average_plus = warriors_vs_raptors_home["PLUS_MINUS"].mean()
    away_average_plus = warriors_vs_raptors_away["PLUS_MINUS"].mean()
    home_average_points = warriors_vs_raptors_home["PTS"].mean()
    away_average_points = warriors_vs_raptors_away["PTS"].mean()

    print(f"Warriors Home Average: {home_average_plus}")
    print(f"Warriors Away Average: {away_average_plus}")


    METRICS  = ["PLUS_MINUS", "POINTS"]
    HOME_VALUES = [home_average_plus, home_average_points]
    AWAY_VALUES = [away_average_plus, away_average_points]

    x = range(len(METRICS))
    bar_width = 0.35

    pyplot.figure(figsize=(8,5))
    pyplot.bar([i - bar_width/2 for i in x], HOME_VALUES, width = bar_width, label = "Home", color = "skyblue")
    pyplot.bar([i - bar_width/2 for i in x], AWAY_VALUES, width = bar_width, label = "Away", color = "orange")

    pyplot.xticks(x, METRICS)
    pyplot.title("Warriors vs Raptors")

    pyplot.ylabel("Average Value")
    pyplot.legend()
    pyplot.show(block = True)

    # input("Press Enter to Close...")


# Exercises

EXERCISE_URL = "https://datahub.io/core/english-premier-league/r/season-2324.csv"
PREMIER_LEAGUE_FILE = "epl_matches.csv"

print("Download")
response = requests.get(EXERCISE_URL)
if response.status_code != 200:
    print("Error getting content")
else:
    with open(PREMIER_LEAGUE_FILE, "wb") as file:
        file.write(response.content)
    print("Download Complete")

    game_data = pandas.read_csv(PREMIER_LEAGUE_FILE)
    print(f"Premier League Data:\n{game_data.head()}")
    
    arsenal = game_data[game_data["HomeTeam"] == "Arsenal"]
    arsenal_vs_liverpool = arsenal[arsenal["AwayTeam"] == "Liverpool"]

    home_yellow_cards = arsenal_vs_liverpool["HY"].mean()
    away_yellow_cards = arsenal_vs_liverpool["AY"].mean()

    home_red_cards = arsenal_vs_liverpool["HR"].mean()
    away_red_cards = arsenal_vs_liverpool["AR"].mean()

    print(f"HYC {home_yellow_cards}")
    print(f"AYC {away_yellow_cards}")

    METRICS = ["Yellow Cards", "Red Cards"]
    HOME_VALUES = [home_yellow_cards, home_red_cards]
    AWAY_VALUES = [away_yellow_cards, away_red_cards]

    x = range(len(METRICS))
    bar_width = 0.35

    pyplot.figure(figsize = (8, 5))
    pyplot.bar([i - bar_width/2 for i in x], HOME_VALUES, width = bar_width, label = "Home", color = "skyblue")
    pyplot.bar([i - bar_width/2 for i in x], AWAY_VALUES, width = bar_width, label = "Away", color = "orange")

    pyplot.xticks(x, METRICS)
    pyplot.title("Arsenal VS Liverpool | Yellow Card and Red Card Comparison")
    pyplot.ylabel("Average")
    pyplot.legend()

    input("Press Enter to Close...")
