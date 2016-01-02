import numpy as np
import cv2
from matplotlib import pyplot as plt


#create a black image
img =np.zeros((512,512,3), np.uint8)

#draw a diagonal line with 5 pxl thickness

img =cv2.line(img,(0,0),(441,441),(255,0,0),5)
#input image diagonal corners and thickness  

img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

img = cv2.circle(img,(447,63), 60, (0,0,255), 3)

img = cv2.ellipse(img,(256,256),(100,100),0,0,180,(0,255,0),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.xticks([]),plt.yticks([])
plt.show()
#cv2.imshow('image', img)
