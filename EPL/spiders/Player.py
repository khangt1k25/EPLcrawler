# MARK:- libs

from scrapy.spiders import CrawlSpider
import scrapy


# MARK: spider
# 363: id season 

base_url = 'https://footballapi.pulselive.com/football/teams/%i/compseasons/363/staff?compSeasons=363'

base_player_url = 'https://footballapi.pulselive.com/football/stats/player/%i?comps=1'

# Get player for each team
class PlayerSpider(CrawlSpider):
    name = 'player'
    
    start_urls = [base_url%i for i in range(1, 22)]  # total 20 teams
    headers = {
        'origin': 'https://www.premierleague.com'
    }
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                headers=self.headers,
                callback=self.parse_item
            )
    def parse_item(self, response):
        jsonfile = response.json()

        team = jsonfile['team']['name']

        players = jsonfile['players']

        for player in players: # each player in team i
            
            player_id  = player['id']
            player_url =  base_player_url % int(player_id)
            yield scrapy.Request(
                url= player_url,
                headers=self.headers,
                callback=self.parse_player
            )
    def parse_player(self, response):
        jsonfile = response.json()
        
        id = jsonfile['entity']['id']

        item = {'id':id, 'info': jsonfile['entity'], 'stats': jsonfile['stats']}
        
        yield item
