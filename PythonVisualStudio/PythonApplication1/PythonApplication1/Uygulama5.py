import cv2
import numpy as np 
from matplotlib import pyplot as plt

#Median Filtering

img = cv2.imread('./images/Day_030.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.resize(gray, (960, 540)) 

median = cv2.medianBlur(gray, 5)
compare = np.concatenate((gray, median), axis=1) #side by side comparison


cv2.imshow('gray', compare)
cv2.waitKey(0)
cv2.destroyAllWindows
