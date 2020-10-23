import cv2
import os
os.system('cls')
from image_read import take_img


object_type = int(input('Enter the type of object: '))
take_img()
img = cv2.imread('image.jpg')
cv2.imshow('image.jpg', img)
key = cv2.waitKey(1000)

