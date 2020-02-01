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
def process_ip(processed1, processed2):
    """
    Processing with the IP Cam
    This function is the function executed by the first thread, it launch the capture of images by the camera and
    process them by the algorithm established in the file "Processing".
    Each image returned by the processing algorithm is put on a queue.
    :param queue1: the fist queue where to put detected images
    :param queue2: the second queue where to put detected images
    source used for this function: https://stackoverflow.com/questions/54460797/how-to-disable-buffer-in-opencv-camera
    """
    receiving = True

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
            return self.q.get()                                         # Get the frame in the queue (timeout of 10 secs)

    cap = VideoCapture(0)

    while receiving:
        frame = cap.read()
        i = 0
        images_speed_limit = Processing.detect_speed_limit(frame)
        images_end_speed_limit = Processing.detect_end_speed_limit(frame)
        # Use 2 queues (2 threads) to make the recognitions (in case of lots images)
        if images_speed_limit is not None:
            if i % 2 == 0:
                processed1.put((images_speed_limit, "speed_limit"))
            else:
                processed2.put((images_speed_limit, "speed_limit"))
            i = i + 1
        if images_end_speed_limit is not None:
            if i % 2 == 0:
                processed1.put((images_end_speed_limit, "end_speed_limit"))
            else:
                processed2.put((images_end_speed_limit, "end_speed_limit"))
            i = i + 1

        # Reset the counter to avoid big number problems
        if i <= 11:
            i = i + 1
        else:
            i = 0

        if chr(cv2.waitKey(1) & 255) == 'q':
            break

    cv2.destroyAllWindows()




def process_picam(processed1, processed2, resolution, framerate):
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

    # Global loop
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array                         # Convert frame to array understood by OpenCv
        i = 0
        images_speed_limit = Processing.detect_speed_limit(frame)
        images_end_speed_limit = Processing.detect_end_speed_limit(frame)

        # Use 2 queues (2 threads) to make the recognitions (in case of lots images)
        if images_speed_limit is not None:
            if i % 2 == 0:
                processed1.put((images_speed_limit, "speed_limit"))
            else:
                processed2.put((images_speed_limit, "speed_limit"))
            i = i + 1
        if images_end_speed_limit is not None:
            if i % 2 == 0:
                processed1.put((images_end_speed_limit, "end_speed_limit"))
            else:
                processed2.put((images_end_speed_limit, "end_speed_limit"))
            i = i + 1
        rawCapture.truncate(0)                     # Clear the stream in preparation for the next frame

        # Reset counter to avoid big number problems
        if i <= 11:
            i = i + 1
        else:
            i = 0

        if cv2.waitKey(40) & 0xFF == ord('q'):
            break


    cv2.destroyAllWindows()


def recognition(queue_images, queue_number):
    """
    This gets the images stored in the queue and use the recognition algorithm established in the file "Recognition".
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
    while True:
        print("Queue size :",queue_images.qsize())
        images, type = queue_images.get()
        if images is not None:
            for image in images:
                number = Recognition.detect_number(image)
                queue_number.put((number, type))


def gui(recognized):
    """
    This function is called by the main Thread, it is the GUI.
    Inside the while loop, it takes each number and shows a referenced traffic sign in function of the number got.
    :param queue_number: the queue containing the number recognized
    """
    # Initializing the GUI
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window)

    img = ImageTk.PhotoImage(file="assets/blank.jpg")
    sign = tkinter.Label(canvas, image=img)
    text = tkinter.Label(window, text="")

    # Global loop
    while True:
        number, type = recognized.get()
        if number is not None:
            img = GUI.GUI(img, number, type)
            sign["image"] = img
            sign.pack()
            canvas.pack()
            text["text"] = number
            text.pack()
            window.update()

######## RUNNING ########
processed1 = Queue()                # First queue to contain the images processed by OpenCV
processed2 = Queue()                # Second queue to contain the images processed by OpenCV

recognized = Queue()                # Contains the numbers recognized by the OCR

if sys.argv is not None:            # When we want to use an IP Camera
    print("Application launched with IP camera !")
    t1 = Thread(target = process_ip, args = (processed1, processed2))
else:                               # When we want to use the PI Camera /!\ NO USB !
    print("Application launched with Pi Cam !")
    resolution = (1920, 1088)
    framerate = 30
    t1 = Thread(target = process_picam, args = (processed1, processed2, resolution, framerate))
t1.start()


t2 = Thread(target = recognition, args =(processed1, recognized))
t2.start()

t3 = Thread(target = recognition, args =(processed2, recognized))
t3.start()


gui(recognized)
