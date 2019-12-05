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


#### THREADS DEFINITIONS ####
def processing(self):
    #cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("assets/vid1.mov")
    #cap = cv2.VideoCapture("assets/test.mp4")
    cap.set(cv2.CAP_PROP_POS_FRAMES, 380)
    while (cap.isOpened()):
        ret, frame = cap.read()
        imgs = []
        if frame is not None:
            imgs = Processing.pre_processing(frame)
            self.put(imgs)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        print("END")
        print("")
        print("")

    cap.release()
    cv2.destroyAllWindows()


def recognition(self):
    while 1:
        imgs = []
        imgs = q1.get()
        if imgs is not None:
            for image in imgs:
                number = Recognition.detect_number(image)
                self.put(number)


def gui():
    list = []

    list_30 = ["30"]
    list.append(list_30)

    list_50 = [
        "50", "S0", "s0", "S0", "s0",
        "5O", "5o",
        "SO", "So",
        "sO", "so", ]
    list.append(list_50)

    list_70 = ["70"]
    list.append(list_70)

    list_90 = ["90"]
    list.append(list_90)

    list_110 = ["110"]
    list.append(list_110)

    list_130 = ["130"]
    list.append(list_130)

    window = tkinter.Tk()
    canvas = tkinter.Canvas(window)

    img = ImageTk.PhotoImage(file="assets/blank.jpg")
    sign = tkinter.Label(canvas, image=img)
    text = tkinter.Label(window, text="")

    while 1:
        number = q2.get()
        img = GUI.GUI(img, number, list)
        sign["image"] = img
        sign.pack()
        canvas.pack()
        text["text"] = number
        text.pack()
        window.update()

#### PROGRAM ####
q1 = Queue()
q2 = Queue()

t1 = Thread(target = processing, args =(q1,))
t1.start()

t2 = Thread(target = recognition, args =(q2,))
t2.start()

gui()

#t1 = Thread(target = application, args =(q, ))







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


def application(self):
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture("assets/vid1.mov")
    #cap = cv2.VideoCapture("assets/test.mp4")
    #cap.set(cv2.CAP_PROP_POS_FRAMES, 380)
    while(cap.isOpened()):
        ret, frame = cap.read()
        imgs=[]
        imgs = Processing.pre_processing(frame)
        if imgs is not None:
            for image in imgs:
                number = Recognition.detect_number(image)
                #print(number)
                event = Event()
                self.put(((number,image),event))

        #print("END")
        #print("\n")
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


### PROGRAM ###
q = Queue()
t1 = Thread(target = application, args =(q, ))
t1.start()

window = tkinter.Tk()
canvas = tkinter.Canvas(window)

img = ImageTk.PhotoImage(file="assets/blank.jpg")
sign = tkinter.Label(canvas, image=img)
processed = tkinter.Label(canvas, image=img)
text = tkinter.Label(window, text="")


while 1:
    (number,image), event = q.get()
    print(q.qsize())
    if image is not None:
        processed["image"]=ImageTk.PhotoImage(image=Image.fromarray(image))
        if number is not None:
            if number=="30":
                img = ImageTk.PhotoImage(file="assets/ref30.jpg")
                sign["image"]=img
            elif number=="50":
                img = ImageTk.PhotoImage(file="assets/ref50.jpg")
                sign["image"]=img
            elif number=="70":
                img = ImageTk.PhotoImage(file="assets/ref70.jpg")
                sign["image"]=img
            elif number=="90":
                img = ImageTk.PhotoImage(file="assets/ref90.jpg")
                sign["image"]=img
            elif number=="110":
                img = ImageTk.PhotoImage(file="assets/ref110.jpg")
                sign["image"]=img
            elif number=="130":
                img = ImageTk.PhotoImage(file="assets/ref130.jpg")
                sign["image"]=img
            sign.pack()
        processed.pack()
        canvas.pack()
        text["text"]=number
        text.pack()
        window.update()
"""




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
    imgs = PreProcessing.pre_processing(elt)
    if imgs is not None:
        for image in imgs:
            txt = Recognition.detect_number(image)
            print(txt)
    print("END")
    print("\n")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


cv2.destroyAllWindows()
"""
exit(0)

