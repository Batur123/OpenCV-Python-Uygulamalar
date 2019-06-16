
import cv2
import numpy as np 
from matplotlib import pyplot as plt
import random

resim = cv2.imread('./images/Day_030.png')

plt.figure(figsize = (15,15))
plt.imshow(resim)

print('Resmin Türü: ' , type(resim))
print()
print('Resim Tam Boyutu: {}'.format(resim.shape))
print('Resim Yüksekliği: {}'.format(resim.shape[0]))
print('Resim Genişliği: {}'.format(resim.shape[1]))
print('Resim Dimensionu: {}'.format(resim.ndim))

print('Resim Boyutu: {}'.format(resim.size))
print('Resimdeki maksimum RGB Değeri: {}'.format(resim.max()))
print('Resimdeki minimum RGB Değeri: {}'.format(resim.min()))

print('Red(Kırmızı) Kanal Sayısı: {}'.format(resim[ 100, 50, 0]))
print('Green(Yeşil) Kanal Sayısı: {}'.format(resim[ 100, 50, 1]))
print('Blue(Mavi) Kanal Sayısı: {}'.format(resim[ 100, 50, 2]))

plt.title('G channel')
plt.ylabel('Height {}'.format(resim.shape[0]))
plt.xlabel('Width {}'.format(resim.shape[1]))

plt.imshow(resim[ : , : , 1]) 
plt.show()

"""R=0, G=1, B=2"""

gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) 
gray = gray(resim)  

plt.figure( figsize = (10,10))
plt.imshow(gray, cmap = plt.get_cmap(name = 'gray'))
plt.show()


"""
low_pixel = resim < 20

# to ensure of it let's check if all values in low_pixel are True or not
if low_pixel.any() == True:
    print(low_pixel.shape)

# set value randomly range from 25 to 225 - these value also randomly choosen
resim[low_pixel] = random.randint(25,225)

# display the image
plt.figure( figsize = (10,10))
plt.imshow(resim)
plt.show()
"""

kernel = np.ones((5,5),np.float32)/25

abc = cv2.filter2D(gray,-1,kernel)
plt.subplot(121),plt.imshow(gray),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(abc),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()