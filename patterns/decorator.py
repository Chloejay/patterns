'''
decorator pattern, inpired by GoF book. illustrated the decorators in three parts
- object (function and class) in clsoure style 
- @property, @staticmethod and @classmethod 
- built in packages functools.wraps() 

why? (use decorator)- @decorator is just the shortcut for the fn=@decorator(fn), its behavior is to replace the decorated function with a new function, 
that accepts the same args and return the value; keep the code more DRY and extend functionality with more ease and flexibility, without inheritance. 
keep in mind, decorator is just the `wrapper`, kind of closure type, which just extend the functions in a mask way
'''

# fn return fn, used concept closure, to attach additional reponsibilities to an object dynamically 
def call(fn): 
    def text(msg):
        return fn(msg)
    return text 

@call    
def write(msg):
    return (f'the morning msg is {msg}')  

# use optional args or kwargs 
def call_1(fn):
    def text_1(*args, **kwargs):
        return fn(*args, **kwargs)
    return text_1

@call_1
def write_1(msg, msg2, msgn):
    return ('this is the test msg {}-{}-{}'.format(msg, msg2, msgn)) 
# can make the fn return fn more nested (chain rule)

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

# decorator outside the class and use self and wrapper fn 
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

    @staticmethod #a plain fn just in the scope of the class building block 
    def write(x):
        return f'just test {x}'
    
    @classmethod 
    def test_fullname(cls, first, last, age):
        return f'fullname is {first} {last}' 
    @classmethod 
    def rewrite(cls,x):
        return cls.write(x) + '!'
    @classmethod 
    def test(cls):
        cls.city='shanghai'
        return f'anther city life in {cls.city }'

# use functools.wraps 
from functools import wraps 
'''
# the helper functions 
def decorator(fn):
    #the functool.wraps is a tool to copy the wrapped fns's infos,like the docstring 
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
        func_name= func.__name__ 
        start= time.perf_counter() #measure time interval for the program run time 
        value= func(*args, **kwargs)
        end= time.perf_counter() 
        run_time= end-start 

        print(f"Finished {func.__name__!r} in {run_time:.2f} secs")
        return value
    return wrapper 

@timer 
def save_time(time):
    for _ in range(time):
        sum([i**2 for i in range(10000)])

#spolier- mix the conditions 
def test_call(have_call):
    def wrapper(*args, **kwargs): 
        from datetime import datetime 
        if 5<datetime.now().hour<20: 
            have_call(*args, **kwargs)
            return have_call(*args, **kwargs)
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
    print(write('halo') ) 
    print(write_1('halo', 'gut_nacht', 'blalala')) 
    print(count1(10))
    print(count1(20))  #should be 30 
    print(test_avg(10) ) 
    print(test_avg(20) ) #should be 15 
    write_again() 
    testAge= Age()
    testAge.add_age(8) 
    person= Test('chloe','ji',28)
    person.change_email='emily'
    print(person.get_email) 
    print(person.write('english and maths to compile the so called algorithm')) 
    print(Test.test_fullname) #bound method of Test
    print(Test.test_fullname('emma','ji', 28))
    print(Test.rewrite('extract abstract')) 
    save_time(100) 
    print(call('emma', 'shanghai') ) 
    print(test_con('ok','TESTING','PLAYING')) 
    

