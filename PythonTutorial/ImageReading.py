import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('garden.jpg',1)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()
#k = cv2.waitKey(0)& 0xFF
#if k == 27:         # wait for ESC key to exit
#    cv2.destroyAllWindows()
#elif k == ord('s'): # wait for 's' key to save and exit
#    cv2.imwrite('messigray.png',img)
#    cv2.destroyAllWindows()
