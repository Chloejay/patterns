class Human:
    old_age=28
    def __init__(self, first, last, age):
        self._firstName= first
        self._lastName= last
        self._age= age 

    @property 
    def get_email(self):
        if self._firstName !='chloe':
            raise 
        return('{}_{}@gmail.com'.format(self._firstName, self._lastName)) 
        
    @property 
    def get_perosn(self):
        return ('name is {} and age is{}'.format(self._lastName, self._age))

    def increase_amt(self):
        self._age= self._age +self.old_age
        return self._age 
