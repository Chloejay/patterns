# __bool__, __add__, __sub__, __mul__, __call__ 

class Test:
    def __init__(self, val):
        self._val= val 

    def __bool__(self):
        if self._val %2 !=0:
            return True 
        else:
            return False 

    def __radd__(self, val2):
        return self._val +val2 

    def __mul__(self, val3):
        return self._val *val3

    def __len__(self):
        return self._val

    def __call__(self):
        self._val+=2
        return f'{self._val} get called'

if __name__=='__main__':
    test= Test(2)
    print(bool(test) ) 
    print(1+test) 
    print(test*2) 
    print(len(test))
    print(test()) 