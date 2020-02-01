# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:03:37 2019

@author: morga
"""

import numpy as np
import cv2 as cv
import cv2
# from matplotlib import pyplot as plt
import pytesseract
from PIL import Image
import math
from sys import platform as _platform

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def crop(img, circles):
    """
    This function is used to crop the circles one they have been detected, the goal is to keep only the number inside the circle
    :param img: original image
    :param circles: array of circles (x, y, r) which have been detected in the orginal image
    :return: extracted: array of images which have been extracted thanks to the array of circles
    """
    extracted = []
    if circles is not None:
        for (x, y, r) in circles:
            # Create mask for the circle
            mask = np.zeros(img.shape, dtype=np.uint8)
            mask = 255-mask
            #cv.circle(mask, (x, y), r, (255, 255, 255), -1, 8, 0)
            out = img * (mask.astype(img.dtype))
            height = out.shape[0]
            width = out.shape[1]

            # Test if the circle doesn't go outside the image
            if (x - r > 0) & (y - r > 0) & (x + r < width) & (y + r < height):
                # Crop to keep the ROI
                h = r
                w = r
                out = out[y - h: y + h, x - w: x + w]

                xc = out.shape[0] / 2
                yc = out.shape[1] / 2
                for i in range(out.shape[0]):
                    for j in range(out.shape[1]):
                        if math.sqrt(math.pow((i - xc), 2) + math.pow((j - yc), 2)) >= r:
                            out[i, j] = [255, 255, 255]

                out = cv.resize(out, (100, 100), interpolation=cv.INTER_LINEAR)
                extracted.append(out)
    return extracted

def detect_circles(img, original):
    """
    This function is used to detect the circles in an image
    :param img: the image where red has been highlighted and where we want to detect circles
    :param original: the original image where circles will be drawn
    :return: result: an array of circles (x, y, r) if at least one circle has been found or FALSE if none circle has been found
    :return: original: the original image with drawn circles to show what circles have been found
    """
    found = 0
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)                             # Convert to Gray color
    img = cv.medianBlur(img, 5)                                            # Apply filter to reduce false circles
    rows = img.shape[0]

    min = 15
    max = 10000
    circles = cv.HoughCircles(                                             # Detect circles thx to Hough-Method
        img,
        cv.HOUGH_GRADIENT,
        1,
        rows/6,
        param1=200,
        param2=20,
        minRadius=min,
        maxRadius=max)

    if circles is not None:                                                 # If at least one circle has been found
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv.circle(original, (x, y), r, (0, 255, 0), 4)
        found = circles.shape[0]

    return found, circles, original


def detect_black(img):
    """
    This function is used to highlight black in image to easily detect number
    :param img: the image where we want to detect black
    :return img_threshold_black: the image segmented for black
    """
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)              # Convert to HSV color-type

    lower_red = np.array([0, 100, 100])                         # Range for lower red
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(img_HSV, lower_red, upper_red)

    lower_red = np.array([160, 100, 100])                       # Range for upper red
    upper_red = np.array([179, 255, 255])
    mask2 = cv2.inRange(img_HSV, lower_red, upper_red)

    mask = mask1 + mask2

    img_HSV[mask > 0] = [255, 255, 255]                         # Eliminate the red

    lower_black = np.array([0, 0, 0])                           # Range for lower black
    upper_black = np.array([180, 255, 115])                     # Range for upper black

    mask = cv2.inRange(img_HSV, lower_black, upper_black)       # Generating mask

    return mask

def detect_white(img):
    """
    This function is used to highlight white in image to easily detect number
    :param img: the image where we want to detect black
    :return: img_threshold_black: the image segmented for black
    """
    img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)                                  # Convert to HSV color-type

    lower_white = np.array([0,0,0], dtype=np.uint8)
    upper_white = np.array([0,0,255], dtype=np.uint8)
    mask= cv.inRange(img_HSV, lower_white, upper_white)
    
    #img_HSV[mask>0]=[255,255,255]                                                   # Eliminate the red
                                                                                     
    img_threshold_white = cv.bitwise_and(img, img, mask)                            

    return img_threshold_white


def OCR(img):
    """
    This function reads numbers from an image
    :param img: cropped image with numbers in the center
    :return : String value of these numbers
    """
#    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#    _, gray = cv.threshold(gray, 50, 255,cv.THRESH_BINARY)
#    gray_inverse=~gray

    ###OCR detection################
    img = Image.fromarray(img)
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    
    txt = pytesseract.image_to_string(img,config=custom_config)
    print(txt)
    
    return 

def end_extractor(img):
    """
    This function returns numbers from an end speed limit pannel
    :param img: image is focused on the pannel 
    :return : image readable for the OCR method
    """
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(imgray)
    
    panneau2=img.copy()
    found, circles,drawn= detect_circles(img,panneau2)
    
    contours_chiffre=[]
    borne_inf= img.shape[0]/6
    borne_sup=img.shape[0]-borne_inf
    
    for i in range(len(contours)):
        indent=0
        for [[y,x]] in contours[i]:
            if y > borne_inf and y< borne_sup and x>borne_inf and x< borne_sup :
                indent=indent+1
        if indent==len(contours[i]) and len(contours[i])>5:
            contours_chiffre.append(contours[i])
    
    cv.drawContours(mask, contours_chiffre, -1, 255, 2)
    
    cv.fillPoly(mask, contours_chiffre, color=(255,255,255))
    
    
    mask1 = np.ones((6, 6), np.uint8)
    image_erode=cv.erode(mask,mask1)
    
    return image_erode


def crop(img, circles):
    """
    This function is used to crop the circles one they have been detected, the goal is to keep only the number inside the circle
    :param img: original image
    :param circles: array of circles (x, y, r) which have been detected in the orginal image
    :return extracted: array of images which have been extracted thanks to the array of circles
    """
    extracted = []
    if circles is not None:

        for (x, y, r) in circles:
            out = img

            height = out.shape[0]
            width = out.shape[1]

            # Test if the circle doesn't go outside the image
            if (x - r > 0) & (y - r > 0) & (x + r < width) & (y + r < height):
                # Crop to keep the ROI
                h = r
                w = r
                out = out[y - h: y + h, x - w: x + w]

                xc = out.shape[0] / 2
                yc = out.shape[1] / 2
                for i in range(out.shape[0]):
                    for j in range(out.shape[1]):
                        if math.sqrt(math.pow((i - xc), 2) + math.pow((j - yc), 2)) > int(r):
                            out[i, j] = [255, 255, 255]

                out = cv2.resize(out, (100, 100), interpolation=cv2.INTER_LINEAR)
                extracted.append(out)
    return extracted


def test(img):
    #    cv.imshow('bin',img)
    #    cv.waitKey(0)
    #    cv.destroyAllWindows()
    cv.imshow('1', img)

    detect_blanc_img = detect_white(img)
    img_2 = img.copy()

    found, circles, drawn = detect_circles(detect_blanc_img, img_2)
    to_return = []
    if found > 0:
        extracted = crop(img, circles)
        for j in range(np.shape(extracted)[0]):
            if extracted[j] is not None:
                to_return.append(extracted[j])

                panneau = to_return[0]

                image_erode = end_extractor(panneau)
                print(OCR(image_erode))
                cv.imshow('bin', image_erode)

                cv.waitKey(0)
                cv.destroyAllWindows()

    return 1

    signs = []
    print(found)
    if found > 0:
        extracted = crop(original, circles)  # Extract the detected circles
        for j in range(np.shape(extracted)[0]):  # Loop through the array containing the extracted image
            if extracted[j] is not None:
                # cv2.imshow("Extracted" + str(j), extracted[j])
                # cv2.moveWindow("Extracted" + str(j), 0, 0)

                img_black = detect_black(extracted[j])  # Detect black (the number at the center of the sign)
                # cv2.imshow("Black segmentation on extracted " + str(j), img_black)
                # cv2.moveWindow("Black segmentation on extracted " + str(j), 0, 0)

                img_black = improve(img_black)  # Erosion dilation to reducing number of particles
                cv2.imshow("Improve after black semgentation" + str(j), img_black)
                # cv2.moveWindow("Improve after black semgentation"  + str(j), 0, 0)

                signs.append(img_black)

    return signs


def main(img):

#    cv.imshow('bin',img)
#    cv.waitKey(0)
#    cv.destroyAllWindows()
    cv.imshow('1', img)

    detect_blanc_img=detect_white(img)
    img_2=img.copy()
    
    found, circles, drawn = detect_circles(detect_blanc_img,img_2)
    to_return = []
    if found>0:
        extracted = crop(img, circles)                                         
        for j in range(np.shape(extracted)[0]):                                    
            if extracted[j] is not None:
                to_return.append(extracted[j])
                
                panneau=to_return[0]
    
                image_erode=end_extractor(panneau)
                print(OCR(image_erode))
                cv.imshow('bin',image_erode)

                cv.waitKey(0)
                cv.destroyAllWindows()
    
    return 1


# cap = cv.VideoCapture(0)
#
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     main(frame)
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     cv.imshow('frame',frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()


if _platform == "linux" or _platform == "linux2":
    pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
elif _platform == "darwin":
    pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.0/bin/tesseract"
elif _platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
elif _platform == "win64":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Itraffic13 = cv.imread("assets/Traffic13.jpeg", -1)
main(Itraffic13)

