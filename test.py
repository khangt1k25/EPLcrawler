import requests
import json

# url = 'https://footballapi.pulselive.com/football/teams/11/compseasons/418/staff?pageSize=30&compSeasons=418&altIds=true&page=0&type=player'
# url = 'https://footballapi.pulselive.com/football/players?pageSize=30&compSeasons=418&altIds=true&page=0&type=player&id=-1&compSeasonId=418'

# matchID = "46889"
# match = requests.get(
#     f"https://footballapi.pulselive.com/football/stats/match/{matchID}",
#     headers = {
#         "origin": "https://www.premierleague.com"
#     }
# )

# match = requests.get(
#     url,
#     headers={
#         "origin": "https://www.premierleague.com"
#     }
# )
# data = json.loads(match.text)
with open('./season.json', 'r') as f:
    data = json.load(f)

new = {ele['id']:ele['label'] for ele in data}

with open('./seasonid.json', 'w') as f:
    json.dump(new, f)


# print(len(data))

