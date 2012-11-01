import unittest

import wootbot


class TestWootBot(unittest.TestCase):
    def test_load(self):
        item = wootbot.get_latest_woot_item()
        self.assertTrue(item['Title'])
        self.assertTrue(item['Price'])
        self.assertTrue(item['SaleUrl'])

    def test_item_load(self):
        json = {u'Title': u'LG 47" 1080p LED HDTV',
                u'Price': u'$499.99',
                u'SaleUrl': 'http://www.woot.com/offers/lg-47-1080p-led-hdtv-6'}
        item = wootbot.WootItem(json)
        self.assertTrue(item.loaded)
        self.assertEqual(item.title, json['Title'])
        self.assertEqual(item.price, json['Price'])
        self.assertEqual(item.url, json['SaleUrl'])
        self.assertEqual(str(item), 'LG 47" 1080p LED HDTV - $499.99')

if __name__ == '__main__':
    unittest.main()
