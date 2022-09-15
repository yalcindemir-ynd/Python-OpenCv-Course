## SHAPE DETECTION
import cv2
import numpy as np

def empty(a):
    pass

def getContours(img):
    #contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours,hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>1000:
            cv2.drawContours(imgContour, cnt, -1, (255,255,255),2)
            peri = cv2.arcLength(cnt, True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            #print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor==3: 
                objectType="Triangle"
            elif objCor==4:
                aspRatio = w/float(h)
                if aspRatio>0.95 and aspRatio<1.05:
                    objectType="Square"
                else:
                    objectType="Rectangle"
            elif objCor>4:
                aspRatio = w/float(h)
                if aspRatio>0.95 and aspRatio<1.05:
                    objectType="Circle"
                else:
                    objectType="Ellipse"                
            else: 
                objectType="None"

            cv2.rectangle(imgContour, (x,y), (x+w,y+h), (200,100,100), 2)
            cv2.putText(imgContour, objectType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (50,50,50),2)

path = "Resources\shapes.png"
aux_img = cv2.imread(path)
aux_imgContour = aux_img.copy()
aux_imgGray = cv2.cvtColor(aux_imgContour, cv2.COLOR_BGR2GRAY)
aux_imgBlur = cv2.GaussianBlur(aux_imgGray, (5,5), 1)

cap = cv2.VideoCapture(1)
cap.set(3, 1920)
cap.set(4, 1080)
cap.set(10, 150)

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640,240)
cv2.createTrackbar("Gauss-K1", "TrackBars", 10, 50, empty)
cv2.createTrackbar("Gauss-K2", "TrackBars", 10, 50, empty)
cv2.createTrackbar("Canny-T1", "TrackBars", 50, 500, empty)
cv2.createTrackbar("Canny-T2", "TrackBars", 150, 500, empty)

while True:
    _, img = cap.read()
    imgContour = img.copy()

    K1 = cv2.getTrackbarPos("Gauss-K1", "TrackBars")
    K2 = cv2.getTrackbarPos("Gauss-K1", "TrackBars")
    T1 = cv2.getTrackbarPos("Canny-T1", "TrackBars")
    T2 = cv2.getTrackbarPos("Canny-T2", "TrackBars")

    kernel = np.ones((K1,K2),np.uint8)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    imgCanny = cv2.Canny(imgBlur, T1, T2)
    imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
    imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

    getContours(imgEroded)
    cv2.imshow("Erode", imgEroded)

    norm = cv2.matchTemplate(imgEroded, imgCanny, cv2.CV_8UC1)
    print(norm)


    if (cv2.waitKey(1000) & 0xFF == ord("q")):
        cv2.destroyAllWindows()
        break