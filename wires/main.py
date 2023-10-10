import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_erosion, binary_opening
from skimage.measure import label

struct = np.ones((3,1))

for i in range(1, 7):
    file = np.load(f'wires{i}.npy.txt')
    plt.subplot(121)
    plt.imshow(file)
    wires_count = label(file).max()
    image = label(binary_erosion(file, struct)) # binary_opening

    plt.subplot(122)
    plt.imshow(image)
    plt.show()

    count =0
    x=0
    for j in range(image.shape[0]):
        if image[j, 0] != 0: # and count != image[j].max():
            x+=1
            print(f'Количество кусков в {x} проводе в файле {i} =',  image[j].max() - count)
            count = image[j].max()
    if x < wires_count:
        print(f'В файле №{i} существует изкромсаный в мясо провод')