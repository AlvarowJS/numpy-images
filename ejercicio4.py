import numpy as np
import imageio.v2 as imageio


# Slicing
np_array =imageio.imread('playa.bmp')
originRed = np_array[:,:,:1]
originGreen = np_array[:,:,1:2]
originBlue = np_array[:,:,2:3]

modRed = 0.298 * originRed + 0.578 * originGreen + 0.132 * originBlue
modGreen = 0.254 * originRed + 0.495 * originGreen + 0.111 * originBlue
modBlue = 0.177 * originRed + 0.343 * originGreen + 0.74 * originBlue
# print(nuevoArray)
# print(nuevoArray2)
# print(nuevoArray3)
x = np.concatenate((modRed,modGreen,modBlue), axis=2)
imageio.imwrite('playa-blackandwhite.bmp', x)