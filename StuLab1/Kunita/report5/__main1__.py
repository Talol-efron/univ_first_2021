from matplotlib.image import imread, imsave
from matplotlib.pyplot import plot
import numpy as np
from . import module_img as m_img

img_x = imread(fname="./report5_1/data_input/img_x.jpg",
               format="jpg")[:, :, 0].astype(np.float64)
img_y = imread(fname="./report5_1/data_input/img_y.jpg",
               format="jpg")[:, :, 0].astype(np.float64)

img = np.add(img_x, img_y)
img_inv = np.subtract(255, img)

m_img.plot_img(img_inv)
