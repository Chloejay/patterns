'''
Factory pattern, to instantiate the new object in one factory(encapsulation), to keep base class
in a mode of 'close for modification', let subclass to decide which class to instantiate, 
also aka static factory. Along with is the abstract factory, create a interface as objects which 
belonged as one family. 

resource: 
https://krzysztofzuraw.com/blog/2016/factory-pattern-python.html 
https://www.giacomodebidda.com/factory-method-and-abstract-factory-in-python/ 
https://stackoverflow.com/questions/3570796/why-use-abstract-base-classes-in-python
'''

from abc import ABC, abstractmethod 

class Playland(ABC):
    def __init__(self, name, play):
        self._name= name
        self._play= play 

    @abstractmethod 
    def make_play(self):
        pass 

    @abstractmethod 
    def sabotage_play(self):
        pass 

class Dream(Playland):
    def make_play(self):
        return f'{self._name} is play the {self._play}' 

    def sabotage_play(self):
        return f'{self._play}' 

class Habit(Playland):
    def make_play(self):
        return f'{self._name} is play the {self._play}' 
    def sabotage_play(self):
        return f'{self._play}' 

# static factory 
class City(ABC):
    def __init__ (self, city):
        self.city= city 

    @abstractmethod
    def visit(self):
        raise NotImplementedError 

    @staticmethod 
    def visitFactory(type, just_args):
        if type=='train':
            return Train(just_args)
        if type=='bike':
            return Bike(just_args)
        else:
            raise 

class Train(City):
    def visit(self):
        print('visit {} by train'.format(self.city))
    
class Bike(City):
    def visit(self): 
        print('visit {} by bike'.format(self.city)) 


if __name__=='__main__':
    list_=[Dream('emma','designer'),
            Habit('chloe','walking')]

    for l in list_:
        print('test for {}'.format(l.make_play())) 
        print('sabotage the habit {}'.format(l.sabotage_play())) 
    
    print(City.visitFactory('bike', 'foresttown').visit()) 