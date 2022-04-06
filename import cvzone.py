import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture (0)
cap.set(3, 1280)
cap.set (4, 720)
detector = HandDetector (detectionCon=0.8, maxHands=2)
while True:
    SUccess, img = cap.read ()
    cv2. imshow("Image", img)
    cv2.waitkey(1)