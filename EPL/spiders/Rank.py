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
base_url = 'https://footballapi.pulselive.com/football/standings?compSeasons=%i&altIds=true'

# Get player for each team
class RankCrawler(CrawlSpider):
    name = 'rank'
    
    
    
    start_urls = [base_url%int(i) for i in seasonids.keys()]

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

        seasonid = jsonfile['compSeason']['id']
        season = jsonfile['compSeason']['label']

        table = jsonfile['tables']

        yield {'id': seasonid, 'season':season, 'table': table}

