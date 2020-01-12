# https://docs.python.org/3/library/configparser.html

import configparser
from pprint import pprint 
import sys
import json 
 
def remove_quotes(original):
    d = original.copy() #use copy not to sabotage source data
    for k, v in d.items():
        if isinstance(v, str):
            s = d[k]
            if s.startswith(('"', "'")):
                s = s[1:]
            if s.endswith(('"', "'")):
                s = s[:-1]
            d[key] = s
        if isinstance(v, dict):
            d[k] = remove_quotes(v)
    return d
 
class Preferences:
    def __init__(self, ini):
        self.ini = ini
        self.config = configparser.ConfigParser()
        # print(self.config._sections) 
        self.config.read(ini)
        self.d = self.to_dict(self.config._sections)
 
    def as_dict(self):
        return self.d 
 
    def to_dict(self, config):
        d = json.loads(json.dumps(config))
        d = remove_quotes(d)
        return d

if __name__=='__main__':
    prefs = Preferences("test.ini")
    d = prefs.as_dict()
    pprint(d)
    

