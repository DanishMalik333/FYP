from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2


kinectC = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)
#i = 1
while 1:
    # --- Getting frames and drawing
    #if kinectD.has_new_depth_frame():
    if kinectC.has_new_color_frame():
        frameC = kinectC.get_last_color_frame()
        frameC = np.reshape(frameC, (1080, 1920, 4))
        outputC = cv2.resize(frameC, (0, 0), fx=0.5, fy=0.5)
        img= outputC[0:180, 380:600]
        img = cv2.rectangle(img, (180,165), (220,180), 255, 2)
        cv2.imshow('KINECT Video StreamC', img)
        #if i == 1:
    key = cv2.waitKey(1)
    if key == 27:
        cv2.imwrite('image.jpg',img)
        break    
        #cv2.imwrite('image.jpg',img)
        #break
cv2.destroyAllWindows()