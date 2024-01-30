# importing the libraries 
import cv2 
import numpy as np 

# Setup camera 
cap = cv2.VideoCapture(0) 

# Read logo and resize 
logo = cv2.imread('elonmusk.png') 
size = 100
logo = cv2.resize(logo, (size, size)) 

# Create a mask of logo 
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY) 
ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY) 


while True: 
	# Capture frame-by-frame 
	ret, frame = cap.read() 
	cv2.line(frame,(0,0), (300,300),(255,0,0),5) #blue
	cv2.line(frame,(0,0), (300,0),(0,255,0),5) #green
	cv2.line(frame,(0,0), (0,300),(0,0,255),5) #red



	# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('WebCam', frame) 
	if cv2.waitKey(1) == ord('q'): 
		break

# When everything done, release the capture 
cap.release() 
cv2.destroyAllWindows() 
