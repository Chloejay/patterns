'''
facade: information hiding, encapsulation, separate of conerns
'''

# subsystem(complex part)
class Mind(object):

    def __init__(self, think)->None:
        self._think = think 

    def talk(self, v:str)->str:
        if v == "secret":
            return f"{self._think}"
        else:
            return "viola, this is fake."

    def act(self, state:str)->str:
        if state: 
            return f"{self._think} at {state}"
        else:
            return "work on progress, please wait!"

# facade character (wrap complex part)
class Facede_Role(object):

    def __init__(self, thought: Mind)->None:
        self._thought = thought 

    def ops(self)->str:
        res = list() 
        res.append("start to infer human action")
        res.append(self._thought.talk("secret")) 
        res.append("after talk is action stage")
        res.append(self._thought.act("doing")) 
        res.append("or wait?") 
        res.append(self._thought.act(None))
        return (("\n").join(res))  

# request service 
def energy_consume(vibration: Facede_Role)->str:
    return vibration.ops() 


if __name__ == "__main__":

    particle = Mind("abstraction is another concrete") 
    record = Facede_Role(particle)
    print(energy_consume(record))