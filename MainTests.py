"""
This file contain the program used to make the tests while developing

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### IMPORTS #####
import tkinter

import cv2
import pytesseract
from sys import platform as _platform
from PIL import ImageTk
import Processing
import Recognition

if _platform == "linux" or _platform == "linux2":
    pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
elif _platform == "darwin":
    pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.0/bin/tesseract"
elif _platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
elif _platform == "win64":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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

window = tkinter.Tk()
window.title("Speed limitation")
canvas = tkinter.Canvas(window)

img = ImageTk.PhotoImage(file="assets/blank.jpg")
sign = tkinter.Label(canvas, image=img)
text = tkinter.Label(window, text="")
for elt in Images:
    imgs = Processing.pre_processing(elt)
    print("processed")

    if imgs is not None:
        for image in imgs:
            cv2.imwrite("test.jpg",image)
            number = Recognition.detect_number(image)
            if number is not None:
                print(number)
                if "10" in number:
                    if "110" in number:
                        print("@@@@ 110 @@@@")
                        img = ImageTk.PhotoImage(file="assets/ref110.jpg")
                    else:
                        print("@@@@ 10 @@@@")
                        img = ImageTk.PhotoImage(file="assets/ref10.jpg")
                elif "30" in number:
                    print("@@@@ 30 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref30.jpg")
                elif "45" in number:
                    print("@@@@ 45 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref45.jpg")
                elif "50" in number:
                    print("@@@@ 50 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref50.jpg")
                elif "70" in number:
                    print("@@@@ 70 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref70.jpg")
                elif "80" in number:
                    print("@@@@ 80 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref80.jpg")
                elif "90" in number:
                    print("@@@@ 90 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref90.jpg")
                elif "130" in number:
                    print("@@@@ 130 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref130.jpg")
    sign["image"] = img
    sign.pack()
    canvas.pack()
    text["text"] = number
    text.pack()
    window.update()
    print("END")
    print("\n")
    cv2.waitKey(0)
    cv2.destroyAllWindows()



exit(0)

