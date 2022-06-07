import numpy as np
import imageio.v2 as imageio

#numpy array original
np_array = np.array(imageio.imread('playa.bmp'))
#print(np_array)
#print(np_array.shape)

#numpy array convertido a 255
nuevoArreglo = np.full((np_array.shape), 255)
#print(nuevoArreglo)

resultado = nuevoArreglo - np_array

imageio.imwrite('playa-negative.bmp', resultado)