import cv2
from keras.models import load_model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
#importing trtained model
model = load_model("finalmodel.h5")
# Capturing from vids.
cap = cv2.VideoCapture (0)
# To use a input video file we can use cap = cv2.VideoCapture('filename.mp4')
while True:
# Read the frame
#_, img = cap.read()
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
# Convert to grayscale as it works on a grayscale model
    gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
# Detecting the faces (multiple)
    faces = face_cascade.detectMultiscale(gray, 1.1, 4)
# Dimensions of the rectangle around each face
    i = 0
    for face in faces:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2) is the dimension of the rectangle
# Increment the iterartor each time to calculate number of faces
            i = i+1
# Adding face number to the box detecting faces
            cv2.putText (frame, 'face num'+str(i), (x-10, y-10),
                         cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('frame', frame)

            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
vid.release()
        # Destroy all the windows
cv2.destroyAllWindows()