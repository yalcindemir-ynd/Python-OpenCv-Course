# Histogram
 
import numpy as np
import cv2 as cv

frameWidth = 1080
frameHeight = 720
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

hsv_map = np.zeros((180, 256, 3), np.uint8)
h, s = np.indices(hsv_map.shape[:2])
hsv_map[:,:,0] = h
hsv_map[:,:,1] = s
hsv_map[:,:,2] = 255
hsv_map = cv.cvtColor(hsv_map, cv.COLOR_HSV2BGR)
cv.imshow('hsv_map', hsv_map)

cv.namedWindow('hist', 0)
hist_scale = 10

def set_scale(val):
    global hist_scale
    hist_scale = val
    
cv.createTrackbar('scale', 'hist', hist_scale, 32, set_scale)

while True:
    flag, frame = cap.read()
    cv.imshow('camera', frame)

    small = cv.pyrDown(frame)

    hsv = cv.cvtColor(small, cv.COLOR_BGR2HSV)
    dark = hsv[...,2] < 32
    hsv[dark] = 0
    h = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

    h = np.clip(h*0.005*hist_scale, 0, 1)
    vis = hsv_map*h[:,:,np.newaxis] / 255.0
    cv.imshow('hist', vis)

    if cv.waitKey(1) & 0xFF==ord("q"):
        break

cv.destroyAllWindows()
