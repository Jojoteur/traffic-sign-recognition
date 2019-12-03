"""
This file contain the programm launched by the Raspberry Pi

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### Imports ######
import time
import cv2
import tkinter as tkinter
from PIL import Image, ImageTk
from imutils.video import VideoStream
from threading import Thread, Event
from queue import Queue

import PreProcessing
import Recognition

##### Program ######
def application(self):
    # Initialization
    vs = VideoStream(usePiCamera=True, resolution=(1920, 1080)).start()

    # Give time to make the focus
    time.sleep(2.0)

    while(1):
        # Reading the flux
        frame = vs.read()
        imgs = PreProcessing.pre_processing(frame)
        if imgs is not None:
            for image in imgs:
                number = Recognition.detect_number(image)
                event = Event()
                self.put((number, event))
        print("END")
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    vs.stop()


### PROGRAM ###
q = Queue()
t1 = Thread(target = application, args =(q, ))
t1.start()

window = tkinter.Tk()
canvas = tkinter.Canvas(window)

img = ImageTk.PhotoImage(file="assets/blank.jpg")
sign = tkinter.Label(canvas, image=img)
text = tkinter.Label(window, text="")

while 1:
    number, event = q.get()
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
        canvas.pack()
        text["text"]=number
        text.pack()
        window.update()