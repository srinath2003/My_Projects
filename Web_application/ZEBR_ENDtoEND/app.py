from flask import Flask, render_template, Response, request, session, redirect, url_for
from flask_cors import CORS
import cv2
import time
from ultralytics import YOLO

app = Flask(__name__)
CORS(app) 
app.secret_key = 'my_secret_key_1234567890'

model = YOLO('best.pt')
model.to('cuda')

video_feed_active = False
frame_rate = 10

@app.route('/start_feed', methods=['POST'])
def start_feed():
    global video_feed_active
    video_feed_active = True
    return '', 204

@app.route('/stop_feed', methods=['POST'])
def stop_feed():
    global video_feed_active
    video_feed_active = False
    return '', 204

@app.route('/video_feed')
def video_feed():
    if video_feed_active:
        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    return '', 204

def gen_frames():
    print("Starting video capture...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    while video_feed_active:
        success, frame = cap.read()
        if not success:
            print("Error: Failed to capture image.")
            break

        results = model(frame)
        for result in results:
            boxes = result.boxes
            for box in boxes:
                conf = box.conf.cpu().item()
                if conf > 0.85:
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    cls = int(box.cls.cpu().item())
                    label = f'{model.names[cls]}: {conf:.2f}'
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
                    cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            print("Error: Frame encoding failed.")
            break

        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
