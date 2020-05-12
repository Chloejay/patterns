"""
when two classes share the same behaviors, then use tempate pattern to generalize to one class,
abstract superclass
"""


from abc import ABC, abstractmethod

class Result(ABC):
    # hold template methods
    def get_result(self):
        self.do()
        self.sports()
        self.work()
        self.relax()

    # abstract method
    @abstractmethod
    def do(self):
        pass

    @abstractmethod
    def sports(self):
        pass

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def relax(self):
        pass

# concrete class one 
class Person_Extrovert(Result):
    def __init__(self, who: str, what: str, field: str, hobby: str)-> None:
        self._who = who
        self.what = what
        self.field = field
        self.hobby = hobby

    def do(self):
        print(f"{self._who} a is doing")

    def sports(self):
        print(f"{self.what} is a group sports")

    def work(self):
        print(f"work in {self.field}")

    def relax(self):
        print(f"maybe go to {self.hobby}")

# concrete class two 
class Person_Introvert(Result):
    def __init__(self, who: str, what: str, field: str, hobby: str)-> None:
        self._who = who
        self.what = what
        self.field = field
        self.hobby = hobby

    def do(self):
        print(f"{self._who} is doing")
    def sports(self):
        print(f"{self.what} is a solo sports")

    def work(self):
        print(f"communicate with {self.field}")

    def relax(self):
        print(f"go for {self.hobby}")



if __name__ == "__main__":
    typeA = Person_Extrovert("extrovertA", "basketball", "communication", "ktv")
    typeB = Person_Introvert("introvertB", "biking", "code", "hiking") 
    typeA.get_result()
    print("----"*20)
    typeB.get_result()