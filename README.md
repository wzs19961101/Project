# Project

League of Legends (LoL) is a multiplayer online battle arena video game developed and published by Riot Games. Inspired by Defense of the Ancients, a custom map for Warcraft III, Riot's founders sought to develop a stand-alone game in the same genre. Since its release in October 2009, the game has been free-to-play and is monetized through purchasable character customization. The game is available for Microsoft Windows and macOS.

Image you are a League of Legends player. You have to pick up a champion from the list as your role in the game. In order to have more chance to win during the game then you will need to have your own strategy. Therefore it will be helpful for you to know the win rate of the champion before you picking up. 

In this case, the main purpose of our project is to scrap the win rate of the champion from the most famous game data resource website:
https://euw.op.gg/champion/statistics

In this website, which includes champion information and ranking data etc. We will mainly  focus on the champion win rate.
For all 3 parts, we will use champion name ‘sett’, position ‘top’ as initially input, therefore the web will be like that : https://euw.op.gg/champion/sett/statistics/top/matchup

Our goal is : Input one champion and its position, then the output will be this champion’s matched-up win rate.
Avaliable Position list: {'top': 'top', 'jun': 'jungle', 'mid': 'mid', 'ad': 'bot', 'sup': 'support'}
Avaliable hero list：“Irelia“; “Trundle”; “Ezreal”; “Alistar”; “Amumu”; “Anivia”; “Annie”; “Ashe”; “ChoGath”; “Fiddlesticks”; “Gangplank”etc.

1.For beautiful soup part:
Just run the beautfulsoup.py, and input champion name ‘sett’, position ‘top’ as example

2.For scrapy part:
Our spider name is gamelol_spider, so we used the command to run : 

scrapy crawl gamelol_spider -o gamelol.csv


3.For selenium part:
Just run the seleproject.py, it will open the website and giving result
