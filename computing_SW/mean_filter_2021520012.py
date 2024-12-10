import matplotlib.pyplot as plt 
import numpy as np


def applied_meanFilter(img, filter_size):
    
    filter_location = (filter_size-1) // 2
    
    padded_image = np.pad(img, ((filter_location, filter_location),(filter_location, filter_location)), 'constant', constant_values=0)

    height, width = np.shape(img)    

    result_image = np.zeros_like(img)

    for y in range(height):
        for x in range(width):
            filter_region = padded_image[y:y+filter_size, x:x+filter_size]
            
            result_image[y, x] = np.sum(filter_region) / (filter_size**2) #result image는 좌표가 다르겠지!
            
    return result_image

img = plt.imread("./cameraman.jpg")
filter_size = int(input("filter size를 입력하세요: "))

blured_image = applied_meanFilter(img, filter_size)

plt.gray()
plt.imshow(blured_image)
plt.show()


