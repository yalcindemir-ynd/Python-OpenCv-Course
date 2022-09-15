import cv2 
import numpy as np 
import utlis 

webcam = False
path="Resources\paper.jpg"

cap = cv2.VideoCapture(0)
cap.set(10, 160)
cap.set(3, 1280)
cap.set(4, 720)
scale = 10
# wP = 330 * scale
# hP = 250 * scale

wP = 30
hP = 20

while True:
    if webcam:
        success,img=cap.read()
    else:
        img=cv2.imread(path)
        
    imgContours, const = utlis.getContours(img,draw=True,minArea=50000,filter=4)
   
    if len(const) != 0:
        biggest = const[0][2]
        imgWarp = utlis.warpImg(img,biggest,wP,hP)
        imgContours2, const2 = utlis.getContours(imgWarp,draw=True,minArea=2000,filter=4,cThr=[40,40])

        if len(const2) != 0:
            for obj in const2:
                cv2.polylines(imgContours2, [obj[2]], True, (0,255,0), 5)
                
                nPoints = utlis.reOrder(obj[2])
            
                nW = round((utlis.findDis(nPoints[0][0]//scale,nPoints[1][0]//scale)//10),1)
                nH = round((utlis.findDis(nPoints[0][0]//scale,nPoints[2][0]//scale)//10),1)

                cv2.arrowedLine(imgContours2, (nPoints[0][0][0],nPoints[0][0][1]), (nPoints[1][0][0],nPoints[1][0][1]), (255,0,255), 2, 8, 0, 0.1)
                cv2.arrowedLine(imgContours2, (nPoints[0][0][0],nPoints[0][0][1]), (nPoints[2][0][0],nPoints[2][0][1]), (255,0,255), 2, 8, 0, 0.1)

                x, y, w, h = obj[3]

                cv2.putText(imgContours2, '{}cm'.format(nW), (x+30,y-10), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,255), 2)
                cv2.putText(imgContours2, '{}cm'.format(nH), (x-70,y+h//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2)

        cv2.imshow("A4", imgContours2)

    img=cv2.resize(img, (0,0),None,0.5,0.5)
    cv2.imshow("Original", img) 

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()