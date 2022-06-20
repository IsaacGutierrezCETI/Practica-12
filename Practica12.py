#Isaac Alejandro Gutiérrez Huerta 19110198 7E1
#Sistemas de Visión Artificial

import os
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
from skimage import io

Matriz = np.array([[1,1,1,1], [1,1,1,1], [0,0,0,0], [0,0,0,0]])
kernel = np.array([[1,1], [-1,-1]])
temp = signal.convolve2d(Matriz , kernel, mode='same')
print(temp)

def show_convolve2d(imagen, kernel):
 
    plt.ion()
    
    imagen_list = []
    for d in range(3):
        temp = signal.convolve2d(imagen[:,:,d] , kernel,  boundary='symm',mode='same')
        imagen_list.append(temp)

    imagen_filt = np.stack(imagen_list, axis=2)
    imagen_filt[imagen_filt > 255] = 255
    imagen_filt[imagen_filt < 0] = 0
    imagen_filt = imagen_filt.astype("uint8")

    plt.subplot(1,2,1)
    io.imshow(imagen)
    plt.axis('off')

    plt.subplot(1,2,2)
    io.imshow(imagen_filt)
    plt.axis('off')

    io.show()

filename = os.path.join('Aguila2.png')
imagen = io.imread(filename)

tam=5
k=np.ones((tam, tam))/(tam**2)
show_convolve2d(imagen,k)

k=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
show_convolve2d(imagen ,k)
