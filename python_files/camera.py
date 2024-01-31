import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
#cap.open() might be useful if the camera dont work


#opening and saving the
# cap = cv.VideoCapture('vtest.avi')
# # Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.set(cv.CAP_PROP_FRAME_WIDTH ,320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT ,240)

print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

cap.release()
cv.destroyAllWindows()
# press q to quit
