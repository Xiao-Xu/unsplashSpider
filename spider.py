# -*- coding: utf-8 -*
import re
import requests
import json

headers = {'User-Agent': 'Mozilla/5.0'}
database = {}
count = 0


class Spider(object):
    def __init__(self, user_query, amount=1000):
        self.defult_page = 1
        self.query = user_query
        self.amount = amount
        self.total = self.request_json()['total']

# make a url include formated query && pages
    def make_url(self):
        url = f'https://unsplash.com/napi/search/photos?query={self.format_query()}&xp=&per_page=30&page={self.defult_page}'
        print('页数', self.defult_page)

        return url


# Format user query from input


    def format_query(self):
        # new_query = self.query.split(' ')
        makestr = re.compile(' ')
        formated_query = makestr.sub('%20', self.query)
        return formated_query
# request json

    def request_json(self):
        server_respons = requests.get(self.make_url(), headers=headers).text
        return json.loads(server_respons)

    def unwraper(self):

        results = self.request_json()['results']
        for i in results:
            if i['id'] not in database.keys():
                database[i['id']] = i['urls']['raw']
                self.total -= 1
                print(self.total)
                print(i['id'])
            else:
                print('重复')
                continue

        if self.total > 0:
            print('调用', self.total)
            self.defult_page += 1
            self.unwraper()

            # self.counting()

        print(database)

    '''def counting(self):
        count += 1
        return count'''

    def download(self):
        pass


ts = Spider('cleaner')
ts.unwraper()
