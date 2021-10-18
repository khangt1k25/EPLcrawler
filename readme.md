
# Crawler EPL data



## Getting started
* Requiremnts:
  * Python
  * Scrapy
  * Git clone repo
  * Cd to repo


1. PlayerOfClub
 
```
scrapy crawl playerofclub -o playerofclub_2122.json
```

change compSeasons in URL in PlayerOfClub.py to id of other seasons and change command line to output playerofclub_xxyy.json [Please read seasonid to get id]

2. Player

```
scrapy crawl playerofclub -o player_2122.json
```

change compSeasons in URL in PlayerOfClub.py to id of other seasons and change command line to output player_xxyy.json [Please read seasonid to get id]

3. Ranking

```
scrapy crawl rank -o rank.json
```

This script run only 1 time to crawl ranking tables of all seasons.