# app.py
from flask import Flask, render_template, request, Response
from cvzone.HandTrackingModule import HandDetector
import cv2
import base64

app = Flask(__name__)

camera = cv2.VideoCapture(0)
detector = HandDetector(detectionCon= .8, maxHands = 1)

def process_frame(frame):
    # Your frame processing logic here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # edges = cv2.Canny(gray, 100, 200)
    
    
    height, width, layers = frame.shape

    frame = cv2.resize(frame, ( width//2, height//2))

    hands, image = detector.findHands(frame)
    if hands:
        lmList = hands[0]

        fingerUp = detector.fingersUp(lmList)
        
        if fingerUp[1] == 1:

            cv2.putText(frame, 'Keep Changing Hairstyle', (20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        else:

            cv2.putText(frame, 'Stop', (20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
    
    return image


def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        processed_frame = process_frame(frame)
        _, buffer = cv2.imencode('.jpg', processed_frame)
        result = base64.b64encode(buffer).decode('utf-8')
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    
    camera.release()
    cv2.destroyAllWindows()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
