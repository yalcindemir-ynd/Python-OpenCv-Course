from __future__ import print_function
import cv2
import numpy as np
import argparse


parser = argparse.ArgumentParser(description='Code for Feature Matching with FLANN tutorial.')
parser.add_argument('--input1', help='Path to input image 1.', default='Resources/pikachu.jpg')
parser.add_argument('--input2', help='Path to input image 2.', default='Resources/robotoy.png')
args = parser.parse_args()

img1 = cv2.imread(cv2.samples.findFile(args.input1), cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(cv2.samples.findFile(args.input2), cv2.IMREAD_GRAYSCALE)

img1 = cv2.resize(img1, (800,800))
img2 = cv2.resize(img2, (800,800))

if img1 is None or img2 is None:
    print('Could not open or find the images!')
    exit(0)

#-- Step 1: Detect the keypoints using SURF Detector, compute the descriptors

orb = cv2.ORB_create(nfeatures=10000)
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# matcher takes normType, which is set to cv2.NORM_L2 for SIFT and SURF, cv2.NORM_HAMMING for ORB, FAST and BRIEF
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
# draw first 50 matches
match_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:500], None)
cv2.imshow('Matches', match_img)
cv2.waitKey()