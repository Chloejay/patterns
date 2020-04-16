'''
composition, favor over inheritance, especially in FP. 
why? DRY (code reuse). 

composite has a composite/wrapper class, creates a "has a" relationship. 
https://lwn.net/Articles/787800/
https://stackoverflow.com/questions/5334353/when-should-i-use-composite-design-pattern
'''


class City:
    def __init__(self, region: str, distance:str)-> None:
        self.region = region
        self.distance = distance 

    def walk(self)-> str:
        return f'walk to {self.region} is {self.distance}' 

class CityBike(City):
    def __init__(self, region:str, distance:str, desc:str)-> None:
        super().__init__(region, distance) 
        self.citywalk = City(region, distance) 
        self.desc = desc

    def bike(self)->str:
        return f'bike to {self.citywalk.region} is {self.desc}'

# TODO, implement with factory method 

if __name__ == '__main__':
    biking = CityBike('forresttown', '10km', 'chill')
    print(biking.walk())
    print(biking.bike())  
