import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1080)
cap.set(4, 720)
cap.set(10, 150)

def empty():
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640,240)
cv2.createTrackbar("4.Kernel-K1", "TrackBars", 4, 20, empty)
cv2.createTrackbar("4.Kernel-K2", "TrackBars", 4, 20, empty)
cv2.createTrackbar("3.Canny-T1", "TrackBars", 150, 200, empty)
cv2.createTrackbar("3.Canny-T2", "TrackBars", 100, 200, empty)

while True:
    _, img = cap.read()
    imgCopy = img.copy()

    K1 = cv2.getTrackbarPos("4.Kernel-K1", "TrackBars")
    K2 = cv2.getTrackbarPos("4.Kernel-K2", "TrackBars")
    T1 = cv2.getTrackbarPos("3.Canny-T1", "TrackBars")
    T2 = cv2.getTrackbarPos("3.Canny-T2", "TrackBars")

    kernel = np.ones((K1,K2),np.uint8)

    imgGray = cv2.cvtColor(imgCopy, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1.2)
    imgCanny = cv2.Canny(imgBlur, T1, T2)
    imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
    imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
    
    imgGray = cv2.resize(imgGray, (780,410))
    imgBlur = cv2.resize(imgBlur, (780,410))
    imgCanny = cv2.resize(imgCanny, (780,410))
    imgDialation = cv2.resize(imgDialation, (780,410))
    imgEroded = cv2.resize(imgEroded, (780,410))
    
    imgHor1 = np.hstack((imgGray,imgCanny))
    imgHor2 = np.hstack((imgDialation,imgEroded))
    imgVer = np.vstack((imgHor1,imgHor2))
    cv2.imshow("Orjinal", imgVer)

    if (cv2.waitKey(200) & 0xFF == ord("q")):
        cv2.destroyAllWindows()
        break