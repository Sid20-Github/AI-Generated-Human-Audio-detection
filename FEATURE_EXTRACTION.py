import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
from PIL import Image
import pathlib
import csv

# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

#Keras
import keras

import warnings
warnings.filterwarnings('ignore')


#####################
cmap = plt.get_cmap('inferno')

header = 'filename chroma_stft spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
for i in range(1, 21):
    header += f' mfcc{i}'
header += ' label'
header = header.split()
print(header)


i = 0
file = open('Features.csv', 'w', newline='')
with file:
   writer = csv.writer(file)
   writer.writerow(header)


types = 'AI_generated Human_Voice'.split()



for g in types:
    for filename in os.listdir(f'./audio_files/{g}'):
        songname = f'./audio_files/{g}/{filename}'
        y, sr = librosa.load(songname, mono=True, duration=30)

##        print("=========")
##        print(sr)
##        print("=========")
        i = i +1
        print(i)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'    
        for e in mfcc:
            to_append += f' {np.mean(e)}'
        to_append += f' {g}'
        file = open('Features.csv', 'a', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(to_append.split())

