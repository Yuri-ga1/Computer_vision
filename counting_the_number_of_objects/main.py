import numpy as np
from skimage.measure import label
from scipy.ndimage import binary_erosion

image = np.load('ps.npy.txt')
totalCount = label(image).max()

struct1 = [[1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1]]
struct2 = [[1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,0,0,1,1],
            [1,1,0,0,1,1]]
struct3 = [[1,1,0,0,1,1],
            [1,1,0,0,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1]]
struct4 = [[1,1,1,1],
           [1,1,1,1],
           [0,0,1,1],
           [0,0,1,1],
           [1,1,1,1],
           [1,1,1,1]]
struct5 = [[1,1,1,1],
           [1,1,1,1],
           [1,1,0,0],
           [1,1,0,0],
           [1,1,1,1],
           [1,1,1,1]]

print('Total number of objects:', totalCount)
for struct, n in zip((struct1, struct2, struct3, struct4, struct5), (1,2,3,4,5)):
    if struct == struct2 or struct == struct3:
        print(f"Struct{n} objects count =", label(binary_erosion(image, struct)).max()-label(binary_erosion(image, struct1)).max())
    else:
        print(f"Struct{n} objects count =", label(binary_erosion(image, struct)).max())