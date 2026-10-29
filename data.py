from typing import TypeVar, Generic

# 1. Déclarer la variable de type
T = TypeVar('T')

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
            print(elmts.tostring() + ", ")
        print(self.output.tostring())