"""
This file is the one executed by the Raspberry Pi.
It contains the threads definition and the execution.

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### IMPORTS #####
import time
import cv2
import tkinter as tkinter
from sys import platform as _platform
from PIL import ImageTk
from threading import Thread
from queue import Queue
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
import Processing
import Recognition
import GUI

######## THREADS DEFINITIONS ########
def processing(queue1, queue2, resolution, framerate):
    """
    This function is the function executed by the first thread, it launch the capture of images by the camera and
    process them by the algorithm established in the file "Processing".
    Each image returned by the processing algorithm is put on a queue.
    :param queue1: the fist queue where to put images detected
    :param queue2: the second queue where to put images detected
    :param resolution: the resolution of the camera
    :param framerate: the framerate of the camera
    """
    # Camera configuration
    camera = PiCamera()
    camera.resolution = resolution
    camera.framerate = framerate
    rawCapture = PiRGBArray(camera, size=resolution)

    # Give time to make the focus
    time.sleep(2)
    i = 0

    # Global loop
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array                         # Convert frame to array understood by OpenCv
        images = Processing.pre_processing(image)   # Image processing
        if images is not None:
            if i%2==0:
                queue1.put(images)
            else:
                queue2.put(images)
        rawCapture.truncate(0)                     # Clear the stream in preparation for the next frame
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

        print("END")
        print("")
        print("")

        # Reset the counter to avoid big number problems
        if i<=11:
            i = i+1
        else:
            i=0

    cv2.destroyAllWindows()


def recognition(queue_images, queue_number):
    """
    This function is called by the second thread. It get the images stored in the queue and use the recognition algorithm
    established in the file "Recognition".
    Then it put the number in an other queue.
    :param queue_images: the queue containing the images detected
    :param queue_number: the queue containing the number recognized
    """
    # Depending of the platform, the tesseract executable is not located at the same place
    if _platform == "linux" or _platform == "linux2":
        pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
    elif _platform == "darwin":
        pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.0/bin/tesseract"
    elif _platform == "win32":
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    elif _platform == "win64":
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Global loop
    while 1:
        print("Queue size :",queue_images.qsize())
        images = queue_images.get()
        if images is not None:
            for image in images:
                number = Recognition.detect_number(image)
                queue_number.put(number)


def gui(queue_number):
    """
    This function is called by the main Thread, it is the GUI.
    Inside the while loop, it take each number and show a referenced traffic sign in function of the number got.
    :param queue_number: the queue containing the number recognized
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

    # Global loop
    while 1:
        number = queue_number.get()
        img = GUI.GUI(img, number, list)
        sign["image"] = img
        sign.pack()
        canvas.pack()
        text["text"] = number
        text.pack()
        window.update()


######## RUNNING ########
resolution = (2592, 1952)

framerate = 15

processed1 = Queue()                # First queue to contain the images processed by OpenCV
processed2 = Queue()                # Second queue to contain the images processed by OpenCV

recognized = Queue()                # Contains the number recognized by the OCR

t1 = Thread(target = processing, args =(processed1, processed2, resolution, framerate))
t1.start()

t2 = Thread(target = recognition, args =(processed1, recognized))
t2.start()

t3 = Thread(target = recognition, args =(processed2, recognized))
t3.start()

gui(recognized)