class Human:
    
    old_age = 28

    def __init__(self, first, last, age):
        self._firstName = first
        self._lastName = last
        self._age = age 

    @property 
    def get_email(self):
        if self._firstName !='chloe':
            raise 
        return f'{self._firstName}_{self._lastName}@gmail.com'  
        
    @property 
    def get_perosn(self):
        return f'name is {self._lastName} and age is {self._age}' 

    def increase_amt(self):
        self._age = self._age + self.old_age
        return self._age 
