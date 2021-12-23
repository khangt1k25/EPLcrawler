


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

base_url = 'https://footballapi.pulselive.com/football/teams?pageSize=25&altIds=true&compSeasons={}'

club_url = 'https://footballapi.pulselive.com/football/teams/{}/compseasons/{}/staff?compSeasons={}'

player_url = 'https://footballapi.pulselive.com/football/stats/player/{}?comps=1'
ssids = list(seasonids.keys())
## change this 
ssid = [ssids[0]]

# Get player for each team
class PlayerOfClubSpider(CrawlSpider):
    name = 'player'
    
    headers = {
        'origin': 'https://www.premierleague.com'
    }
    # start_urls = [base_url*int(i) for i in ssids]
    def start_requests(self):
        for ss in ssid:
            yield scrapy.Request(
                url = base_url.format(int(ss)),
                headers=self.headers,
                callback=self.parse,
                cb_kwargs={'ss':int(ss)}
            )
    
    def parse(self, response, ss):
        jsonfile = response.json()
        for club in jsonfile['content']:
            clubid =  club['id']
            yield scrapy.Request(
                url=club_url.format(int(clubid), int(ss), int(ss)),
                headers=self.headers,
                callback=self.parse_item,
                cb_kwargs={'ss':int(ss), 'clubid':int(clubid)}
            )
    def parse_item(self, response, ss, clubid):
        jsonfile = response.json()

        for player in jsonfile['players']:
            yield scrapy.Request(
                url=player_url.format(int(player['id'])),
                headers=self.headers,
                callback=self.parse_player,
                cb_kwargs=dict({'ss':ss, 'clubid':clubid})
            )


    def parse_player(self, response, ss, clubid):
        jsonfile = response.json()
        
        id = jsonfile['entity']['id']

        item = {'id':id, "ss": ss, 'clubid': clubid, 'playerId': jsonfile['entity']['playerId'], 'info': jsonfile['entity'], 'stats': jsonfile['stats']}
        
        yield item
