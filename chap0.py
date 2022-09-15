from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils 
import cv2

kernel = np.ones((2,2),np.uint8)

def CenterPoint():
    return ((pointA[0] + pointB[0]) * 0.5 , (pointA[1] + pointB[1]) * 0.5)

img = cv2.imread("Resources\lara.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

imgCanny = cv2.Canny(imgBlur,50,100)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

imgResult = imgEroded.copy()

sekiller = cv2.findContours(imgResult,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


sekiller = sekiller[0] 
if imutils.is_cv2(): pass 
else: sekiller[1]

(sekiller, _) = contours.sort_contours(sekiller)

if cv2.contourArea(sekil) < 200:
    k=0
    
# cv2.imshow("Canny",imgCanny)
# cv2.imshow("Dialation",imgDialation)
# cv2.imshow("Eroded",imgEroded)
# cv2.waitKey(0)

# cv2.destroyAllWindows()