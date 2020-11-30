"""
This file contain the program used to make the tests while developing

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### IMPORTS #####
import tkinter

import cv2
import pytesseract
from sys import platform as _platform
from PIL import ImageTk
import Processing
import Recognition

"""
#### Test with videos (capture or file) ####
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("assets/vid1.MOV")
#cap = cv2.VideoCapture('http://192.168.0.107:8080/video')
cap.set(cv2.CAP_PROP_POS_FRAMES, 380)

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
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

"""

#### Test with some images ####
Images = []

Itraffic1 = cv2.imread("assets/Traffic1.jpg", cv2.IMREAD_UNCHANGED)
Itraffic2 = cv2.imread("assets/Traffic2.jpg", cv2.IMREAD_UNCHANGED)
Itraffic3 = cv2.imread("assets/Traffic3.jpg", cv2.IMREAD_UNCHANGED)
Itraffic4 = cv2.imread("assets/Traffic4.jpg", cv2.IMREAD_UNCHANGED)
Itraffic5 = cv2.imread("assets/Traffic5.JPG", cv2.IMREAD_UNCHANGED)
Itraffic6 = cv2.imread("assets/Traffic6.jpg", cv2.IMREAD_UNCHANGED)
Itraffic7 = cv2.imread("assets/Traffic7.jpg", cv2.IMREAD_UNCHANGED)
Itraffic8 = cv2.imread("assets/Traffic8.jpg", cv2.IMREAD_UNCHANGED)
Itraffic9 = cv2.imread("assets/Traffic9.jpg", cv2.IMREAD_UNCHANGED)
Itraffic10 = cv2.imread("assets/Traffic10.jpg", cv2.IMREAD_UNCHANGED)
Itraffic11 = cv2.imread("assets/Traffic11.jpg", cv2.IMREAD_UNCHANGED)
Itraffic12 = cv2.imread("assets/Traffic12.jpg", cv2.IMREAD_UNCHANGED)
Itraffic13 = cv2.imread("assets/Traffic13.jpg", cv2.IMREAD_UNCHANGED)


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

windowTraffic = tkinter.Tk()
windowTraffic.title("Traffic image")
canvasTraffic = tkinter.Canvas(windowTraffic)
imgTraffic = ImageTk.PhotoImage(file="assets/blank.jpg")
imgTrafficLabel = tkinter.Label(canvasTraffic, image=imgTraffic)

windowSpeedLimit = tkinter.Tk()
windowSpeedLimit.title("Speed limitation")
canvasSpeedLimit = tkinter.Canvas(windowSpeedLimit)

img = ImageTk.PhotoImage(file="assets/blank.jpg")
sign = tkinter.Label(canvasSpeedLimit, image=img)
text = tkinter.Label(windowSpeedLimit, text="")
for elt in Images:
    imgs = Processing.pre_processing(elt)
    print("processed")
    img = ImageTk.PhotoImage(file="assets/blank.jpg")
    if imgs is not None:
        for image in imgs:
            number = Recognition.detect_number(image)
            if number is not None:
                if "11" in number or "10" in number:
                    print("@@@@ 110 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref110.jpg")
                elif "30" in number:
                    if "130" in number or "13" in number:
                        print("@@@@ 130 @@@@")
                        img = ImageTk.PhotoImage(file="assets/ref130.jpg")
                    else:
                        print("@@@@ 30 @@@@")
                        img = ImageTk.PhotoImage(file="assets/ref30.jpg")
                elif "5" in number:
                    print("@@@@ 50 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref50.jpg")
                elif "7" in number:
                    print("@@@@ 70 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref70.jpg")
                elif "8" in number:
                    print("@@@@ 80 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref80.jpg")
                elif "9" in number:
                    print("@@@@ 90 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref90.jpg")
    sign["image"] = img
    sign.pack()
    canvasSpeedLimit.pack()
    text["text"] = number
    text.pack()
    
    windowSpeedLimit.update()

    imgTrafficLabel["image"] = elt
    imgTrafficLabel.pack()
    canvasTraffic.pack()
    windowTraffic.update()
    
    print("END")
    print("\n")
    cv2.waitKey(0)
    cv2.destroyAllWindows()



exit(0)

