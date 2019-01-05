"""
Smile recognition based on the face_recognition model we just implemented.
"""

# Importing the openCV library
import cv2

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')  # for smile recognition

"""
A function that takes the image in black and white (gray) and the original image (frame) as input, 
and that will return the same image with the detector rectangles.
"""
def detect(gray, frame):
    # Apply the detectMultiScale method from the face cascade to locate one or several faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Paint a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Get the region of interest in the black and white image
        roi_gray = gray[y:y+h, x:x+w]
        # Get the region of interest in the colored image
        roi_color = frame[y:y+h, x:x+w]
        # Apply the detectMultiScale method to locate one or several eyes in the image
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        
        for (ex, ey, ew, eh) in eyes:
            # Paint a rectangle around the eyes, but inside the referential of the face
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
            
    # Return the image with the detector rectangles
    return frame


# Doing Face Recognition with the webcam
video_capture = cv2.VideoCapture(0)

while True:  # Repeat infinitely
    # Get the last frame
    _, frame = video_capture.read()
    # Do some colour transformations
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Get the output of our detect function
    canvas = detect(gray, frame)
    # Display the outputs
    cv2.imshow('Video', canvas)
    # Type on the keyboard to finish:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# We turn the webcam off.
video_capture.release()

# We destroy all the windows inside which the images were displayed.
cv2.destroyAllWindows()