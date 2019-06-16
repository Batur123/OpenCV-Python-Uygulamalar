import cv2
import numpy as np 
from matplotlib import pyplot as plt
import imutils

#Median Filtering

img = cv2.imread('./images/Day_030.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.resize(gray, (960, 540)) 

median = cv2.medianBlur(gray, 5)
compare = np.concatenate((gray, median), axis=1) #side by side comparison

lower_range = np.array([65,60,60])
upper_range = np.array([80,255,2555])

mask = cv2.inRange(img, lower_range, upper_range)
masked = cv2.resize(mask, (960, 540)) 
cv2.imshow('image', img)
cv2.imshow('mask', masked)

while(True):
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break

  
cv2.imshow('gray', compare)
cv2.waitKey(0)
cv2.destroyAllWindows
