import random
import numpy as np

print("Heloo")
class NeuralNetwork(object):
    def __init__(self, x):
        self.input = x
        self.weights1   = np.random.rand(self.input.shape[1],4) 
        self.weights2   = np.random.rand(4,1)                 
        self.y          = y
        self.output     = np.zeros(y.shape)
    def yes(self):
        pass