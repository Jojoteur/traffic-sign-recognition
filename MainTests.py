"""
This file contain the programm used to make the tests while developing

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""


import cv2
import tkinter
from PIL import Image,ImageTk
from threading import Thread, Event
from queue import Queue

import Processing
import Recognition
import GUI


#### Test with videos (capture or file) ####

"""
#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("assets/vid1.mov")
cap = cv2.VideoCapture("assets/test.mp4")
#cap.set(cv2.CAP_PROP_POS_FRAMES, 380)
while(cap.isOpened()):
    ret, frame = cap.read()
    imgs=[]
    imgs = Processing.pre_processing(frame)
    if imgs is not None:
        for image in imgs:
            number = Recognition.detect_number(image)
            print(number)

    #print("END")
    #print("\n")
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
"""


#### Test with some images ####
Images = []

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

Images.append(Itraffic1)
Images.append(Itraffic2)
Images.append(Itraffic3)
Images.append(Itraffic4)
Images.append(Itraffic5)
Images.append(Itraffic6)
Images.append(Itraffic7)
Images.append(Itraffic8)
Images.append(Itraffic9)
Images.append(Itraffic10)
Images.append(Itraffic11)
Images.append(Itraffic12)
Images.append(Itraffic13)


for elt in Images:
    imgs = Processing.pre_processing(elt)
    print("processed")
    if imgs is not None:
        for image in imgs:
            txt = Recognition.detect_number(image)
            print(txt)
    print("END")
    print("\n")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


cv2.destroyAllWindows()
exit(0)

