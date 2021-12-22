


# MARK:- libs

from scrapy.spiders import CrawlSpider
import scrapy

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

base_url = 'https://footballapi.pulselive.com/football/teams?pageSize=25&altIds=true&compSeasons=418'

club_url = 'https://footballapi.pulselive.com/football/teams/%i/compseasons/418/staff?compSeasons=418'

player_url = 'https://footballapi.pulselive.com/football/stats/player/%i?comps=1'

# Get player for each team
class PlayerOfClubSpider(CrawlSpider):
    name = 'player'
    
    headers = {
        'origin': 'https://www.premierleague.com'
    }
    start_urls = [base_url]
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url = url,
                headers=self.headers,
                callback=self.parse
            )
    
    def parse(self, response):
        jsonfile = response.json()
        for club in jsonfile['content']:
            clubid =  club['id']
            cluburl = club_url%int(clubid)
            yield scrapy.Request(
                url=cluburl,
                headers=self.headers,
                callback=self.parse_item
            )
    def parse_item(self, response):
        jsonfile = response.json()
        teamid = jsonfile['team']['club']['id']
        # teamname = jsonfile['team']['name']
        for player in jsonfile['players']:
            yield scrapy.Request(
                url=player_url%int(player['id']),
                headers=self.headers,
                callback=self.parse_player,
                cb_kwargs=dict(team=teamid)
            )


    def parse_player(self, response, team):
        jsonfile = response.json()
        
        id = jsonfile['entity']['id']

        item = {'teamid': team, 'id':id, 'playerId': jsonfile['entity']['playerId'], 'info': jsonfile['entity'], 'stats': jsonfile['stats']}
        
        yield item
