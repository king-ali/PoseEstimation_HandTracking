import cv2
import mediapipe

cap = cv2.VideoCapture("football.mp4")
mPose = mediapipe.solutions.pose
pose = mPose.Pose()

mpDraw = mediapipe.solutions.drawing_utils


while True:
    success, img = cap.read()
    img = cv2.resize(img, (640,720))
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mPose.POSE_CONNECTIONS)

        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape
            # print(id,lm)
            
            cx,cy = int(lm.x*w), int(lm.y*h)

            cv2.circle(img, (cx,cy), 5, (255,0,0),cv2.FILLED)

    cv2.imshow("Image", img)
    cv2.waitKey(1)