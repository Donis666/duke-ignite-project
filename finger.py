# game => https://chromedino.com

import cv2
# from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController
from cvzone.HandTrackingModule import HandDetector

mouse = MouseController()
cap = cv2.VideoCapture(0)

def showVideo(): 
    while cap.isOpened():

        ret, frame = cap.read()
        height, width, layers = frame.shape

        frame = cv2.resize(frame, ( width//2, height//2))

        cv2.imshow('Frame', frame)

        k = cv2.waitKey(1)

        if k == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

# showVideo()

def showVideoWHands(): 
    from cvzone.HandTrackingModule import HandDetector

    detector = HandDetector(detectionCon= .8, maxHands = 1)

    while cap.isOpened():

        ret, frame = cap.read()
        height, width, layers = frame.shape

        frame = cv2.resize(frame, ( width//2, height//2))

        hands, image = detector.findHands(frame)

        cv2.imshow('Frame', image)

        k = cv2.waitKey(1)

        if k == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()


# showVideoWHands()

def showVideoWFingers(): 

    detector = HandDetector(detectionCon= .8, maxHands = 1)

    index = 0
    length = 10
    hairs = []


    while cap.isOpened():

        ret, frame = cap.read()
        height, width, layers = frame.shape

        frame = cv2.resize(frame, ( width//2, height//2))

        hands, image = detector.findHands(frame)

        if hands:
            lmList = hands[0]

            fingerUp = detector.fingersUp(lmList)

            print(fingerUp)
            
            if (1 in fingerUp):
                # keep changing and make it random
                
                # while True:
                    # hair = hairs[index]
                cv2.putText(frame, 'Keep Changing Hairstyle', (20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                    # index += 1
                    # if index >= length:
                    #     index = 0
                    
                    # USE THE hair
                
            else:
                # no fingers up means stop. 
                # hair = hairs[index]
                cv2.putText(frame, 'Stop', (20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)


        cv2.imshow('Frame', image)

        k = cv2.waitKey(1)

        if k == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

showVideoWFingers()
