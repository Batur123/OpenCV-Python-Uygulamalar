import cv2
import numpy as np 
from matplotlib import pyplot as plt

image = cv2.imread('./images/Day_030.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
aa = np.shape(gray_image)
print (aa)

ret,thresh = cv2.threshold(image,0,230, cv2.THRESH_BINARY)
height, width = image.shape
print ("Yukseklik ve Genislik: ",height, width)
size = image.size
print ("Toplam Pixel Sayisi", size )



plt.show()


