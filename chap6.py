#Joining Images 
import cv2
import numpy as np 

img = cv2.imread("Resources\panda.jpg")

imghor = np.hstack((img,img))
imgVer = np.vstack((imghor,imghor))

cv2.imshow("Horizontal-Vertical", imgVer) 
cv2.waitKey(0)