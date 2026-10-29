class Data[T]: 
    inputs: list[T]
    output: T
    def __init__(self , inputs, output):
        self.inputs = inputs
        self.output = output