import tensorflow as tf
import numpy as np
import cv2

# class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
#                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images_re = train_images / 255.0
test_images_re = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images_re, train_labels, epochs=10)

# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# print('\nTest accuracy:', test_acc)

predictions = model.predict(test_images_re)

cnt_o = 0
cnt_x = 0
for idx,pred in enumerate(predictions):
    mypred = np.argmax(pred)
    mygool = test_labels[idx]
    if mypred == mygool:
        cnt_o += 1
    else:
        cnt_x += 1
        cv2.imwrite("images_miss/"+str(idx)+"_"+str(mypred)+"_"+str(mygool)+".png", test_images[idx])
    print("mypred : ", mypred)
    print("mygool : ", mygool)
# for i,label in enumerate(train_labels):
#     print("train : ",i)
#     cv2.imwrite("images_train/"+str(i)+"_"+str(label)+".png", train_images[i])
#
# for i,label in enumerate(test_labels):
#     print("test : ", i)
#     cv2.imwrite("images_test/"+str(i)+"_"+str(label)+".png", test_images[i])
    
    