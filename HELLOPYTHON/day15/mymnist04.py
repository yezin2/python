from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
import numpy as np
import cv2

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(test_labels[0])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255


train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

model = models.Sequential() #신경망
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images, train_labels, epochs=5, batch_size=128)

predictions = model.predict(test_images)

for i,img in enumerate(test_images):
    if test_labels[i] == predictions[i]:
        cv2.imwrite('miss/' + str(i) +'_'+ str(test_images[i]) +'.png', img)
print(np.argmax(predictions[0]))





predictions = model.predict(test_images)

cnt_o = 0
cnt_x = 0
for idx,pred in enumerate(predictions):
    mypred = np.argmax(pred)
    mygool = np.argmax(test_labels[idx])
    if mypred == mygool:
        cnt_o += 1
    else:
        cnt_x += 1
        cv2.imwrite("miss/"+str(idx)+"_"+str(mypred)+"_"+str(mygool)+".png", test_images[idx])
    print("mypred : ", mypred)
    print("mygool : ", mygool)