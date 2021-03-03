import cv2
import socketio




def receive:
# Open the device at the ID 0 

cap = cv2.VideoCapture(2)

#Check whether user selected camera is opened successfully.

if not (cap.isOpened()):
    print("Could not open video device")

#cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

while(True): 

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('preview',frame)
    #Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
