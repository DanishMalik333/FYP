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
#print (img.shape)import cv2
import os
import time
os.system('cls')
from image_read import take_img
#from hardware import ser_com

#object_type = int(input('Enter the type of object: '))
take_img()
img = cv2.imread('image.jpg')
img = img[145:315, 415:685]
#img = cv2.rectangle(img, (160,140), (280,180), 255, 2)
cv2.imshow('img', img)
key = cv2.waitKey(10000)
print(img.shape)


#time.sleep(0.5)
#ser_com('90+90+90+0')
#time.sleep(0.5)
#ser_com('180+90+90+0')

