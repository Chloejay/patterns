'''
when to use: to fix the mismatch and incompatibility of interfaces. 
multiple classes have similar property, but different behaviors, by inheritate generalClass 
and adapte class's implementation, the concept of duck typing.  

two types of adapter (aka.wrapper):
- class adapter uses multiple inheritance to adapt one interface to another
- object adapter uses encapsulation and relies on object composition 

Resource: 
# https://www.giacomodebidda.com/adapter-pattern-in-python/ 
# http://ginstrom.com/scribbles/2009/03/27/the-adapter-pattern-in-python/
# http://python-history.blogspot.com/2010/06/method-resolution-order.html 
'''

from abc import ABC, abstractmethod 


class FakeCity(ABC): 
    def __init__(self, site: str):
        self.site= site 

    @abstractmethod 
    def spacetravel(self):
        raise NotImplementedError('add concret behaviors ....') 

class Mountain(FakeCity):
    def __init__(self,site: str):
        self.site = site

    def spacetravel(self):
        return f'space travel in {self.site}' 

class Ocean(object):
    def __init__(self, site: str):
        self.site = site

    def swim(self):
        return f'ocean swim in {self.site}' 

#use object adapter, adapt the interface of its parent's class and return adaptee's function 
class ObjectAdapter(FakeCity):
    def __init__(self, site):
        self.site= site

    def spacetravel(self):
        return self.site.travel() 

    def __getattr__(self, attr: str)-> str: 
        return getattr(self.site, attr)

# abstract common interface 
class OceanAdapter(Ocean, FakeCity):
    def __init__(self, site):
        Ocean.__init__(self, site) 

    def spacetravel(self):
        return self.swim() 



if __name__=='__main__':
    mountain= Mountain('everest') 
    ocean= OceanAdapter('riviera') 
    oceanObj= ObjectAdapter(Ocean('riviera_site'))
    print(mountain.spacetravel())
    print(ocean.spacetravel()) 
    print(oceanObj.swim())  
    