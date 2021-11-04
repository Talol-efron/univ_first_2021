from matplotlib.image import imread, imsave
from matplotlib.pyplot import plot
import numpy as np
from . import module_img as m_img

img_x = imread(fname="./pkg_Matrix/data_input/img_x.jpg",format="jpg")[:, :, 0].astype(np.float64)
img_y = imread(fname="./pkg_Matrix/data_input/img_y.jpg",format="jpg")[:, :, 0].astype(np.float64)

img_x_inv = np.subtract(255, img_x)
m_img.plot_img(img_x)
m_img.plot_img(img_x_inv)

img_y_inv = np.subtract(255, img_y)
m_img.plot_img(img_y)
m_img.plot_img(img_y_inv)

"""
img_y = imread(fname="./pkg_Matrix/data_input/img_y.jpg",format="jpg")[:, :, 0]
m_img.plot_img(img_y[: , 160:])
"""