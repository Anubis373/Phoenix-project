from math_network import *


class Neuron:
    weighted_sum: float
    return_value: float
    weights: list[float]
    bias: float

    def __init__(self, size: int):
        self.weighted_sum = 0
        self.weights = [0] * size
        self.return_value = 0
        self.bias = 1

    def linear_sum(self, inputs: list[float]):
        self.weighted_sum = 0
        for i in range(len(inputs)):
            self.weighted_sum += self.weights[i] * inputs[i]
        self.weighted_sum += self.bias
        return(self.weighted_sum)

    def activate(self):
        self.return_value = sigmoid(self.weighted_sum)
        return self.return_value

    def process(self, inputs: list[float]):
        self.linear_sum(inputs=inputs)
        return self.activate()
