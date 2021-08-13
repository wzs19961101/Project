import requests
from bs4 import BeautifulSoup

position_all = {'top': 'top', 'jun': 'jungle', 'mid': 'mid', 'ad': 'bot', 'sup': 'support'}
# anti-crawler mechanism
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
name_input = input('input the champion name：')
myname = name_input
myposition = input('input the position：')
position = position_all[myposition]
print('searching，please wait~~~')
# Make a request to the url, pass in the request header, and keep the returned result in res
res = requests.get('http://euw.op.gg/champion/{}/statistics/{}/matchup'.format(myname, position), headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# Find the div tag whose class attribute is champion-matchup-champion-list__item to form a list named items
items = soup.find_all('div', class_='champion-matchup-champion-list__item')

print('hero    win rate')

for i in items:
    # The data-champion-name attribute value in the div is the hero name
    name = i['data-champion-name']
    # The data-value-winrate attribute in the div attribute is the winning rate of the hero
    rate =  float(i['data-value-winrate'])
    print(name, '{}%'.format(round(rate * 100, 2)))
