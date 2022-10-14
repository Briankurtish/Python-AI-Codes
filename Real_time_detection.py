import cv2
from random import randrange

# Load some pre trained data on face frontals from opencv (haar casacde algorithm)
trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')


# choose an image to detect faces in
#img = cv2.imread('3Faces.jpg')

# To Capture Video from webcam
webcam = cv2.VideoCapture(0)
key = cv2.waitKey(1)


# Must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect Faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# print(face_coordinates)

# Draw Rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128, 256),
                  randrange(128, 256), randrange(128, 256)), 2)

cv2.imshow('Cipher Tech Face Detector', img)

# Waits until a key is pressed
cv2.waitKey()


print("Code Completed")
