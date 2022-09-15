# Warp Prespective

import cv2 
import numpy as np

img = cv2.imread("Resources\card.png")
print(img.shape)


width,height = 250,350
pts1 = np.float32([[520,100],[670,130],[480,310],[630,350]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("Card", img)
cv2.imshow("Card", imgOutput)
cv2.waitKey(0)