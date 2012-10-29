import requests
from bs4 import BeautifulSoup
from reddit import Reddit

reddit_connection = Reddit(user_agent='wootbot/1.0')
reddit_connection.login('wootbot', 'password')

r = requests.get('http://www.woot.com')
soup = BeautifulSoup(r.content)

item = soup.find('h2', 'fn').text
price = soup.find('span', 'price').text
list_price = soup.find('span', 'list-price').text
percent_off = soup.find('span', 'percentage').text

title = '%s - %s' % (item, price)
text = '%s\n\n%s\n\n%s (%s)' % (item, price, percent_off, list_price)

reddit_connection.submit('woot', title, text)
