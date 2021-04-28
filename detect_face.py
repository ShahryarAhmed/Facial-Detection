import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 0 is the webcame
cap = cv2.VideoCapture(0)

# for video capture read the images in terms of frames
while True:
	# gets each frame
	_, img = cap.read()

	# Read the input image
	#img = cv2.imread('test.jpeg')


	# CV only works on grayscale images
	# Convert into grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Detect faces
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)


	# Draw rectangle around the faces
	for (x, y, w, h) in faces:
	    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

	# Display the output
	cv2.imshow('img', img)

	# if esc key pressed -> exit the loop
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()