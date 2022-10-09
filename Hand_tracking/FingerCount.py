import cv2
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

detector = htm.handDetector(detectionCon=0.75)
tipIds = [4,8,12,16,20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    # print(lmlist)

    if len(lmlist)!=0:
        fingers = []

        #Thumb

        if lmlist[tipIds[0]][1] < lmlist[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

    #For fingers
        for id in range(1,5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(fingers)
        totalFingers = fingers.count(1)
        # print(totalFingers)

        cv2.rectangle(img,(20,225),(170,425),(0,255,0),cv2.FILLED)
        cv2.putText(img,str(totalFingers),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)

    cv2.imshow("Image", img)
    cv2.waitKey(1)