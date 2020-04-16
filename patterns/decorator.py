'''
decorator pattern, inspired by GoF book. decorator is illustrated in three parts
- object (function and class) in closure style 
- @property, @staticmethod and @classmethod 
- built in packages functools.wraps() 

why?
@decorator is shortcut for fn=@decorator(fn), its behavior is to replace the decorated 
function with a new callable object, which accepts the same args and return related value 
multiply times, keep code DRY and extend functionality with more flexibility, without 
inheritance, decorator is just the `wrapper`, kind of closure type. 
'''

# closure and wrapper  
from typing import Iterable
from functools import wraps, partial

def wrap_single_args(fn): 
    # @wraps(fn)
    def text(*msg):
        return fn(*msg) 
    return text 

@wrap_single_args  
def write(msg, msg2):
    return f'the morning msg is {msg}->{msg2}' 

class WriteClass:
    @wrap_single_args
    def write(self, msg, msg2):
        return f'test decorator class {msg}->{msg2}' 

# use variable_args[kwargs]  
def wrapper_outside(fn_call_inside_wrapper):
    def wrapper(*args, **kwargs):
        return fn_call_inside_wrapper(*args, **kwargs)
    return wrapper 

@wrapper_outside 
def call_anything(a:int, b:int)-> Iterable[str]:
    return f'combine arguments into one {a*b if a>b else a/b }' 

def partialFn(arg1, arg2):
    return int(arg1)* float(arg2)

# closure concept for the free variable and nonlocal variable concept 
def count():
    list_ = list()

    def sum_count(val):
        list_.append(val) #list_, a free variable 
        total = sum(list_)
        return total 

    return sum_count 

countInstance = count() 

def make_avg():
    count, total = 0, 0 

    def avg(new_val):
        nonlocal count, total 
        count += 1
        total += new_val 
        return total/count 
    return avg 

avg_instance = make_avg() 

#decorated class   
class Test_1:
    def __init__(self,fn):
        self.fn= fn 
        self.callCount= 0 
    
    def __call__(self, *args): #use __call__ to make class callable 
        self.callCount+= 1
        self.fn(self.callCount, *args)

@Test_1
def write_again(val, val2):
    print(f'OK! call {val2} for {val} times') 

class Test_2:
    def __init__(self, fn):
        self.fn = fn 

    def __call__(self, *args, **kwargs):
        result = self.fn(*args, **kwargs)
        return result 

@Test_2
def addEle(val:int, val2:int)-> int: 
    print(val, val2)
    return val + val2 

# decorator outside the class and use self and wrapper function 
def outsider_fn(fn):
    def wrapper(self, age):
        age = age + 1
        return fn(self,age)
    return wrapper 

class Age(object):
    def __init__(self):
        self.adultAge = 20
    @outsider_fn
    def add_age(self, age):
        print(f'my age is {self.adultAge + age} in 2020')  

# @property, @staticmethod, @classmethod decorator 
class Test:
    def __init__ (self, first, age, last='ji'):
        self._firstName = first
        self._lastName = last 
        self.age = age 
        self.city = 'town'

    @property 
    def get_email(self):
        try:
            return f'{self._firstName} - {self._lastName}@gmail.com' 
        except AttributeError as e:
            print(str(e)) 

    @get_email.setter
    def get_email(self, new_name):
        self._firstName = new_name 
        # return f'{self._firstName}-{self._lastName}@gmail.com' 

    @get_email.deleter 
    def get_email(self):
        del self._lastName 

    @staticmethod  
    def write(anyVal):
        return f'plain staticmethod in scope - {anyVal}'
    
    @classmethod 
    def fullname(cls, first, last):
        return first + " " + last 

    @classmethod 
    def rewrite(cls, anyVal):
        return f"rewriting {anyVal}" 

    @classmethod 
    def test(cls, val):
        cls.city = 'space'
        return f'{cls.city} by {cls.rewrite(val)}'

# use functools.wraps 
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
            start = time.perf_counter() #measure program run time 
            value = func(*args, **kwargs)
            end = time.perf_counter() 
            run_time = end-start 

            print(f"Finished {func.__name__!r} in {run_time:.2f} secs") 
        except Exception:
            pass 

        return value
    return wrapper 

@timer 
def time_record(time):
    for _ in range(time):
        sum([i**2 if i %2 !=0 else i for i in range(10000)]) 

#extra - mix conditions 
def test_call(have_call):

    def wrapper(*args): 
        from datetime import datetime 
        if 5 < datetime.now().hour < 20: 
            return have_call(*args)
        print('Good Night then!') 
    return wrapper

@test_call
def call(name, city):
    return f'halo {name}, whom lives in {city}'  
# test_call(call)() 

# use function as condition 
def test_con(a, x, y):
    def fn1(x):
        return f'the condition one {x}'
    def fn2(y):
       return f'the condition two {y}' 
    if a == 'ok':
        return fn1(x) 
    else:
        return fn2(y)


if __name__ == '__main__':

    print(call_anything(1,2)) #should be 1/2
    classtest = WriteClass() 
    print(classtest.write('decoratedClass','test'))
    print(write('halo','viola')) 
    print(partial(partialFn, 1.00005)(1.12))
    print(countInstance(10))
    print(countInstance(20))  #should be 30 
    print(avg_instance(10)) 
    print(avg_instance(20)) #should be 15 
    write_again('viola') 
    write_again('viola!!')
    print(addEle(0,1)) 
    testAge= Age()
    testAge.add_age(8) 
    person= Test('chloe',28)
    person.get_email='emily'
    print(person.get_email) 
    print(person.write('WRITING')) 
    print(Test.fullname('emma','ji'))
    print(Test.rewrite('ABSTRACTING')) 
    print(Test.test('craft')) 
    time_record(100) 
    print(call('emma', 'foresttown')) 
    print(test_con('ok','TESTING','PLAYING')) 

# TODO decorator return decorator 
