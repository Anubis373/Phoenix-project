from data import Data


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
        if(sum >= 0):
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
        self.weights = [0] * self.dataset[0].length()

    def show_details(self):
        print(f"Learning rate: {self.learning_rate}")
        print(f"Weights : ")
        for i in range(len(self.weights)):
            print(f"Weight {i} = {self.weights[i]}")
#        for data in self.dataset:
#            data.show()

    def train(self):
        total_error = 1
        while total_error > 0:
            total_error = 0
            for example in self.dataset:
                neuron = Neuron(example.inputs, self.weights, self.bias)
                result = neuron.compute_inputs()
                total_error += abs(example.output - result)
                #  self.show_details()
                self.update_weights(example=example, actual=result)

    def update_weights(self, example: Data, actual):
        for i in range(len(self.weights)):
            self.weights[i] += self.learning_rate * (example.output - actual) * example.inputs[i]
            self.bias += self.learning_rate * (example.output - actual)
