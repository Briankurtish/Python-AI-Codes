import cv2
from random import randrange

# Load some pre trained data on face frontals from opencv (haar casacde algorithm)
trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')


# choose an image to detect faces in
#img = cv2.imread('3Faces.jpg')

# To Capture Video from webcam
webcam = cv2.VideoCapture(0)

# Iterate forever over Frames

while True:

    # Read the current Frame
    successful_frame_read, frame = webcam.read()

    # Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw Rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Cipher Tech Face Detector', frame)

    # Waits until a key is pressed
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key == 81 or key == 113:
        break

# Release the webcam Object
webcam.release()

print("Code Completed")

'''''


cv2.imshow('Cipher Tech Face Detector', img)

# Waits until a key is pressed
cv2.waitKey()


print("Code Completed")
'''
