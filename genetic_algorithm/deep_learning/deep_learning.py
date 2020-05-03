import random
import numpy as np
import math

print("3 neurons in input")
print("4 neurons in hidden layer")
print("1 neurons in output")

# feedpropagation is the calculation of the prediction output
# backpropagation is the update process of change the bias and weights
# loss function let us avaluate the goodness of this predictions (error-real_value)^2 we have to minimize

# the derivative of the loss function with respect to the weights and biases is used to calculate the backpropagation


class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 4)
        self.weights2 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = np.sigmoid(np.dot(self.input, self.weights1))
        self.output = np.sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(
            self.layer1.T, (2*(self.y - self.output) * np.sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * np.sigmoid_derivative(
            self.output), self.weights2.T) * np.sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2
