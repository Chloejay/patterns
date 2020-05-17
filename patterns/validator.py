#! /usr/bin/env python

#build class independently, let inheritance discover itself 

from abc import ABC, abstractmethod 

class Validator(ABC):
    def __set_name__(self, name):
        self._private_name = f'_{name}' 

    def __get__(self, obj, objtype= None):
        return getattr(obj, self._private_name)
    
    def __set__(self, obj, val):
        self.validate(val)
        setattr(obj, self._private_name, val) 

    @abstractmethod
    def validate(self, val):
        pass 

class Num(Validator):

    def __init__(self, small= None, large= None):
        self.small = small
        self.large = large 

    def validate(self, val):

        if not isinstance(val, (int, float)):
            raise TypeError('Excpected variable type is int and float')
        if self.small is not None and val < self.small:
            raise ValueError (f'{val} is too small')
        if self.large is not None and val > self.large:
            raise ValueError (f'{val} is too large') 

class String(Validator):

    def __init__(self, small_len= None, large_len= None, pred= None):
        self.small_len = small_len
        self.large_len = large_len
        self.pred = pred

    def validate(self, val):

        if not isinstance(val, str):
            raise TypeError('Expected variable type is str')
        if self.small_len is not None and len(val) < self.small_len:
            raise ValueError(f'{val} is too small')
        if self.large_len is not None and len(val) > self.large_len:
            raise ValueError(f'{val} is too large')
        if self.pred is not None and not self.pred(val):
            raise ValueError ('wrong val') 



if __name__ == '__main__':
    number = Num(10, 20)
    string = String(10, 40)
    number.validate(30) #ValueError: 30 is too large  
    string.validate('dasistgut') #ValueError: dasistgut is too small