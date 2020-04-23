import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

data = keras.datasets.fashion_mnist

# All input data is images that are 28x28 pixels: [[a,a,a, x 28]],[], ... x28] = 784 inputs
(train_image, train_labels), (test_images, test_labels) = data.load_data()
# there will be 784 input neurons and 10 outputs:
# this are the different types of data that the network is going to return:
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# the hidden layer is going to have 128 neurons: we can have more bias and weights
# usually the number_neurons_hidden_layers = 15-20% of the number_neurons_input
train_image = train_image / 255.0
test_images = test_images / 255.0
model = keras.Sequential([
    # The input layer 28*28, I flat it:
    keras.layers.Flatten(input_shape=(28, 28)),
    # I set the activation functions and the number of hidden layers connected to each layer
    # rectified linear function, very commond
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")  # remove the negative
])
# i set the loss fucntion in order to avaluate the output info related with the good one
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy", metrics=["accuracy"])
# I train it, epochs is the number of times the model is going to see the info
model.fit(train_image, train_labels, epochs=15)

# now I evaluate the model obtein previously
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Test Acc: ", test_acc)

# if I want to play with the model:
prediction = model.predict(test_images)

for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel("Actual: " + class_names[test_labels[i]])
    plt.title("Predicttion: " + class_names[np.argmax(prediction[i])])
    plt.show()
