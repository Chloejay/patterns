'''inheritance: OOP the object inherit attributes and behaviors from base class without needing to implementing again. 
super() let call methods originate from the base class to 'pollute' subclass, can take two parameters (subclass,an 
instance of subclass)
http://python-history.blogspot.com/2010/06/method-resolution-order.html from Guido 
'''

class Dream(object):
    def __init__(self, dream):
        self._dream= dream
        self._work= 'design'

class Work(Dream):
    def __init__(self, dream):
        super().__init__(dream)
        self._work='work'

    @property 
    def work(self):
        return self._work

    @work.setter 
    def work(self, new_work):
        self._work= new_work 

class Lazy(Dream):
    def __init__(self, dream):
        super().__init__(dream) 
        
#multiply inheritance 
class Book:
    def __init__(self,name):
        self.name= name
        self.page=0

    def bookmark(self, new_page):
        return f'mark {new_page} page'

class Novel(Book):
    def __init__(self, name, booktype):
        self.booktype= booktype
        super().__init__(name) 
    
    def categorize(self):
        return f'{self.name} is being categoried into {self.booktype}' 

class Adventure(Novel, Book): #mro 
    def __init__(self, name, booktype, desc):
        self.desc= desc 
        # super().__init__(name, booktype) 
        super(Adventure, self).__init__(booktype, name) 

    def read_book(self):
        return f'read book {self.name} about {self.desc}' 

def main():
    Work.work='coder'
    print(Work.work) 
    if issubclass(Adventure, Novel): 
        print(Adventure.__mro__)
        print(Novel.__mro__) 
        test=Adventure('inito the wild','non-fiction','"go solo"') 
        print(test.read_book())
        print(test.categorize()) 
        print(test.bookmark('last_page')) #auto 
        

if __name__=='__main__':
    main()  
