from matplotlib.image import imread, imsave
from matplotlib.pyplot import plot
import numpy as np
from . import module_img as m_img

img_x = imread(fname="./report5_2/data_input/img_x.jpg",
               format="jpg")[:, :, 0].astype(np.float64)
img_y = imread(fname="./report5_2/data_input/img_y.jpg",
               format="jpg")[:, :, 0].astype(np.float64)

img_x_inv = np.subtract(255, img_x)

img_y_inv = np.subtract(255, img_y)

img = np.add(img_x_inv, img_y_inv)

m_img.plot_img(img)