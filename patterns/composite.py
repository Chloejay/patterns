'''
composition, used together with inheritance for code reuse. 
composite has the composite or wrapper class, component that is being wrapped, aka "wrapee". 
composition creates a "has a" relationship. 
https://lwn.net/Articles/787800/
https://stackoverflow.com/questions/5334353/when-should-i-use-composite-design-pattern
'''


class City:
    def __init__(self, region, distance):
        self.region= region
        self.distance= distance 

    def walk(self):
        return f'walk to {self.region} is {self.distance}' 

class CityBike(City):
    def __init__(self, region, distance, desc):
        super().__init__(region, distance) 
        self.citywalk= City(region, distance) 
        self.desc= desc

    def bike(self):
        return f'bike to {self.citywalk.region} is {self.desc}'

# TODO, can implement with factory method 

if __name__=='__main__':
    test= CityBike('forresttown', '10km', 'chill')
    print(test.walk())
    print(test.bike() )  
