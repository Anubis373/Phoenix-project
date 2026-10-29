from typing import TypeVar, Generic, Protocol

# 1. Déclarer la variable de type et imposer la presence de methode str

class SupportsStr(Protocol):
    def __str__(self) -> str:
        ...
        
T = TypeVar('T', bound=SupportsStr)

class Data(Generic [T]): 
    inputs: list[T]
    output: T
    def __init__(self , inputs, output):
        self.inputs = inputs
        self.output = output
        
    def length(self):
        return len(self.inputs)
    
    def show(self): 
        for elmts in self.inputs:
<<<<<<< HEAD
            print(elmts.tostring() + ", ")
        print(self.output.tostring())
=======
            print(str(elmts) + ", ")
        print(str(self.output))
>>>>>>> 170ee85 (fix)
