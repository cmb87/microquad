import socketio
import cv2
import base64
import time
import logging

# standard Python
sio = socketio.Client()

def decode(frame):
    # Send encoded frame back to browser
    retval, buf = cv2.imencode('.png', frame)
    jpg_as_text = base64.b64encode(buf).decode('utf-8')
    return f"data:image/jpeg;base64,{jpg_as_text}"


@sio.event
def connect():
    logging.info('Successfully connected to server.')

@sio.event
def connect_error():
    logging.info('Failed to connect to server.')

@sio.event
def disconnect():
    logging.info('Disconnected from server.')


def main():
    while True:
        try:
            sio.connect(f"ws://localhost:5000", namespaces=["/ros2"])
            logging.info("Connected!")
            break
        except:
            logging.warning(f"Could not connect to server ws://localhost:5000")
            time.sleep(4)

 
    cap = cv2.VideoCapture(0)


    while True:
       ret, frame = cap.read()
    
       if not ret:
           break

       #frame = cv2.resize(frame, (300, 300))
       frame = cv2.resize(frame, (100, 100))
       frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       sio.emit('videofeed1', {'frame': decode(frame)}, namespace='/ros2')
       print("emitted")
       time.sleep(0.1)

if __name__ == "__main__":
    main()
