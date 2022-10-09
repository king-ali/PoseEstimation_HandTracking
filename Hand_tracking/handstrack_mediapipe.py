import cv2
import mediapipe

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

#Detection of hands

mpHands = mediapipe.solutions.hands
hands = mpHands.Hands()

#Draw landmarks
mpDraw = mediapipe.solutions.drawing_utils


while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    cv2.waitKey(1)