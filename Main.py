import cv2
import Functions
import time
from PIL.Image import *
import cv2
import os

nombreDeBoucles=0
a = 0
i=0
securite=1

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, 1)
    cv2.imwrite('assets/hsv_frame.png', hsv_frame)
    hsv_frame = cv2.imread('assets/hsv_frame.png', -1)
    Functions.selection(hsv_frame)


    if(Functions.selection(frame)=="valide"):
       i=i+1
       finalpixels = open("assets/ImageFinal.png")          # permet de calculer le nombre de pixel moyen blanc pour le chiffre de gauche
       NombrePixel=Functions.whitePixels(finalpixels)
       a=a+NombrePixel
       nombreDeBoucles = nombreDeBoucles + 1
       NombrePixelMoyenne=a/nombreDeBoucles
       print "le nombre de pixel moyen est" , NombrePixelMoyenne
       if i==securite:
          Functions.validation(NombrePixelMoyenne)
          i=0
    else:
        Noir=cv2.imread('assets/Noir.png', 1)
        cv2.imwrite('assets/ImageFinal.png',Noir)
        nombreDeBoucles=0
        a=0



    key = cv2.waitKey(1)
    if key == 27:
        break



"""
#### Test with some images ####
Itraffic1 = cv2.imread("assets/Traffic1.jpg", -1)
Itraffic2 = cv2.imread("assets/Traffic2.jpg", -1)
Itraffic3 = cv2.imread("assets/Traffic3.jpg", -1)
Itraffic4 = cv2.imread("assets/Traffic4.jpg", -1)
Itraffic5 = cv2.imread("assets/Traffic5.jpg", -1)
Itraffic6 = cv2.imread("assets/Traffic6.jpg", -1)
Itraffic7 = cv2.imread("assets/Traffic7.jpg", -1)
Itraffic8 = cv2.imread("assets/Traffic8.jpg", -1)
Itraffic9 = cv2.imread("assets/Traffic9.jpg", -1)
Itraffic10 = cv2.imread("assets/Traffic10.jpg", -1)
Itraffic11 = cv2.imread("assets/Traffic11.jpg", -1)
Itraffic12 = cv2.imread("assets/Traffic12.jpg", -1)
Itraffic13 = cv2.imread("assets/Traffic13.jpg", -1)

ref30 = cv2.imread("assets/ref30.jpg", -1)


Functions.test(Itraffic1)
Functions.test(Itraffic2)
Functions.test(Itraffic3)
Functions.test(Itraffic4)
Functions.test(Itraffic5)
Functions.test(Itraffic6)
Functions.test(Itraffic7)
Functions.test(Itraffic8)
Functions.test(Itraffic9)
Functions.test(Itraffic10)
Functions.test(Itraffic11)
Functions.test(Itraffic12)
Functions.test(Itraffic13)

"""

## END ##
cv2.waitKey(0)
cv2.destroyAllWindows()

exit(0)
