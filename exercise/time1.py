#! /usr/bin/env python

import time 
import requests 
import logging 
from pprint import pprint 
import functools 
logging.basicConfig(level=logging.INFO)

class ServiceUnavailableError(Exception):
    pass

def sleep(timeout, retry = 2 : int):
    def func(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries <retry:
                try:
                    return fn(*args, **kwargs)  
                except Exception as e:
                    logging.error(f'error is {e}')
                    time.sleep(timeout) 
                    logging.info(f'sleep for {timeout} seconds')
                    retries +=1 
        return wrapper 
    return func

@sleep(3)
def check_service(url: str)-> str:
    try:
        res = requests.get(url)
        data = res.text

        if res.status_code != 200:
            raise ServiceUnavailableError() 
    except (
        requests.exceptions.ConnectionError, 
        requests.exceptions.Timeout,
        requests.exceptions.HTTPError
    ) as exc:
        raise ServiceUnavailableError from exc 
    else:
        return data 
    finally:
        logging.info(f'{url} load is ok')



if __name__ == "__main__":
    url = 'https://medium.com/'
    print(check_service(url))