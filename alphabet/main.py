import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops

def filling_factor(region):
    return region.image.mean()

def recognize(region):
    if filling_factor(region) == 1:
        return "-"
    else:
        match(region.euler_number):
            case -1: # B or 8
                if 1 in region.image.mean(0):
                    return "B"
                return '8'
            case 0: # A 0 P D
                if 1 in region.image.mean(0): # P D
                    mid = region.image.shape[1] // 2
                    if region.image[-1][:mid].mean() == 1:
                        return "D"
                    return "P"
                tmp = region.image.copy()
                tmp[-1, :] = 1
                tmp_labeled = label(tmp)
                tmp_regions = regionprops(tmp_labeled)
                if tmp_regions[0].euler_number == -1:
                    return 'A'
                return '0'
            case 1: # 1 W X * /
                if 1 in region.image.mean(0):
                    return "1"
                tmp = region.image.copy()
                tmp[[0, -1], :] = 1
                tmp_labeled = label(tmp)
                tmp_regions = regionprops(tmp_labeled)
                match(tmp_regions[0].euler_number):
                    case -1:
                        return "X"
                    case -2:
                        return 'W'
                if region.eccentricity > 0.5:
                    return '/'
                return '*'
    return "?"

image = plt.imread('symbols.png')
binary = image.mean(2)
binary[binary>0] = 1

labeled = label(binary)
print('counts =', labeled.max())
regions = regionprops(labeled)

counts={}
for region in regions:
    symbol = recognize(region)
    if symbol not in counts:
        counts[symbol] = 0
    counts[symbol] += 1

print(counts)
print((labeled.max() - counts.get("?", 0)) / labeled.max())