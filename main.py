import cv2
import os
import time
os.system('cls')
#from image_read import take_img
from hardware import ser_com

#object_type = int(input('Enter the type of object: '))
#take_img()
#img = cv2.imread('image.jpg')
#cv2.imshow('image.jpg', img)
#key = cv2.waitKey(1000)
#print (img.shape)


time.sleep(0.5)
ser_com('90+90+90+0')
time.sleep(0.5)
ser_com('180+90+90+0')
