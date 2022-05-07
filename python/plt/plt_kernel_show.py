import matplotlib.pyplot as plt
import numpy as np

def gkern(l=10, sig=1.):
    """\
    creates gaussian kernel with side length `l` and a sigma of `sig`
    """
    ax = np.linspace(-(l - 1) / 2., (l - 1) / 2., l)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sig))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)

def plt_test():
    kernel = gkern(l = 11, sig = 1)
    plt.axis('off')
    plt.imshow(kernel,cmap='binary_r',interpolation='bicubic')# binary_r binary
    plt.savefig('./python/plt/kernel.png',bbox_inches='tight', pad_inches=0)