from flask import Flask, render_template, Response, request
import cv2
import time
from ultralytics import YOLO

app = Flask(__name__)

# Load the model
model = YOLO('best.pt')  # Ensure the correct path
model.to('cuda')  # Move the model to GPU

# Global variable to control the video feed
video_feed_active = False
frame_rate = 10  # Limit to 10 FPS

def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        if not video_feed_active:
            time.sleep(1)  # Sleep for a second if feed is inactive
            continue
        
        success, frame = cap.read()
        if not success:
            break

        # Perform inference
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
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        # Limit the frame rate
        time.sleep(1 / frame_rate)

    cap.release()
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
