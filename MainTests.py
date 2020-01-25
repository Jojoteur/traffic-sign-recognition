"""
This file contain the program used to make the tests while developing

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### IMPORTS #####
import cv2
import pytesseract
from sys import platform as _platform
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

stream = cv2.VideoCapture('http://192.168.0.107:8080/video')

stream.set(cv2.CAP_PROP_BUFFERSIZE, 1);
stream.set(cv2.CAP_PROP_FPS, 2);
stream.set(cv2.CAP_PROP_POS_FRAMES , 1);
while(cap.isOpened()):
    r, f = stream.read()
    cv2.imshow('IP Camera stream', f)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

import cv2, queue, threading, time

class VideoCapture:
  def __init__(self, name):
    self.cap = cv2.VideoCapture('http://192.168.0.107:8080/video')
    self.q = queue.Queue()
    t = threading.Thread(target=self._reader)
    t.daemon = True
    t.start()

  # read frames as soon as they are available, keeping only most recent one
  def _reader(self):
    while True:
      ret, frame = self.cap.read()
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()   # discard previous (unprocessed) frame
        except queue.Empty:
          pass
      self.q.put(frame)

  def read(self):
    return self.q.get()

cap = VideoCapture(0)
while True:
  frame = cap.read()
  imgs = Processing.pre_processing(frame)
  if imgs is not None:
      for image in imgs:
          number = Recognition.detect_number(image)
          print(number)

  # print("END")
  # print("\n")
  if chr(cv2.waitKey(1)&255) == 'q':
    break

"""

#### Test with some images ####
Images = []

Itraffic1 = cv2.imread("assets/Traffic1.jpg", -1)
Itraffic2 = cv2.imread("assets/Traffic2.jpg", -1)
Itraffic3 = cv2.imread("assets/Traffic3.jpg", -1)
Itraffic4 = cv2.imread("assets/Traffic4.jpg", -1)
Itraffic5 = cv2.imread("assets/Traffic5.JPG", -1)
Itraffic6 = cv2.imread("assets/Traffic6.jpg", -1)
Itraffic7 = cv2.imread("assets/Traffic7.jpg", -1)
Itraffic8 = cv2.imread("assets/Traffic8.jpg", -1)
Itraffic9 = cv2.imread("assets/Traffic9.jpg", -1)
Itraffic10 = cv2.imread("assets/Traffic10.jpg", -1)
Itraffic11 = cv2.imread("assets/Traffic11.jpg", -1)
Itraffic12 = cv2.imread("assets/Traffic12.jpg", -1)
Itraffic13 = cv2.imread("assets/Traffic13.jpg", -1)


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

if _platform == "linux" or _platform == "linux2":
    pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
elif _platform == "darwin":
    pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.0/bin/tesseract"
elif _platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
elif _platform == "win64":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


for elt in Images:
    imgs = Processing.pre_processing(elt)
    print("processed")
    if imgs is not None:
        for image in imgs:
            txt = Recognition.detect_number(image)
            if txt is not None:
                if "10" in txt:
                    if "110" in txt:
                        print("@@@@ 110 @@@@")
                    else:  print("@@@@ 10 @@@@")
                elif "30" in txt:
                    print("@@@@ 30 @@@@")
                elif "45" in txt:
                    print("@@@@ 45 @@@@")
                elif "50" in txt:
                    print("@@@@ 50 @@@@")
                elif "70" in txt:
                    print("@@@@ 70 @@@@")
                elif "80" in txt:
                    print("@@@@ 80 @@@@")
                elif "90" in txt:
                    print("@@@@ 90 @@@@")
                elif "130" in txt:
                    print("@@@@ 130 @@@@")
    print("END")
    print("\n")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


cv2.destroyAllWindows()
exit(0)

