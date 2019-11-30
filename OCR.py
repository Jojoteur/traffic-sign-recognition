# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:06:38 2019

@author: morga
"""
import pytesseract
from PIL import Image
import sys
import cv2 
from numpy import fft,log10,angle,array,zeros,dot,dstack,float32,arange,reshape,savetxt,append,empty,loadtxt,uint8,round,hstack

#############################################Test pytesseract########################
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image= cv2.imread('70_test.png') 

cv2.imshow('bin',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, gray = cv2.threshold(gray, 50, 255,cv2.THRESH_BINARY)
gray_inverse=~gray
img = Image.fromarray(gray_inverse)
cv2.imshow('bin',gray_inverse)
cv2.waitKey(0)
cv2.destroyAllWindows()
txt = pytesseract.image_to_string(img)
print(txt)