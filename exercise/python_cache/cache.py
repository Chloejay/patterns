from functools import lru_cache 
from time import time 
from datetime import datetime 
import logging 
logging.basicConfig(level=logging.INFO)


def logtime(if_cache_func):
    def wrapper(*args, **kwargs):
        start = time() 
        result = if_cache_func(*args, **kwargs)
        exc_time = time()- start

        with open (f'fib_log/{if_cache_func.__name__}_eventLog.txt', 'a') as outf:
            outf.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}\t{if_cache_func.__name__}\t{exc_time:.4f}\n')
        return result 

    return wrapper 

@logtime
def fib(number: int) -> int:
    if number == 0: 
        return 0
    elif number == 1: 
        return 1
    return fib(number-1) + fib(number-2)


#cache size set to 32 
@lru_cache(maxsize = 32)
@logtime
def fib_memoization(n: int)-> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib_memoization(n-1) + fib_memoization(n-2)


def main():
    fib(20)
    fib_memoization(20)
    logging.info(fib_memoization.cache_info())


if __name__ == '__main__':
    main() 