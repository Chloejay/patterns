'''
when to use: to fix the mismatch and incompatibility of the interfaces. 
multiple classes have similar property, but different behaviors, by inheritate generalClass inheritance 
and adaptee class's implementation. 

two types of adapter (aka.wrapper):
- class adapter uses multiple inheritance to adapt one interface to another
- object adapter uses encapsulation and relies on object composition 

Resource: 
# https://www.giacomodebidda.com/adapter-pattern-in-python/ 
# http://ginstrom.com/scribbles/2009/03/27/the-adapter-pattern-in-python/
# http://python-history.blogspot.com/2010/06/method-resolution-order.html 
'''

from abc import ABC, abstractmethod 


class City(ABC): 
    def __init__(self, site):
        self.site= site 

    @abstractmethod 
    def spacetravel(self):
        raise NotImplementedError('add concret behaviors ....') 

class Mountain(City):
    def __init__(self,site):
        self.site = site

    def spacetravel(self):
        return f'space travel in {self.site}' 

class Ocean:
    def __init__(self, site):
        self.site = site

    def swim(self):
        return f'ocean swim in {self.site}' 

# to abstract the common interface 
class OceanAdapter(City, Ocean):
    def __init__(self, site):
        Ocean.__init__(self, site) 

    def spacetravel(self):
        return self.swim() 

#use object adapter, adapt the interface of its parent's class and return adaptee's function 
class ObjectAdapter(City):
    def __init__(self, site):
        self.site= site

    def spacetravel(self):
        return self.site.travel() 

    def __getattr__(self, attr): 
        return getattr(self.site, attr)


if __name__=='__main__':
    mountain= Mountain('everest') 
    ocean= OceanAdapter('riviera') 
    oceanObj= ObjectAdapter(Ocean('riviera_site'))
    print(mountain.spacetravel())
    print(ocean.spacetravel()) 
    print(oceanObj.swim())  
    