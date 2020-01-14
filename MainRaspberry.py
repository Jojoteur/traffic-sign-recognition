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
import sys

######## THREADS DEFINITIONS ########
def processing_ip(queue1, queue2, queue3):
    """
    Processing with the IP Cam
    This function is the function executed by the first thread, it launch the capture of images by the camera and
    process them by the algorithm established in the file "Processing".
    Each image returned by the processing algorithm is put on a queue.
    :param queue1: the fist queue where to put images detected
    :param queue2: the second queue where to put images detected
    """

    class VideoCapture:
        def __init__(self, name):
            IP = str(sys.argv[1])                                       # Get Ip from arguments
            self.cap = cv2.VideoCapture('http://'+IP+':8080/video')
            self.q = Queue()
            t = Thread(target=self._reader)
            t.daemon = True
            t.start()

        # Read frames as soon as they are available, keeping only most recent one
        def _reader(self):
            while True:
                ret, frame = self.cap.read()
                if not ret:                                             # If there is not frame
                    break
                if not self.q.empty():
                    try:
                        self.q.get_nowait()                             # Discard previous (unprocessed) frame
                    except Queue.Empty:
                        pass
                self.q.put(frame)                                       # Put the new frame inside the queue

        def read(self):
            return self.q.get()                                         # Get the frame in the queue

    cap = VideoCapture(0)
    i = 1
    while True:
        frame = cap.read()
        images = Processing.pre_processing(frame)                       # Image processing
        # Use 3 queues (3 threads) to make the recognitions (in case of lots images)
        if images is not None:
            if i == 1:
                queue1.put(images)
            elif i == 2:
                queue2.put(images)
            elif i == 3:
                queue3.put(images)

        if i <= 2:
            i = i + 1
        else:
            i = 0
        if chr(cv2.waitKey(1) & 255) == 'q':
            break
    cv2.destroyAllWindows()


def processing_picam(queue1, queue2, resolution, framerate):
    """
    Processing with the Pi cam
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
    This gets the images stored in the queue and use the recognition algorithm
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
    # Initializing the GUI
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window)

    img = ImageTk.PhotoImage(file="assets/blank.jpg")
    sign = tkinter.Label(canvas, image=img)
    text = tkinter.Label(window, text="")

    # Global loop
    while 1:
        number = queue_number.get()
        img = GUI.GUI(img, number)
        sign["image"] = img
        sign.pack()
        canvas.pack()
        text["text"] = number
        text.pack()
        window.update()


######## RUNNING ########

processed1 = Queue()                # First queue to contain the images processed by OpenCV
processed2 = Queue()                # Second queue to contain the images processed by OpenCV
processed3 = Queue()                # Third queue to contain the images processed by OpenCV


recognized = Queue()                # Contains the numbers recognized by the OCR

if sys.argv[1] is not None:         # When we want to use an IP Camera
    t1 = Thread(target = processing_ip, args =(processed1, processed2))
else:                               # When we want to use the PI Camera /!\ NO USB !
    resolution = (1920, 1088)
    framerate = 30
    t1 = Thread(target = processing_picam, args=(processed1, processed2, resolution, framerate))
t1.start()

t2 = Thread(target = recognition, args =(processed1, recognized))
t2.start()

t3 = Thread(target = recognition, args =(processed2, recognized))
t3.start()

t4 = Thread(target = recognition, args =(processed3, recognized))
t4.start()

gui(recognized)