from typing import Generic, Iterable, List, TypeVar
from collections import defaultdict
from future.utils import iteritems
from functools import reduce 

#use functional programming concept here based on Scala, to write some FP in python. 

A = TypeVar("A") 

def compose(f, g):
    return lambda x: f(g(x)) 

def pure(val): # category theory, identity 
    return val 

# https://stackoverflow.com/questions/16739290/composing-functions-in-python
def combine_all(*f):
    reduce(compose, pure, f)  

def functor(x, f):
    return f(x) 

class Monoid(Generic[A]):

    def __init__(self, empty, combine):
        self.empty = empty 
        self. combine = combine 

    def monoid_combine(self, iterable):
        return monoid_combine(self, iterable) 

    def foldMap(self, f, iterable):
        return self.monoid_combine(map(f, iterable)) 


def groupBy(f, iterable):
    results = defaultdict(list)
    for i in iterable: 
        results[f(i)].append(i) 
    return results 

def filter_keys(predicate, mapping):
    return {k: v for k, v in iteritems(mapping) if predicate(k)}

def find(predicate, iterable):
    list_ = list() 
    for i in iterable:
        if predicate(i):
            return i  
    return None 



if __name__ == "__main__":
    x = compose (lambda x: x**x,lambda y: y**y) 
    print(x(2)) #256
    print(functor(1, lambda x: x+x)) 
    print(groupBy(lambda x: x*x, [1,2]))
    filter = filter_keys(lambda x: x % 2 == 0, {1:"a", 2:"b"}) 
    print(filter) 

