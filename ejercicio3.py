import numpy as np
import imageio.v2 as imageio

roll = np.array(imageio.imread('playa.bmp'))

x = np.flip(roll)

imageio.imwrite('playa-roll.bmp', x)