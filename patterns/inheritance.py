#! /usr/bin/env python

'''inheritance: OOP the object inherit attributes and behaviors from base class without needing to implementing again. 
super() let call methods originate from the base class to 'pollute' subclass, can take two parameters (subclass,an 
instance of subclass)
http://python-history.blogspot.com/2010/06/method-resolution-order.html from Guido 
'''

class Dream(object):
    def __init__(self, dream):
        self._dream = dream
        self._work = 'design'

class Work(Dream):
    def __init__(self, dream):
        super().__init__(dream)
        self._work = 'work'

    @property 
    def work(self):
        return self._work

    @work.setter 
    def work(self, new_work):
        self._work = new_work 

    @work.deleter
    def work(self):
        del self._work 

class Lazy(Dream):
    def __init__(self, dream):
        super().__init__(dream) 
        
#multiply inheritance (MRO)
class Book:
    def __init__(self,name):
        self.name = name
        self.page = 1

    def bookmark(self, new_page):
        return f'mark {new_page} page'

class Novel(Book):
    def __init__(self, name, booktype):
        self.booktype = booktype
        super().__init__(name) 
    
    def categorize(self):
        return f'{self.name} is being categoried into {self.booktype}' 

class Adventure(Novel, Book): 
    def __init__(self, name, booktype, desc):
        self.desc= desc 
        # super().__init__(name, booktype) 
        super(Adventure, self).__init__(booktype, name) 

    def bookmark(self):
        return f'read book {self.name} about {self.desc} at {self.page}' 

def main():
    Work.work = 'coder'
    print(Work.work) 
    if issubclass(Adventure, Novel): 
        print(Adventure.__mro__)
        print(Novel.__mro__) 
        novel=Novel('women on the train','non-fiction')
        print(novel.bookmark('last_page')) 
        test=Adventure('into the wild','non-fiction','"go solo"') 
        print(test.bookmark())
        print(test.categorize()) 

if __name__ == '__main__':
    main()