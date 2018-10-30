import requests 
import datetime
from bs4 import BeautifulSoup

url = 'https://www.coinmarketcap.com'

data = requests.get(url)

soup = BeautifulSoup(data.content, "html.parser")

coin_table = soup.find('table', { 'id': 'currencies' })
tbody = coin_table.find('tbody')

now = datetime.datetime.now()

print("Current Price of Cryptocurrencies as of: " +
      now.strftime("%Y-%m-%d %H:%M:%S"))
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

for tr in tbody.find_all('tr'):
    place = tr.find_all('td')[0].text.strip()
    coin = tr.find_all('td')[1].find_all('a')[1].text.strip()
    price = tr.find_all('td')[3].text.strip()
    
    print(place + " " + coin + ": " + price)

