from Layer import Layer


class Network:
    layers: list[Layer]

    def __init__(self, layer_sizes:list[int], input_size: int):
        self.layers = []
        for i in range(len(layer_sizes)):
            if(i == 0):
                self.layers.append(Layer(layer_sizes[0], input_size))
                continue
            self.layers.append(Layer(layer_sizes[i], layer_sizes[i-1]))

    def compute(self, inputs: list):
        current = inputs
        for layer in self.layers:
            layer.compute(current)
            current = layer.outputs
        return current
