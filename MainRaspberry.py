"""
This file is the one executed by the Raspberry Pi.
It contains the threads definition and the execution.

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

import time
import cv2
import tkinter as tkinter
from PIL import ImageTk
from threading import Thread
from queue import Queue

from picamera.array import PiRGBArray
from picamera import PiCamera

import Processing
import Recognition
import GUI


######## THREADS DEFINITIONS ########
def processing(self):
    """
    This function is the function executed by the first thread, it launch the capture of images by the camera and
    process them by the algorithm established in the file "Processing".
    Each image returned by the processing algorithm is put on a queue.
    """
    # Camera configuration
    camera = PiCamera()
    camera.resolution = (1640, 922)
    camera.framerate = 40
    rawCapture = PiRGBArray(camera, size=(1640, 922))

    # Give time to make the focus
    time.sleep(2)

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array                         # Convert frame to array understood by OpenCv

        images = Processing.pre_processing(image)   # Image processing

        if images is not None:
            self.put(images)

        rawCapture.truncate(0)                      # Clear the stream in preparation for the next frame

        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

        print("END")
        print("")
        print("")

    cv2.destroyAllWindows()


def recognition(self):
    """
    This function is called by the second thread. It get the images stored in the queue and use the recognition algorithm
    established in the file "Recognition".
    Then it put the number in an other queue.
    """
    while 1:
        images = q1.get()
        if images is not None:
            for image in images:
                number = Recognition.detect_number(image)
                self.put(number)


def gui():
    """
    This function is called by the main Thread, it is the GUI.
    Inside the while loop, it take each number and show a referenced traffic sign in function of the number got.
    """
    # Creating the data base of references for numbers
    list = []

    references_30 = ["30"]
    list.append(references_30)

    references_50 = [
        "50", "S0", "s0", "S0", "s0",
        "5O", "5o",
        "SO", "So",
        "sO", "so", ]
    list.append(references_50)

    references_70 = ["70"]
    list.append(references_70)

    references_90 = ["90"]
    list.append(references_90)

    references_110 = ["110"]
    list.append(references_110)

    references_130 = ["130"]
    list.append(references_130)

    # Initializing the GUI
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


######## RUNNING ########
q1 = Queue(2)
q2 = Queue(2)

t1 = Thread(target = processing, args =(q1,))
t1.start()

t2 = Thread(target = recognition, args =(q2,))
t2.start()

gui()


###### OLD #######

"""
##### Imports ######
import time
import cv2
import tkinter as tkinter
from PIL import Image, ImageTk
from threading import Thread, Event
from queue import Queue

from picamera.array import PiRGBArray
from picamera import PiCamera

import PreProcessing
import Recognition

import ThreadsRaspberry


##### Program ######
def application(self):
    camera = PiCamera()
    camera.resolution = (1640, 922)
    camera.framerate = 40
    rawCapture = PiRGBArray(camera, size=(1640, 922))

    time.sleep(0.1)

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array

        imgs = PreProcessing.pre_processing(image)
        if imgs is not None:
            for image in imgs:
                number = Recognition.detect_number(image)
                event = Event()
                self.put((number, event))


        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

        print("END")
        print("")
        print("")

    cv2.destroyAllWindows()

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
"""