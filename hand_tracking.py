import cv2
import mediapipe as mp
import time
import hand_tracking_module as htm
  
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10,30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 255), 1)

    cv2.imshow('image', img)
    cv2.waitKey(1)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break