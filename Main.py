import cv2
import Functions
import time
import cv2
import os


"""
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("assets/vid1.mov")
#cap = cv2.VideoCapture("assets/test.mp4")
#cap.set(cv2.CAP_PROP_POS_FRAMES, 380)
while(cap.isOpened()):
    ret, frame = cap.read()
    Functions.algorithm(frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""


"""
#### Test with some images ####
Itraffic1 = cv2.imread("assets/Traffic1.jpg", -1)
Itraffic2 = cv2.imread("assets/Traffic2.jpg", -1)
Itraffic3 = cv2.imread("assets/Traffic3.jpg", -1)
Itraffic4 = cv2.imread("assets/Traffic4.jpg", -1)
Itraffic5 = cv2.imread("assets/Traffic5.jpg", -1)
Itraffic6 = cv2.imread("assets/Traffic6.jpg", -1)
Itraffic7 = cv2.imread("assets/Traffic7.jpg", -1)
Itraffic8 = cv2.imread("assets/Traffic8.jpg", -1)
Itraffic9 = cv2.imread("assets/Traffic9.jpg", -1)
Itraffic10 = cv2.imread("assets/Traffic10.jpg", -1)
Itraffic11 = cv2.imread("assets/Traffic11.jpg", -1)
Itraffic12 = cv2.imread("assets/Traffic12.jpg", -1)
Itraffic13 = cv2.imread("assets/Traffic13.jpg", -1)

ref30 = cv2.imread("assets/ref30.jpg", -1)


Functions.algorithm(Itraffic1)
Functions.algorithm(Itraffic2)
Functions.algorithm(Itraffic3)
Functions.algorithm(Itraffic4)
Functions.algorithm(Itraffic5)
Functions.algorithm(Itraffic6)
Functions.algorithm(Itraffic7)
Functions.algorithm(Itraffic8)
Functions.algorithm(Itraffic9)
Functions.algorithm(Itraffic10)
Functions.algorithm(Itraffic11)
Functions.algorithm(Itraffic13)
Functions.algorithm(Itraffic12)

## END ##
cv2.waitKey(0)
cv2.destroyAllWindows()

exit(0)



"""

##### FOR THE RASPBERRY #####
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

# Camera initialization
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))


# Capturing frames
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array

    Functions.algorithm(image)

    # Wait for key
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)


cv2.destroyAllWindows()