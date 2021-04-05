import cv2
import mediapipe as mp
import time
pTime = 0
cTime = 0


##화면설정
wCam, hCam= 1280,720x`
##
cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            ##안에 그리게 해준다.
            #mpDraw.draw_landmarks(원본이미지 이름, handLms = 손을 그려준다., mpHands.HAND_CONNECTIONS = 이걸 이어준다.

    ##프레임률 적기
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
    ##

    cv2.imshow("Image", img)
    cv2.waitKey(1)