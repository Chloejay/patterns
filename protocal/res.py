#! /usr/bin/env python

import requests 
from pprint import pprint 
import simplejson as json 
from bs4 import BeautifulSoup
import time 
import asyncio 
import logging 
import aiohttp 

url='https://www.goodreads.com/search/index.xml'
TIMEOUT= 10
 
class Request(object):
    def __init__(self, key, 
                    url = url, 
                    timeout = TIMEOUT, 
                    _secret= '', 
                    logger=logging.getLogger()):

        self.url = url
        self.timeout = timeout 
        self._key = key 
        self._secret = _secret
        logger.setLevel(logging.INFO)
        self.logger = logger 
    
    def send_request(self):
        r = requests.get(self.url, 
                        timeout = self.timeout, 
                        params={'key':self._key, 
                        'q':'some_book'}) 
        try:

            if r.status_code == requests.codes.ok:
                self.logger.info('starting fetching....')
                content = r.content 
                c=json.dumps(content)
                items = json.loads(c) 
                bs = BeautifulSoup(items, 'html.parser')
                # print(bs.prettify())
                works= bs.find_all('work')
                for w in works:
                    
                    authors=w.find_all('author')
                    authorlist, ratings = [],[]
                    for author in authors:
                        authorlist.append(author.find('name').getText()) 
                    ratings.append(w.find('average_rating').getText())

                    zipped=zip(authorlist, ratings) 
                    for a,r in list(zipped):
                        print(f'author name is {a}, whose book avg rating is {r}')
                        time.sleep(3)
                    
            else:
                return f'error is {r.raise_for_status()}'

        except Exception as e:
            pprint(str(e)) 

    #TODO 
    # def post_response(self):
    #     r=requests.post(self.url, json = {'key', 'val'})
    #     pprint(r.json()) 
    #     return r.json()  

if __name__=='__main__':
    _key='X3ZhR1BQknYiwnnPeS1uAw'
    x= Request(_key) 
    print(x.send_request()) 


# async def main(url, key):
    
#     async with aiohttp.ClientSession() as sess:
#         async with sess.get(url,params= {'key':key, 'q':'some_book'}) as r:
#             content = await r.text()
#             return content 

# loop= asyncio.get_event_loop() 
# c= loop.run_until_complete(main(url, key))
# print(c) 