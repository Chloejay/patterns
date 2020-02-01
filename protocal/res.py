import requests 
from pprint import pprint 
import simplejson as json 

#TODO 
url='https://twitter.com/home'
TIMEOUT= 20

# data, payload  
class Request(object):
    def __init__(self, name, pswd, url = url, timeout = TIMEOUT):
        self.url = url
        # self.data = data
        self.timeout = timeout 
        # self.payload = payload
        self._name = name 
        self._pswd=pswd

    def send_request(self):
        r = requests.get(self.url, timeout = self.timeout,auth = (self._name, self._pswd)) 
        # print(r.status_code) #DEBUG 
        try:

            if r.status_code == requests.codes.ok:
                content = r.content 
                pprint(content) 
                items = json.loads(content) 
                for item in items:
                    # pprint(item) 
                    return item 
            else:
                return f'error is {r.raise_for_status()}'

        except Exception as e:
            pprint(str(e)) 

    #TODO
    def post_response(self):
        r=requests.post(self.url, json = {'key', 'val'})
        pprint(r.json()) 
        return r.json()  

if __name__=='__main__':

    x= Request('chloeji91','') 
    x.send_request() 



