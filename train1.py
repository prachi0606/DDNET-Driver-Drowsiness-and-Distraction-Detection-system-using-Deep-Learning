from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.pooling import AveragePooling2D
from keras.applications import ResNet50, VGG16
from keras.layers.normalization import BatchNormalization
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Dropout
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras.layers import Input
from keras.models import Model
from keras.utils import to_categorical
from keras.optimizers import SGD,Adam,RMSprop
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imutils import paths
from numpy import load
import random
import numpy as np
import argparse
import pickle
import cv2
import os
import h5py
from keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
print("Hello1")
data = load(r'D:\DDNet\100x100data.npy')
labels = load(r'D:\DDNet\100x100labels.npy')

print("Hello2")
data = np.array(data, dtype="float")
labels = np.array(labels)

print(data.shape)
print(labels.shape)

                          
(trainX, testX, trainY, testY) = train_test_split(data,\
 labels, test_size=0.30, random_state=42)


#lb = LabelBinarizer()
#labels = lb.fit_transform(labels)



#trainAug = ImageDataGenerator(zoom_range=0.15,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.15,horizontal_flip=True,fill_mode="nearest")
#aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1, height_shift_range=0.1, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode="nearest")
#valAug = ImageDataGenerator()
#mean = np.array([123.68, 116.779, 103.939], dtype="float32")
#trainAug.mean = mean
#valAug.mean = mean
INIT_LR = 0.00010
EPOCHS =50
BS = 32

img_rows=trainX[0].shape[0]
img_cols=testX[0].shape[1]
print(trainX[0].shape)
print(testX[0].shape)


model = Sequential()
#model = BatchNormalization()(model)
#model.add(Flatten())

model.add(Conv2D(16, (3, 3), padding="same",input_shape=(100,100, 3), activation="relu"))
model.add(Conv2D(16, (3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), padding="same", activation="relu"))
model.add(Conv2D(32, (3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
print("Hello3")
model.add(Conv2D(128, (3, 3), padding="same", activation="relu"))
model.add(Conv2D(128, (3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(512, (3, 3), padding="same", activation="relu"))
model.add(Conv2D(512, (3, 3), padding="same", activation="relu"))
model.add(Conv2D(512, (3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(512, (3, 3), padding="same", activation="relu"))
model.add(Conv2D(512, (3, 3), padding="same", activation="relu"))
model.add(Conv2D(512, (3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(1024, (3, 3), padding="same", activation="relu"))
model.add(Conv2D(1024, (3, 3), padding="same", activation="relu"))
model.add(Conv2D(1024, (3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

print("Hello4")
model.add(Flatten())
#model = BatchNormalization()(model)

model.add(Dense(1000, activation="relu", kernel_regularizer='l2'))
model.add(Dropout(0.5))
print("Hello5")


model.add(Dense(5, activation="softmax", kernel_regularizer='l2'))
print("Hello6")
print("[INFO] compiling model...")
opt = RMSprop(lr=1e-4,decay=1e-4/ EPOCHS)
print("Hello7")
model.compile(loss="categorical_crossentropy", optimizer=opt,metrics=["accuracy"])
print("[INFO] training head...")
Callbacks=[EarlyStopping(monitor="val_accuracy",mode="max",patience=5, restore_best_weights=True, verbose=0),
           ReduceLROnPlateau(patience=2),
           ModelCheckpoint(filepath='D:\DDNet\100x100RMSpropTrained_Model50epoch.h5', save_best_only=True)]
print("Hello8")
aug = ImageDataGenerator()
model.fit(aug.flow(trainX, trainY, batch_size=BS),validation_data=(testX, testY),steps_per_epoch=len(trainX)//BS, epochs=EPOCHS)
#model.fit_generator(aug.flow(trainX, trainY, batch_size=BS),validation_data=(testX, testY),steps_per_epoch=len(trainX)//BS, epochs=EPOCHS)
print("Hello9")
#model.fit(trainX, trainY, batch_size=8,validation_data=(testX, testY),epochs=EPOCHS, callbacks= Callbacks)
#model.fit(trainX, trainY, batch_size= 2,validation_data=(testX, testY),epochs=EPOCHS, callbacks= Callbacks)
import h5py
model.save('D:\DDNet\100x100RMSPropTrained_Model50epoch.h5')
print("Hello10")
model.summary()  
