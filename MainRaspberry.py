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
def capture(self, resolution, framerate):
    """
    This function is the function executed by the first thread, it only deal with the capture of images by the picam
    """
    # Camera configuration
    camera = PiCamera()
    camera.resolution = resolution
    camera.framerate = framerate
    rawCapture = PiRGBArray(camera, size=resolution)

    # Give time to make the focus
    time.sleep(2)

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array  # Convert frame to array understood by OpenCv

        self.put(image)

        print("CAPTURED")

        rawCapture.truncate(0)


def processing(self):
    """
    This function is the function executed by the second thrad, it take the images which have been captured to the queue
    and process
    """
    while 1:
        image = q0.get()
        results = Processing.pre_processing(image)                      # Image processing
        if results is not None:
            self.put(results)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        print("PROCESSED")

    cv2.destroyAllWindows()


def recognition(self):
    """
    This function is called by the last thread. It get the images stored in the queue and use the recognition algorithm
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
resolution = (1920, 1080)
framerate = 30

q0 = Queue()
q1 = Queue()
q2 = Queue()

t0 = Thread(target = capture, args =(q0, resolution, framerate))
t0.start()

t1 = Thread(target = processing, args =(q1,))
t1.start()

t2 = Thread(target = recognition, args =(q2,))
t2.start()

gui()