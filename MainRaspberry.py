"""
This file contain the programm launched by the Raspberry Pi

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### Imports ######
import time
import cv2
from imutils.video import VideoStream

import PreProcessing
import Recognition

##### Program ######

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
            print(number)

    print("END")
    print("\n")

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
vs.stop()