import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

#cap = cv2.VideoCapture('protocol://IP:port/1')
cap.set(3, 1920)
cap.set(4, 1080)

def getGaussImage(img):
    #imgGray = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5,5),np.uint8)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (9,9), 1)
    # imgCanny = cv2.Canny(img, 150, 200)
    # imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
    # imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
    return imgBlur

def detectCircle(img,minR,maxR):
    
    all_circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT , 1, 30, param1=50, param2=30, minRadius=minR, maxRadius=maxR)

    #print(all_circles)
    try:
        all_circles_rounded = np.uint16(np.around(all_circles))
        #print(all_circles_rounded)
    except :
        all_circles_rounded = []
        print("Error")

    return all_circles_rounded

def drawCircle(circles,img):
    if len(circles) != 0   :
        for i in circles[0,:]:
            cv2.circle(img, (i[0],i[1]), i[2], (0,255,0), 2 )
            cv2.circle(img, (i[0],i[1]), 2, (0,0,255), 2 )
            information = f"({i[0]},{i[1]}) R={i[2]/10}mm"      
            cv2.putText(img, information, (i[0],i[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 3)
            print("Success")
    return img

while True:
    _, img = cap.read()
    original_image = img.copy()

    gauss_image = getGaussImage(img)

    circles = detectCircle(gauss_image,40,80)

    b= detectCircle(gauss_image,100,120)
    
    original_image = drawCircle(circles, original_image)
    #original_image = drawCircle(b, original_image)

    #cv2.imshow("Gauss", gauss_image)
    #cv2.imshow("Circle", showImage)
    cv2.imshow("Circle Detection", original_image)

    if (cv2.waitKey(1) & 0xFF == ord("q")):
        cv2.destroyAllWindows()
        break




