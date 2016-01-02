import numpy as np
import cv2
from matplotlib import pyplot as plt


img=cv2.imread('roi.jpg')
# accessing RED value
img.item(10,10,2)

# modifying RED value
#img.itemset((10,10,2),100)
#img.item(10,10,2)

print (img.shape) 
#extracting ROI
ball = img[238:278, 276:316]
img[221:261, 30:70] = ball
cv2.imshow('image',img)

b,g,r =cv2.split(img)
print(b.shape)
print(b)
cv2.imshow('B',b)
cv2.imshow('G',g)
cv2.imshow('R',r)

img2=cv2.merge((b,g,r))
cv2.imshow('merge',img2)
