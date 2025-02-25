from imutils import paths
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.constraints import maxnorm
import random
import os
import numpy as np
from numpy import save
import cv2
imagePaths = sorted(list(paths.list_images(r'/home/itm1138/Pictures/frames')))
#print(imagePaths[0])
random.seed(42)
random.shuffle(imagePaths)
data = []
labels = []
for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (100, 100))
    data.append(image)
    label = imagePath.split(os.path.sep)[-2]
    if label == 'Backward':
	    label=[1,0,0,0,0]
    elif label == 'Forward':
	    label=[0,1,0,0,0]
    elif label == 'Sleeping':
            label=[0,0,1,0,0]
    elif label== 'Yawning':
	    label=[0,0,0,1,0]
    else:
	    label=[0,0,0,0,1]
        
    labels.append(label)

data = np.array(data, dtype="float")
labels = np.array(labels, dtype="float")


print(labels.shape)

save("/home/itm1138/Pictures/da.npy",data)
save("/home/itm1138/Pictures/la.npy",labels)

