#! /usr/bin/env python

'''
visitor pattern creates new operations by adding new subclass to hierarchy, without altering base class. 

from GoF UML, concretVisitor class override Visitor Class operations to implement visitor-specific behaviors
for the ConcretVisitable class, and once AbstractVisitable accept visitor, it sends an request to 
ConcretVisitor elements and encode visitor's code.  
'''

from abc import ABC, abstractmethod 


class AbstractVisitor(ABC):
    
    @abstractmethod 
    def visit_Int(self): 
        pass
    def visit_ConcretVisitableAdd(self):
        pass 

class ConcretVisitorA(AbstractVisitor):
    # each visit operation on Visitor declare its argument to be a particular ConcretElement 
    def visit_Int(self, v): #v, a particular element from VistableElement 
        return v.a

    def visit_ConcretVisitableAdd(self, v):
        return f'{self.__class__.__name__} add result is {v.a.accept(self) + v.b.accept(self)}'

class ConcretVisitorB(AbstractVisitor): # visitable can accept different visitor datatype 
    def visit_Int(self, v):
        return v.a

    def visit_ConcretVisitableAdd(self, v):
        return f'{self.__class__.__name__} add result is {v.a.accept(self) + v.b.accept(self) + int(10.00001)}'

class ConcretVisitorC(AbstractVisitor):
    def visit_Int(self, v):
        return v.a

    def visit_ConcretVisitablePow(self, v):
        return f'{self.__class__.__name__} pow result is {v.a.accept(self) ** v.b.accept(self) }'

#object structure (concept from GoF)
class VisitableElement: 
    # define an accept operation that take visitor as argument 
    def accept(self, visitor):
        val = 'visit_{}'.format(self.__class__.__name__) 
        visitorInstance = getattr(visitor, val) #getattr(object,'x')== object.x  
        return visitorInstance(self) 

class Int(VisitableElement):
    def __init__(self, a):
        self.a = a

class ConcretVisitableAdd(VisitableElement):
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
class ConcretVisitablePow(VisitableElement):
    def __init__(self, a, b):
        self.a = a
        self.b = b



if __name__ == '__main__':
    output1  = ConcretVisitableAdd(Int(1),Int(2)).accept(ConcretVisitorA())
    output2  = ConcretVisitableAdd(Int(1.5),Int(2)).accept(ConcretVisitorB()) 
    output3  = ConcretVisitablePow(Int(1/2),Int(1/2)).accept(ConcretVisitorC()) 
    list_ = [output1, output2, output3]
    for output in list_:
        print(output) 