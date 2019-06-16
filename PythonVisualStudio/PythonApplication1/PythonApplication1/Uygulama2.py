"""
Resim Formatını Değiştirme.
"""

import cv2
import numpy as np


image = cv2.imread('./images/Day_030.png')
cv2.imshow('Orjinal Resim', image)
cv2.waitKey()


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Editlenmis Resim',gray_image)
cv2.waitKey()
cv2.destroyAllWindows()
