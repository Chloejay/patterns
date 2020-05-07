'''
composition, compose nested structure to build tree-like structure.
structure: create component interface, implement composit and leaf class.
'''

# class City:
    # def __init__(self, region: str, distance:str)-> None:
        # self.region = region
        # self.distance = distance
#
    # def walk(self)-> str:
        # return f'walk to {self.region} is {self.distance}'
#
# class CityBike(City):
    # def __init__(self, region:str, distance:str, desc:str)-> None:
        # super().__init__(region, distance)
        # self.citywalk = City(region, distance)
        # self.desc = desc
#
    # def bike(self)->str:
        # return f'bike to {self.citywalk.region} is {self.desc}'

# implement with factory method
# interface
from abc import ABC, abstractmethod

class ComponentInterface(ABC):
    def __init__(self, city: str)->None:
        self.city = city

    @abstractmethod
    def unify(self):
        """provides common interface for both composite and leaf classes"""
        pass

# leaf class
class Leaf(ComponentInterface):
    def __init__(self, city: str)->None:
        self.city = city

    def unify(self):
        print(f"single city: {self.city}")

# composite class, children components management interface
class Composite(ComponentInterface):

    def __init__(self, city: str)-> str:
        self.cities = city
        self.allCities = list()

    def unify(self):
        print(f"City by Region: {self.cities}")
        for c in self.allCities:
            c.unify()

    def append_city(self, unit: str)->str:
        self.allCities.append(unit)

    def remove_city(self, unit: str)->str:
        self.allCities.remove(unit)

def main():
    Paris = Leaf("paris")
    Berlin = Leaf("berlin")
    Shanghai = Leaf("shanghai")
    EU = Composite("EU")
    ASIA = Composite("ASIA")
    Earth = Composite("Earth")

    EU.append_city(Paris)
    EU.append_city(Berlin)
    ASIA.append_city(Shanghai)
    Earth.append_city(ASIA)
    Earth.append_city(EU)
    EU.remove_city(Paris)
    Earth.unify()


if __name__ == "__main__":
    # biking = CityBike('forresttown', '10km', 'chill')
    # print(biking.walk())
    # print(biking.bike())
    main()
