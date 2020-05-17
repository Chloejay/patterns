#! /usr/bin/env python

from typing import Generic, Iterable, List, TypeVar, Mapping, Callable, Any, NoReturn
from collections import defaultdict
from future.utils import iteritems
from functools import reduce

#use functional programming concept based on Scala and type theory. 

A = TypeVar("A")

def compose(f: Callable[[Any], Any], g: Callable[[Any], Any])-> Any:
    return lambda x: f(g(x))

def pure(val: Any): # category theory, identity 
    return val

# https://stackoverflow.com/questions/16739290/composing-functions-in-python
def combine_all(*f)-> int:
    reduce(compose, pure, f)

# input is int
def functor(x: int, f: Callable[[int], int])-> int:
    return f(x)

class Monoid(Generic[A]):
    def __init__(self, empty: None, combine: Callable[[Any], Any]):
        self.empty = empty
        self.combine = combine

    def monoid_combine(self, iterable: Iterable[int]):
        return monoid_combine(self, iterable)

    def foldMap(self, f, iterable: Iterable[int]):
        return self.monoid_combine(map(f, iterable))


def groupBy(f: Callable, iterable: Iterable[Any]):
    results = defaultdict(list)
    for i in iterable:
        results[f(i)].append(i)
    return results

def filter_keys(predicate: bool, mapping: Mapping):
    return {k: v for k, v in iteritems(mapping) if predicate(k)}

def find(predicate: bool, iterable: Iterable):
    list_ = list()
    for i in iterable:
        if predicate(i):
            return i
    return None



if __name__ == "__main__":

    x = compose(lambda x: x ** x, lambda y: y ** y)
    print(x(2)) #256
    print(functor(1, lambda x: x + x))
    print(groupBy(lambda x: x * x, [1, 2]))
    filter = filter_keys(lambda x: x % 2 == 0, {1: "a", 2: "b"})
    print(filter)