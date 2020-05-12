"""
change object behaviors based on states
"""


from abc import ABC, abstractmethod

class Seasons(ABC):
    # all the methods will do the same behaviors based on state

    @abstractmethod
    def commute(self):
        pass

    @abstractmethod
    def wear(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Summer(Seasons):
    def __init__(self, loc: str, tool: str, cloth: str, food: str)-> None:

        self.loc = loc
        self.tool = tool
        self.cloth = cloth
        self.food = food

    def commute(self):
        print(f"by {self.tool} at {self.loc}")

    def wear(self):
        print(f"wear {self.cloth}")

    def eat(self):
        print(f"eat {self.food}")


class Winter(Seasons):
    def __init__(self, tool: str, cloth: str, food: str, loc: str = "space")-> None:
        
        self.loc = loc
        self.tool = tool
        self. cloth = cloth
        self. food = food

    def commute(self):
        print(f"by {self.tool} at {self.loc}")

    def wear(self):
        print(f"wear {self.cloth}")

    def eat(self):
        print(f"eat {self.food}")

class Person(Seasons):

    def __init__(self, state: str)-> None:
        self._state = state

    def set_state(self, state: str)-> None:
        self._state = state

    def commute(self):
        return self._state.commute()

    def wear(self):
        return self._state.wear()

    def eat(self):
        return self._state.eat()


if __name__ == "__main__":
    summer = Person(Summer("earth", "bike", "t-shirt", "ice cream"))
    winter = Person(Winter("walk", "jacket", "hot pot"))
    print(summer.commute())
    print(summer.wear())
    print(summer.eat())
    print(winter.commute())
    print(winter.wear())
    print(winter.eat())