'''
the hardcore usecase is pub/sub in event streaming system, observer pattern use the one-to-many structure. 
Based on GoF book the Observer has four parts, subject, concretSubject, observer and concretObserver as 
interface and implementation. 'encapsulate interchangable behaviors and use delegation to decide which one to use' 
is the concept mentioned in Head First Design Pattern book. 
'''

from abc import ABC, abstractmethod #use compound patterns 

class Observer(ABC): #aka. subscriber 
    def __init__(self, name):
        self.name= name 

    @abstractmethod 
    def update(self, *args, **kwargs):
        raise NotImplementedError ('implement on the concretClass....') 

class Observer(Observer): #observer 
    def __init__(self,name):
        self.name= name 

    def update(self, *args, **kwargs):
        print('{} gets message {}'.format(self.name, args, kwargs)) 

class ObserverTwo(Observer): #observer 
    def __init__(self,name):
        self.name= name 

    def update(self, *args, **kwargs):
        print('{} gets message also {}'.format(self.name, args, kwargs)) 

class Subject(ABC):
    @abstractmethod 
    def attach(self):
        pass 
    def disatch(self):
        pass
    def notify(self):
        pass 

class ConcretSubject(Subject): #aka. observable/Publisher, the object is being observed, use this as interface 
    def __init__(self):
        self.subscribers=dict() 

    def attach(self, observer, callback=None): #any object can self register to be the observer 
        if callback is None:
             callback= getattr(observer, 'callback_method') #trade-off for multiple attrs 
        self.subscribers[observer]= callback

    def disatch(self, observer): 
        del self.subscribers[observer] 

    def disatch_all(self):
        del self.subscribers

    def notify(self, *message):
        for subscriber, callback in self.subscribers.items():
            callback(*message) 

#use the first-class functions instead of using abstract class 
class SubjectFn(object):
    def __init__(self):
        self.observers= list()
    def attach(self, fn):
        self.observers.append(fn)
        return fn 
    def notify(self, *args, **kwargs):
        for fn in self.observers:
            fn(*args, **kwargs)

class ObseverFn(object):
    def fn(self,*args):
        return f'{args}' 
        

if __name__=='__main__':
    pub= ConcretSubject() 
    observer1= Observer('apple') 
    observer2=ObserverTwo('banana')
    pub.attach(observer1, observer1.update)
    pub.attach(observer2, observer2.update) 
    pub.notify('time is up!','>')
    pub.disatch(observer2)
    # pub.disatch_all() 
    pub.notify('kill one!','<')  
    obj= SubjectFn() 
    observer= ObseverFn() 
    print(obj.attach(observer.fn('ok','viola')))
    