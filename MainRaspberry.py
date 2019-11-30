"""
This file contain the programm launched by the Raspberry Pi

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

import time
import cv2
from imutils.video import VideoStream

import PreProcessing
import Recognition


# Initialization
vs = VideoStream(usePiCamera=True, resolution=(1920, 1080)).start()

# Give time to make the focus
time.sleep(2.0)

while(1):
    # Reading the flux
    frame = vs.read()

    img = PreProcessing.algorithm(frame)
    if img is not None:
        number = Recognition.detect_number(img)
        print(number)

    key = cv2.waitKey(1) & 0xFF

cv2.destroyAllWindows()
vs.stop()