from data import Data
import numpy
class Neuron:
    output: float
    inputs: list
    weights: list

    def __init__(self, inputs, weights, bias):
        self.output = 0
        self.inputs = inputs
        self.weights = weights
        self.bias = bias

    def compute_inputs(self):
        sum = 0
        for i in range(len(self.inputs)):
            sum += self.inputs[i] * self.weights[i]
        sum += self.bias
        if(sum>=0):
            return 1
        else:
            return 0


class Learner:
    learning_rate: int
    dataset: list[Data]
    weights: list
    bias: float

    def __init__(self, learning_rate, dataset):
        self.learning_rate = learning_rate
        self.dataset = dataset
        self.bias = 1
        self.weights = [self.dataset[0].length()]
        for i in range(self.dataset[0].length()):
            self.weights[i] = 0
    def show_details(self):
        print(f"Learning rate: {self.learning_rate}")
        print(f"Weights : ")
        for i in range(len(self.weights)):
            print(f"Weight {i} = {self.weights[i]}")
    def train(self):
        for example in self.dataset:
            neuron = Neuron(example.inputs, self.weights, 1)  # 1 is the bias
            result = neuron.compute_inputs()
            self.show_details()
            self.update_weights(example=example, actual=result)

    def update_weights(self, example:Data, actual):
        for i in range(len(self.weights)):
            self.weights[i] += self.learning_rate * (example.output - actual) * example.inputs[i]




learner = Learner(1,[Data([1],1)])
learner.show_details()