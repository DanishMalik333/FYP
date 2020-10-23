from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2

def take_img():
    kinectC = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)
    #i = 1
    while 1:
        # --- Getting frames and drawing
        #if kinectD.has_new_depth_frame():
        if kinectC.has_new_color_frame():
            frameC = kinectC.get_last_color_frame()
            frameC = np.reshape(frameC, (1080, 1920, 4))
            outputC = cv2.resize(frameC, (0, 0), fx=0.5, fy=0.5)
            #cv2.imshow('KINECT Video StreamC', outputC)
            
            #if i == 1:
            cv2.imwrite('image.jpg',outputC)
            break
            #i = i+1
            