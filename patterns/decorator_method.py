'''
Python decorator methods, @decorator is shortcut for fn = @decorator(fn), a wrapper
- object (function and class) in closure style
- @property, @staticmethod and @classmethod
- built in packages functools.wraps()

TODO:
decorator pattern, to add behaviors dynamically to an object at runtime by combing polymorphism
and aggregation.
- design component interface
- abstract decorator class
- concrete decorator class
'''

from typing import Iterable
from functools import wraps, partial

def wrap_single_args(fn):
    # @wraps(fn)
    def text(*msg):
        return fn(*msg)
    return text

@wrap_single_args
def write(msg: str, msg2: str)->str:
    return f'greetings msg is {msg} -> {msg2}'

class WriteClass:
    @wrap_single_args
    def write(self, msg: str, msg2: str):
        return f'test decorator class {msg} -> {msg2}'

# use variable_args[kwargs]
def wrapper_outside(fn_call_inside_wrapper):

    def wrapper(*args, **kwargs):
        return fn_call_inside_wrapper(*args, **kwargs)
    return wrapper

@wrapper_outside
def call_anything(a: int, b: int)-> Iterable[str]:
    return f'combine arguments into one {a*b if a>b else a/b }'

def partialFn(arg1, arg2):
    return int(arg1)* float(arg2)

# free variable and nonlocal variable concept
def count():
    list_ = list() #free variable

    def sum_count(val):
        list_.append(val)
        total = sum(list_)
        return total

    return sum_count

COUNTINSTANCE = count()

def make_avg():
    count, total = 0, 0

    def avg(new_val: int)->int:
        nonlocal count, total
        count += 1
        total += new_val
        return total/count
    return avg

AVG_INSTANCE = make_avg()

#decorated class
class Test1:
    def __init__(self, fn):
        self.fn = fn
        self.callCount = 0

    def __call__(self, *args): #use __call__ to make class callable 
        self.callCount += 1
        self.fn(self.callCount, *args)

@Test1
def write_again(val, val2):
    print(f'OK! call {val2} for {val} times')

class Test2:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        result = self.fn(*args, **kwargs)
        return result

@Test2
def addEle(val: int, val2: int)-> int:
    print(val, val2)
    return val + val2

# decorator outside class
def outsider_fn(fn):
    def wrapper(self, age: int)-> int:
        age = age + 1
        return fn(self, age)
    return wrapper

class Age(object):
    def __init__(self):
        self.adultAge = 20
    @outsider_fn
    def add_age(self, age: int)-> str:
        print(f'my age is {self.adultAge + age} in 2020')

# @property, @staticmethod, @classmethod decorator method
class TestEmail:
    def __init__ (self, first: str, age: int, last = 'ji')-> None:
        self._firstName = first
        self._lastName = last
        self.age = age
        self.city = 'town'

    @property #set dynamic attributes 
    def email(self):
        try:
            return self._get_email()
        except AttributeError as e:
            print(str(e))

    @email.setter
    def get_email(self, first: str):
        return self._reset_email(first)
        # return f'{self._firstName}-{self._lastName}@gmail.com' 

    @get_email.deleter
    def get_email(self):
        del self._lastName
    
    def _get_email(self):
        return f'{self._firstName} - {self._lastName}@gmail.com'

    def _reset_email(self, first: str):
        self._firstName = first
        # self._lastName = last 

    @staticmethod
    def write(anyVal: str)-> str:
        return f'plain staticmethod in scope - {anyVal}'
    
    @classmethod
    def fullname(cls, first: str, last: str)-> str:
        return first + " " + last

    @classmethod
    def rewrite(cls, anyVal: str)-> str:
        return f"rewriting {anyVal}"

    @classmethod
    def test(cls, val: str)-> str:
        cls.city = 'space'
        return f'{cls.city} by {cls.rewrite(val)}'

# UDD, use functools.wraps
'''
# helper function
def decorator(fn):
    #the functool.wraps is a tool to copy the wrapped function's infos,like docstring
    @wraps(fn)
    def wrapper(*args, **kwars):
        result= fn(*args, **kwargs)
        return result
    return wrapper
'''
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time

        try:
            start = time.perf_counter()
            value = func(*args, **kwargs)
            end = time.perf_counter()
            run_time = end - start

            print(f"Finished {func.__name__!r} in {run_time:.2f} secs")
        except Exception:
            pass

        return value
    return wrapper

@timer
def time_record(time):
    for _ in range(time):
        sum([i**2 if i %2 != 0 else i for i in range(10000)]) 

#extra - mix conditions
def test_call(have_call):

    def wrapper(*args):
        from datetime import datetime
        if 5 < datetime.now().hour < 20:
            return have_call(*args)
        print('Night then!')
    return wrapper

@test_call
def call(name, city: str)-> str:
    return f'{name}, whom lives in {city}'
# test_call(call)()

# use function as condition
def test_con(a, x: str, y: str)->str: 
    def fn1(x):
        return f'condition one {x}'
    def fn2(y):
       return f'condition two {y}' 
    if a == 'ok':
        return fn1(x)
    else:
        return fn2(y)


if __name__ == "__main__":

    print(call_anything(1, 2)) #should be 1/2
    classtest = WriteClass()
    print(classtest.write('decoratedClass', 'test'))
    print(write('halo', 'viola')) 
    print(partial(partialFn, 1.00005)(1.12))
    print(COUNTINSTANCE(10))
    print(COUNTINSTANCE(20))  #should be 30 
    print(AVG_INSTANCE(10))
    print(AVG_INSTANCE(20)) #should be 15 
    write_again('viola') 
    write_again('viola!!')
    print(addEle(0, 1))
    testAge = Age()
    testAge.add_age(8)
    person = TestEmail('chloe', 28)
    person.get_email = 'emily'
    print(person.get_email)
    print(person.write('WRITING'))
    print(TestEmail.fullname('emma', 'ji'))
    print(TestEmail.rewrite('ABSTRACTING'))
    print(TestEmail.test('craft'))
    time_record(100)
    print(call('emma', 'foresttown'))
    print(test_con('ok', 'TESTING', 'PLAYING'))