import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder, StandardScaler

data=pd.read_csv("Features_final.csv")

genre_list = data.iloc[:, -1]
encoder = LabelEncoder()
y = encoder.fit_transform(genre_list)


print("Y : ",len(y))

scaler = StandardScaler()

X = np.array(data.iloc[:, :-1], dtype = float)
print("X : ",len(X))

from keras import models
from keras import layers

model = models.Sequential()

model.add(layers.Dense(1024, activation='relu', input_shape=(X.shape[1],)))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(8, activation='relu'))
model.add(layers.Dense(4, activation='relu'))
model.add(layers.Dense(2, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

epochs=25

model.fit(X, y, epochs=epochs)

model.save('NN.h5')
print(' ')
print("Training completed")
