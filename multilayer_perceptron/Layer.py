from multilayer_perceptron.Neuron import Neuron


class Layer:
    neurons: list[Neuron]
    outputs: list[float]

    def __init__(self, neuron_count: int, input_size: int):
        self.neurons = []
        for i in range(neuron_count):
            self.neurons.append(Neuron(input_size))
        self.outputs = []

    def compute(self, inputs):
        for neuron in self.neurons:
            self.outputs.append(neuron.process(inputs))
        