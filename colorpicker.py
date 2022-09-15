import cv2
import numpy as np


frameWidth = 1080
frameHeight = 720
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640,240)
cv2.createTrackbar("Hue Min", "HSV", 0, 179, empty)
cv2.createTrackbar("Hue Max", "HSV", 179, 179, empty)
cv2.createTrackbar("Sat Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Sat Max", "HSV", 255, 255, empty)
cv2.createTrackbar("Val Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Val Max", "HSV", 255, 255, empty)

while True:
    _, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "HSV")
    h_max = cv2.getTrackbarPos("Hue Max", "HSV")
    s_min = cv2.getTrackbarPos("Sat Min", "HSV")
    s_max = cv2.getTrackbarPos("Sat Max", "HSV")
    v_min = cv2.getTrackbarPos("Val Min", "HSV")
    v_max = cv2.getTrackbarPos("Val Max", "HSV")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask = mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    #hStack = np.hstack([img,mask,result])

    # cv2.imshow("Orijinal", img)
    # cv2.imshow("Orijinal", imgHsv)
    # cv2.imshow("Orijinal", mask)
    cv2.imshow("Orijinal", result)
    #cv2.imshow("HorizontalStacking",hStack)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()