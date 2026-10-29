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
    dataset: list
    weights: list

    def __init__(self, learning_rate, dataset):
        self.learning_rate = learning_rate
        self.dataset = dataset
        for i in range(len(self.dataset[0])-1):
            self.weights[i] = 0
