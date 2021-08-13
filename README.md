# Project

1.For beautiful soup part:
Just run the beautfulsoup.py, and input champion name ‘sett’, position ‘top’ as example

2.For scrapy part 
Our spider name is gamelol_spider, so we used the command to run : 
scrapy crawl gamelol_spider -o gamelol.csv
PS: But in here, if we want to change champion name and position, we have to change the start_urls to:  https://euw.op.gg/champion/{hero}/statistics/{position}/matchup
Replace {hero} and {position}  to your hero name and position.

3.For selenium part 
Just run the seleproject.py, it will open the website and giving result
