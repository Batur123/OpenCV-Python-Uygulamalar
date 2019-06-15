import cv2
import numpy as np


input = cv2.imread('./images/Day_030.png')

bb = np.shape(input) 

print (bb)
print ('Resim Height:', bb[0])
print('Resim Widht:', bb[1])

cv2.imwrite('Bitki.jpg' , input)


cv2.imshow('Örnek Resim',input)
cv2.waitKey(0)
cv2.destroyAllWindows()



""" 
input = cv2.imread() komutu resmi almak için kullanılır.

bb = np.shape(input) ise alınan resmin büyüklüğünü N-dimension tipinde gösterir. Örneğin 1024x768 büyüklüğünde olduğunu gösterebilir.
print(bb) ise, ölçülen resim büyüklüğünü yazdırmaya işe yarar.
cv2.imshow() Resmi göstermek için kullanılır.
cv2.waitKey() bekleme komutudur. Parantez içi milisaniyeler olarak alınır. 
cv2.destoryAllWindows() aslında bir Exception Handling olarak sayılabilir. Hata oluşmasın diye veya hata oluşurşa diye açılan tüm programları kapatır.

"""