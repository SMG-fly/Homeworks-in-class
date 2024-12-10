import matplotlib.pyplot as plt
import numpy as np

def applied_meanFilter(image, mf_size): #mf_size -> meanfilter_size
    pad_size = int ((mf_size-1)/2)
    
    mean_filter = np.ones((mf_size, mf_size))
    mean_filter = mean_filter / (mean_filter.size) #size값(element값)이랑 제곱값이랑 같지~
    
    blurred_image = np.zeros_like(image)
    image = np.pad(image, ((pad_size, pad_size), (pad_size, pad_size)), 'constant', constant_values=0)
    
    for i in range(blurred_image.shape[0]): #행 #print(blurred_image.shape)->(256, 256)
        for j in range(blurred_image.shape[1]): #열
            blurred_image[i, j] = np.sum(image[i:i+mf_size, j:j+mf_size]*mean_filter) #mean_filter -> 1/(mf_size^2)가 필터 칸에 채워져 있음
            #blurred_image를 새로 만들어서 blurred_image 요소들로 채운 다음 출력
            
    plt.gray()
    plt.imshow(blurred_image)
    plt.show()

image = plt.imread('./cameraman.jpg')
applied_meanFilter(image, 7) #filter size 여기 입력