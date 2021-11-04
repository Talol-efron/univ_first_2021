import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')

def plot_img(img):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap="gray")
    plt.show()
