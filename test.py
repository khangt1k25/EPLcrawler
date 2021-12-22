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
seasonids = {
    "418": "2021/22",
    "363": "2020/21",
    "274": "2019/20",
    "210": "2018/19",
    "79": "2017/18",
    "54": "2016/17",
    "42": "2015/16",
    "27": "2014/15",
    "22": "2013/14",
    "21": "2012/13",
    "20": "2011/12",
    "19": "2010/11",
    "18": "2009/10",
    "17": "2008/09",
    "16": "2007/08",
    "15": "2006/07",
    "14": "2005/06",
    "13": "2004/05",
    "12": "2003/04",
    "11": "2002/03",
    "10": "2001/02",
    "9": "2000/01",
    "8": "1999/00",
    "7": "1998/99",
    "6": "1997/98",
    "5": "1996/97",
    "4": "1995/96",
    "3": "1994/95",
    "2": "1993/94",
    "1": "1992/93"
}
clubstat_url = 'https://footballapi.pulselive.com/football/stats/team/{}?compSeasons={}'
print(clubstat_url.format(123,456))
# new = {ele['id']:ele['label'] for ele in data}

# with open('./p212.json', 'w') as f:
#     json.dump(new, f)


# print(len(data))

