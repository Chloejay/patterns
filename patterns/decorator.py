'''
decorator pattern, inpired by GoF book. illustrated the decorators in three parts
- object (function and class) in clsoure style 
- @property, @staticmethod and @classmethod 
- built in packages functools.wraps() 

why? (use decorator)- @decorator is just the shortcut for the fn=@decorator(fn), its behavior is to replace the decorated 
function with a new function, that accepts the same args and return the value; keep the code more DRY and extend functionality 
with more ease and flexibility, without inheritance. keep in mind, decorator is just the `wrapper`, kind of closure type, 
which just extend the functions in a mask way. 
'''
# fn return fn, used concept closure and wrapper (attach additional reponsibilities to an object dynamically) 

from typing import Iterable

def wrape_single_args(fn): 
    def text(msg):
        return fn(msg)
    return text 

@wrape_single_args  
def write(msg):
    return (f'the morning msg is {msg}') 

# use variable_args[kwargs]  
def wrapper_outside(fn_call_inside_wrapper):
    def wrapper(*args, **kwargs):
        return fn_call_inside_wrapper(*args, **kwargs)
    return wrapper 

@wrapper_outside 
def call_anything(a:int, b:int)-> Iterable[int]:
    return f'combine arguments into one {a*b if a>b else a/b }' 

import functools
def partialFn(arg1, arg2):
    return int(arg1)* float(arg2)

# closure concept for the free variable and nonlocal vraibale concept 
def count():
    list_= list()
    def sum_count(val):
        list_.append(val) #list_, a free variable 
        total= sum(list_)
        return total 
    return sum_count 

count1= count() 

def make_avg():
    count, total=0, 0 

    def avg(new_val):
        nonlocal count, total 
        count+=1
        total+= new_val 
        return total/count 
    return avg 

test_avg= make_avg() 

class Test_1:
    def __init__(self,name):
        self.name= name 
    
    def __call__(self): #need to use __call__ 
        self.name() 

@Test_1
def write_again():
    print('OK!') 

# decorator outside the class and use self and wrapper function 
def outsider_fn(fn):
    def wrapper(self, age):
        age= age+1
        return fn(self,age)
    return wrapper 

class Age(object):
    def __init__(self):
        self.adultAge= 20
    @outsider_fn
    def add_age(self, age):
        print('my age is {} in 2020'.format(self.adultAge + age)) 

# decorator use @property, @staticmethod, @classmethod 
class Test:
    def __init__ (self, first, last, age):
        self._firstName= first
        self._lastName= last 
        self.age= age 
        self.city= 'berlin'

    @property 
    def get_email(self):
        return f'{self._firstName}-{self._lastName}@gmail.com'
    @get_email.setter
    def change_email(self, new_name):
        self._firstName=new_name
        # return f'{self._firstName}-{self._lastName}@gmail.com' 

    @staticmethod  
    def write(x):
        return f'just test plain staticmethod in class scope - {x}'
    
    @classmethod 
    def test_fullname(cls, first, last, age):
        return f'fullname is {first} {last}' 
    @classmethod 
    def rewrite(cls,x):
        return cls.write(x) + '!'
    @classmethod 
    def test(cls,x):
        cls.city='space'
        return f'anther city life in {cls.city}, well {cls.write(x)}'

# use functools.wraps 
from functools import wraps 
'''
# the helper function 
def decorator(fn):
    #the functool.wraps is a tool to copy the wrapped function's infos,like the docstring 
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
            func_name= func.__name__ 
            start= time.perf_counter() #measure program run time 
            value= func(*args, **kwargs)
            end= time.perf_counter() 
            run_time= end-start 

            print(f"Finished {func.__name__!r} in {run_time:.2f} secs") 
        except Exception:
            pass 
        return value
    return wrapper 

@timer 
def time_recored(time):
    for _ in range(time):
        sum([i**2 if i %2 !=0 else i for i in range(10000)]) 

#extra- mix the conditions 
def test_call(have_call):
    def wrapper(*args): 
        from datetime import datetime 
        if 5<datetime.now().hour<20: 
            return have_call(*args)
        else:
            print('Good Night then!') 
    return wrapper

@test_call
def call(name, city):
    return ('halo {}, whom lives in {}'.format(name, city)) 
# test_call(call)() 

# use the function as the condtion 
def test_con(a,x,y):
    def fn1(x):
        return f'the condtion one {x}'
    def fn2(y):
       return f'the condtion two {y}' 
    if a=='ok':
        return fn1(x) 
    else:
        return fn2(y)


if __name__=='__main__':
    print(call_anything(1,2)) #should be 1/2
    print(write('halo')) 
    print(functools.partial(partialFn, 1.00005)(1.12))
    print(count1(10))
    print(count1(20))  #should be 30 
    print(test_avg(10)) 
    print(test_avg(20)) #should be 15 
    write_again() 
    testAge= Age()
    testAge.add_age(8) 
    person= Test('chloe','ji',28)
    person.change_email='emily'
    print(person.get_email) 
    print(person.write('combine english yet maths to compile so called algorithm')) 
    print(Test.test_fullname) #bound method of Test
    print(Test.test_fullname('emma','ji', 28))
    print(Test.rewrite('extract abstract')) 
    print(Test.test('craft')) 
    time_recored(100) 
    print(call('emma', 'foresttown')) 
    print(test_con('ok','TESTING','PLAYING')) 

# decorator return decorator TODO 