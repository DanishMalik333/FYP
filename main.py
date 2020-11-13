import cv2
import os
import time
os.system('cls')
from image_read import take_img
from hardware import ser_com

#object_type = int(input('Enter the type of object: '))
take_img()
img = cv2.imread('image.jpg')
#img = cv2.rectangle(img, (160,140), (280,180), 255, 2)
cv2.imshow('img', img)
key = cv2.waitKey(10000)
print(img.shape)


x = 220
y = 180
x_p = x - 180
y_p = y - 165
x_n = x_p*(32.7/220)
y_n = y_p*(32.7/220)
print(x_p, y_p, x_n, y_n)
#time.sleep(0.5)
#ser_com('90+90+90+0')
#time.sleep(0.5)
#ser_com('180+90+90+0')



