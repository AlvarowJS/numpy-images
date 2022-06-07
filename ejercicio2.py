import numpy as np
import imageio.v2 as imageio

np_array = np.array(imageio.imread('playa.bmp'))
print(np_array.shape)
y = np_array.shape[0]
x = np_array.shape[1]

Cx = x/2
Cy = y/2

i, j = np.ogrid[0:y, 0:x]
print(i)
# i= np.ogrid[0:x]
# j = np.ogrid[0:y]

h = (y/2)**2

result = (j - Cx)**2 + (i - Cy)**2 > h
np_array[result,:]=0

#imageio.imwrite('playa-circle.bmp', np_array)
