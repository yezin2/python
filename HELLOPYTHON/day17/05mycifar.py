import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models
import cv2
 
cifar10 = datasets.cifar10 
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
 
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
 
train_images = train_images.reshape((50000, 32, 32, 3))
test_images = test_images.reshape((10000, 32, 32, 3))

# for i,img in enumerate(train_images):
#     print("train : ",i)
#     cv2.imwrite("img_cf_train/"+str(i)+"_"+str(train_labels[i][0])+".png", img)
#     if i >= 99:
#         break
#
# for i,img in enumerate(test_images):
#     print("test : ", i)
#     cv2.imwrite("img_cf_test/"+str(i)+"_"+str(test_labels[i][0])+".png", img)
#     if i >= 99:
#         break

train_images = train_images/255.0
test_images = test_images/255.0

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10)

img = cv2.imread('test_img.jpg', cv2.IMREAD_COLOR)
img_32 = cv2.resize(img, dsize=(32, 32))

cv2.imshow('testimage_img32', img_32)
# cv2.imshow('testimage_test', test_images[0])

img_32 = img_32.reshape((1, 32, 32, 3))

predictions = model.predict(img_32)

print(np.argmax(predictions), class_names[np.argmax(predictions)]) #class_names[np.argmax(predictions)]