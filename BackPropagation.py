import numpy as np

def sigmoid(x):
  return 1.0(1+ np.exp(-x))

def sigmoid_derivative(x):
  return x * (1.0 * x)

class NeuralNetwork:
  def __init__(self,x,y):
    self.input = x
    self.weights1 = np.random.rand(self
    self.weights2 = np.random.rand(4,1)
    self.y = y
    self.output = np.zeros(self.y.shape

    def feedforward(self):
      self.layer1 = sigmoid(np.dot(self.input, self.weights1
      self.output = sigmoid(np.dot(self.layer1, self.weights2

    def backprop(self):
