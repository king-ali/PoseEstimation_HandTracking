import cv2
import PoseEstimationModule as pm

cap = cv2.VideoCapture("football.mp4")

detector = pm.poseDetector()

while True:

    success, img = cap.read()
    img = cv2.resize(img, (640, 720))
    img = detector.findPose(img,draw=False)
    lmlist = detector.findPosition(img,draw=False)
    # print(lmlist)

    #draw points on left arm
    detector.findAngle(img,11,13,15)

    #draw points on right arm
    detector.findAngle(img,12,14,16)

    #draw points on left leg
    detector.findAngle(img,23,25,27)

    #draw points on right leg
    detector.findAngle(img,24,26,28)


    cv2.imshow("Image", img)
    cv2.waitKey(1)