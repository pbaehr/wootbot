import urllib2
import json

from reddit import Reddit


# Change these to valid credentials
bot_username = 'wootbot'
bot_password = 'password'


def get_latest_woot_item():
    r = urllib2.urlopen('http://api.woot.com/1/sales/current.json')
    woot_json = json.loads(r.read())
    return woot_json['sales'][0]


class WootItem:
    title = ''
    price = ''
    url = ''
    loaded = False

    def __init__(self, item_json=None):
        if item_json:
            self.title = item_json['Title']
            self.price = item_json['Price']
            self.url = item_json['SaleUrl']
            self.loaded = True

    def __str__(self):
        if self.title:
            return '%s - %s' % (self.title, self.price)
        return ''

    def __unicode__(self):
        return self.__str__()

    def post_to_reddit(self):
        reddit_connection = Reddit(user_agent='wootbot/1.0')
        reddit_connection.login(bot_username, bot_password)
        reddit_connection.submit('woot', self.__str__(), url=self.url)


if __name__ == '__main__':
    newest_item = get_latest_woot_item()
    item = WootItem(newest_item)
    if item.loaded:
        item.post_to_reddit()
        print 'Posted: %s' % item
    else:
        print 'No Woot item found. Post aborted.'
