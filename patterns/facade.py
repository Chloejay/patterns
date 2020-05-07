'''
facade: information hiding, encapsulation, separate of conerns
'''

# subsystem(complex part)
class Mind:

    def __init__(self, think: str)->None:
        self._think = think

    def talk(self, v: str)->str:
        if v == "secret":
            return f"{self._think}"
        return "viola, this is fake."

    def act(self, state: str)->str:
        if state:
            return f"{self._think} at {state}"
        return "work on progress, please wait!"

# facade character (wrap complex part)
class FacadeRole:

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
        return ("\n").join(res)

# request service
def energy_consume(vibration: FacadeRole)->str:
    return vibration.ops()


if __name__ == "__main__":

    PARTICLE = Mind("abstraction is another concrete")
    RECORD = FacadeRole(PARTICLE)
    print(energy_consume(RECORD))