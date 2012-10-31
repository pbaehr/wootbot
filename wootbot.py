import urllib2
import json

from reddit import Reddit

reddit_connection = Reddit(user_agent='wootbot/1.0')
reddit_connection.login('wootbot', 'password')

r = urllib2.urlopen('http://api.woot.com/1/sales/current.json')
json = json.loads(r.read())
newest_item = json['sales'][0]

item = newest_item['Title']
price = newest_item['Price']
url = newest_item['SaleUrl']

title = '%s - %s' % (item, price)

print title
print url
reddit_connection.submit('woot', title, url=url)
