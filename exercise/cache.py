from functools import lru_cache 
import time

def fib(number: int) -> int:
    if number == 0: 
        return 0
    elif number == 1: 
        return 1
    return fib(number-1) + fib(number-2)

start = time.time()
fib(100)
print(f'Duration: {time.time() - start}s') 

#memorization 
@lru_cache(maxsize=512)
def fib_1(n: int)-> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_1(n-2) + fib_1(n-1) 
 
start = time.time()
fib_1(100)
print(f'Duration: {time.time() - start}s') 

