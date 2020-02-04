# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:03:37 2019

@author: morgan
File used to test the detection of end speed limits
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import pytesseract
from PIL import Image
import math
from sys import platform as _platform


# Depending of the platform, the tesseract executable is not located at the same place
    if _platform == "linux" or _platform == "linux2":
        pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"
    elif _platform == "darwin":
        pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.0/bin/tesseract"
    elif _platform == "win32":
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    elif _platform == "win64":
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def crop_end(img, circles):
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

def detect_circles_end(img, original):
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
    max = 100
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
    :return: img_threshold_black: the image segmented for black
    """
    img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)                                  # Convert to HSV color-type
                                                   # Eliminate the red
    lower_black = np.array([0, 0, 0])                                               # Range for lower black
    upper_black = np.array([180, 255, 115])                                         # Range for upper black

    mask1 = cv.inRange(img_HSV, lower_black, upper_black)
                             #generating mask
    img_threshold_black = cv.bitwise_and(img,img,mask=mask1)

    return img_threshold_black

def detect_white(img):
    """
    This function is used to highlight white in image to easily detect number
    :param img: the image where we want to detect black
    :return: img_threshold_black: the image segmented for black
    """
    img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)                                  # Convert to HSV color-type

    lower_white = np.array([0,0,168], dtype=np.uint8)
    upper_white = np.array([172,111,255], dtype=np.uint8)
    mask1= cv.inRange(img_HSV, lower_white, upper_white)
    
    #img_HSV[mask>0]=[255,255,255]                                                   # Eliminate the red
                                                                                     
    img_threshold_white = cv.bitwise_and(img, img, mask=mask1)                            

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
    This function returns numbers from an end of speed limit pannel
    :param img: image is focused on the pannel 
    :return : image readable for the OCR method
    """
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
      
    mask = np.zeros_like(imgray)
    
    panneau2=img.copy()
    found, circles,drawn= detect_circles_end(img,panneau2)
    
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


def pre_process_end(img):
    """
    this function is used to pre-process an image of an end of speed limit traffic sign
    param: img RGB 
    return: a treatable image by OCR
    """

    detect_blanc_img=detect_white(img)
    
    img_2=img.copy()
    
    found, circles, drawn = detect_circles_end(detect_blanc_img,img_2)
    
    cv.circle(img, (circles[0][0], circles[0][1]), circles[0][2], (0, 255, 0), 2)
    
    to_return = []
    if found>0:
        extracted = crop_end(img, circles)                                         
        for j in range(np.shape(extracted)[0]):                                    
            if extracted[j] is not None:
                to_return.append(extracted[j])
                
        panneau=to_return[0]
        
    
        image_erode=end_extractor(panneau)
        
    return image_erode

image= cv.imread(r'C:\Users\morga\Desktop\ensem3a\PFE\photo_fin_52.jpg')
cv.imshow('bin',pre_process_end(image))
cv.waitKey(0)
cv.destroyAllWindows()

OCR(pre_process_end(image))


#cap = cv.VideoCapture(0)
#
#while(True):
#    # Capture frame-by-frame
#    ret, frame = cap.read()
#    main(frame)
#    # Our operations on the frame come here
#    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#    
#    # Display the resulting frame
#    cv.imshow('frame',frame)
#    if cv.waitKey(1) & 0xFF == ord('q'):
#        break
#
## When everything done, release the capture
#cap.release()
#cv.destroyAllWindows()


