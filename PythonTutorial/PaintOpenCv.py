import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
radius = 1
R= 0
G=0
B=0
# mouse callback function
def nothing(x):
    pass

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,radius,R,G,B
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        pass
        #if drawing == True:
        #    if mode == True:
        #        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),3)
        #    else:
        #        cv2.circle(img,(x,y),radius,(0,0,255),3)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(B,G,R),1)
        else:
            cv2.circle(img,(x,y),radius,(B,G,R),1)

img = np.zeros((512,512,3), np.uint8)
img[:]=[255,255,255]
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
#create colour pallet
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('Ra','image',0,100,nothing)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    R = cv2.getTrackbarPos('R','image')
    G = cv2.getTrackbarPos('G','image')
    B = cv2.getTrackbarPos('B','image')
    radius = cv2.getTrackbarPos('Ra','image')
    s = cv2.getTrackbarPos(switch,'image')
   # if s == 0:
   #     img[:] = 0
   # else:
   #    img[:] = img+[b,g,r]
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
