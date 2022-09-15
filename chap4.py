## Shapes and Texts

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
#img[200:300,100:300]= 255,0,0

cv2.line(img,(0,0),(200,300),(0,255,0),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),3)

cv2.rectangle(img, (100,10), (300,350), (0,0,255), cv2.FILLED)
cv2.rectangle(img, (200,20), (370,370), (0,0,255), 2)

cv2.circle(img, (400,400), 100, (120,120,120), 3)

cv2.putText(img, "YND", (50,400), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (100,150,200),1)

cv2.imshow("Image", img)

cv2.waitKey(0)