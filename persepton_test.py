from perceptron import *

and_gate_list = [
    Data([0, 0], 0),
    Data([0, 1], 1),
    Data([1, 0], 1),
    Data([1, 1], 0)
]
learner = Learner(1, and_gate_list)
learner.train(10)
neuron = Neuron(inputs=[0, 0], weights=learner.weights, bias=learner.bias)
print(neuron.compute_inputs())
