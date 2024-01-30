from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=False,
	help="path to input image")
args = vars(ap.parse_args())


# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])




# load the input image, resize it, and convert it to grayscale
# image = cv2.imread(args["image"])

# image = imutils.resize(image, width=500)

cap = cv2.VideoCapture(0)

# Read logo and resize 
# logo = cv2.imread('elonmusk.png') 
logo = cv2.imread('elonmusk.jpg') 

size = 100

while True:

	# Region of Image (ROI), where we want to insert logo 



	# Capture frame-by-frame
	ret, frame = cap.read()
	# if frame is read correctly ret is True
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		break
	# Our operations on the frame come here
	frame = imutils.resize(frame, width=500)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Display the resulting frame
	rects = detector(gray, 1)
	# loop over the face detections
	for (i, rect) in enumerate(rects):
		# determine the facial landmarks for the face region, then
		# convert the facial landmark (x, y)-coordinates to a NumPy
		# array
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)
		for i, (x, y) in enumerate(shape):
			# cv2.circle(image, (x, y), 5, (0, 255, 0), -1)  # Draw a circle at the point
			cv2.putText(frame, str(i+1), (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)  # Add text
			# convert dlib's rectangle to a OpenCV-style bounding box
			# [i.e., (x, y, w, h)], then draw the face bounding box
		(x, y, w, h) = face_utils.rect_to_bb(rect)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		# show the face number
		cv2.putText(frame, "Face #{}".format(i + 1), (x - 10, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		# loop over the (x, y)-coordinates for the facial landmarks
		# and draw them on the image
		for (x, y) in shape:
			cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
		# show the output image with the face detections + facial landmarks
		
		logo = cv2.resize(logo, (w, h)) 

		# Create a mask of logo 
		img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY) 
		ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY) 
			#add face of elon in 		
		# roi = frame[-h-20:-20, -w-20:-20] 
		# roi = frame[-h-50:-50, -w-50:-50] 
		
		roi = frame[y-100:y+h-100, x-80:x+w-80]



		# roi = frame[y:y+h, x:x+w] 

		# Set an index of where the mask is 

		try:
			roi[np.where(mask)] = 0
			roi += logo 
		except IndexError:
			pass


	cv2.imshow('frame', frame)
	if cv2.waitKey(1) == ord('q'):
		break

# detect faces in the grayscale image




cap.release()
cv2.destroyAllWindows()

