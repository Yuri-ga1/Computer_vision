import numpy as np
from scipy.ndimage import binary_erosion
from skimage.measure import label

plus_mask = np.array([[0,0,1,0,0],
                [0,0,1,0,0],
                [1,1,1,1,1],
                [0,0,1,0,0],
                [0,0,1,0,0]])

cross_mask = np.array([[1,0,0,0,1],
                [0,1,0,1,0],
                [0,0,1,0,0],
                [0,1,0,1,0],
                [1,0,0,0,1]])

file = np.load('stars.npy')
plus_count = label(binary_erosion(file, plus_mask)).max()
cross_count = label(binary_erosion(file, cross_mask)).max()
print(f"pluses: {plus_count}\ncrosses: {cross_count}")