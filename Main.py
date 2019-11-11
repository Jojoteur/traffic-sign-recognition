import cv2
import Functions
import time
from PIL.Image import *
import cv2
import os



"""
cap = cv2.VideoCapture("assets/video1.avi")
#cap = cv2.VideoCapture(0)

while True:
    
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, 1)
    cv2.imshow("", hsv_frame)
    #cv2.imwrite('assets/hsv_frame.png', hsv_frame)
    #hsv_frame = cv2.imread('assets/hsv_frame.png', -1)
    Functions.algorithm(hsv_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
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
#Functions.algorithm(Itraffic12)
Functions.algorithm(Itraffic13)


## END ##
cv2.waitKey(0)
cv2.destroyAllWindows()

exit(0)
