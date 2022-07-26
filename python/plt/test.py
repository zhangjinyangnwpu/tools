from sklearn.datasets import load_iris
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF,Matern

kernel = 1.0 * RBF([1.0,1.5,0.5,1]) # just create anisotropic kernel here
#kernel = 1.0 * RBF([1]) # isotropic kernel
print(kernel.diag())