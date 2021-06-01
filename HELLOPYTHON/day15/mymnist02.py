from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
import cv2

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
for i, img in enumerate(test_images):
    cv2.imwrite('test/' + str(i) +'_'+ str(test_labels[i]) +'.png', img)
    if i>100 :
        break
    
cv2.waitKey(0)
cv2.destroyAllWindows()