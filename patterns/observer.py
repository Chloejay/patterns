'''
the hardcore of observer pattern is pub/sub originated from event streaming concept, which uses one-to-many structure. 
Based on GoF book Observer has four parts, subject, concretSubject, observer and concretObserver as 
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

class ObserverOne(Observer): #observer 
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

class ConcretSubject(Subject): #aka. observable/Publisher, object is being observed, use this as interface 
    def __init__(self):
        self.subscribers=dict() 

    def attach(self, observer, callback=None): #any object can self register to be observer 
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

#use first-class function instead of using abstract class 
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
        
#implement
class Event:
    _observers=list() 

    def __init__(self, *args):
        self.args= args

    @classmethod 
    def attach(cls, *observer):
        if observer not in cls._observers:
            cls._observers.append(*observer)

    @classmethod 
    def disattch(cls, *observer):
        if observer in cls._observers:
            self._observers.remove(*observer)

    @classmethod 
    def notify(cls, *subject):
        for observer in cls._observers:
            observer(cls(*subject)) 

def observer_test(klass):
    print('{} was written into topic'.format(klass.args))  #fn(cls(subject))

class observer_test2:
    def __call__ (self, klass):
       print('{} was received'.format(klass.args) ) 


def main():
    def callObserver():
        try:
            pub= ConcretSubject() 
            observer1= ObserverOne('apple') 
            observer2=ObserverTwo('banana')
            pub.attach(observer1, observer1.update)
            pub.attach(observer2, observer2.update) 
            pub.notify('time is up!','>')
            pub.disatch(observer2)
            pub.disatch_all() 
            pub.notify('kill one!','<')  
        except AttributeError as e:
            import logging 
            logging.info(e) 
            pass 
    callObserver()

    def callObserver2():
        obj= SubjectFn() 
        observer= ObseverFn() 
        print(obj.attach(observer.fn('ok','viola'))) 
    callObserver2()  

    def callObserver3():
        Event.attach(observer_test)    
        Event.attach(observer_test2())   
        Event.notify('new message')  
        Event.notify('last message') 
    callObserver3() 



if __name__=='__main__':
    main() 

