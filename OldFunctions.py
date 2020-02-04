import numpy as np
import cv2


# Image.putpixel(i, (x, y), 255)
def white_pixels(img):
    """
    This function is used to count the number of white pixels
    :param img: the image with canny filter
    :return: n: the number of pixels white
    """
    n = 0
    (l, h) = np.shape(img)
    for y in range(h):
        for x in range(l):
            if img[x, y] > 50 :
            #if img[x, y] ==255:
                n = n + 1
    print ("nombre de pixels blanc = ", n)
    return n


def detect_number(img):
    """
    This function is used to detect the number is the traffic sign
    :param img: the img with canny filter
    :return:
    """
    nb_white = white_pixels(img)
    #nbTotal = np.shape(img)[0] * np.shape(img)[0]
    #ratio = float(nbWhite) / float(nbTotal)
    validation(nb_white)


def validation(nb_white):
    if (nb_white > 175 and nb_white < 180):
        panneau = 30
        print ("La limitation est de                         :" , panneau)

    if (nb_white > 123 and nb_white < 143):
        panneau = 70
        print ("La limitation est de                         :" , panneau)

    if (nb_white > 161 and nb_white < 165):
        panneau = 50
        print ("La limitation est de                         :" , panneau)


def black_pixels_column_1(img):
    """
    This function is used to find the lower bound culumn of the black picture
    :param img: the image in black and white
    :return: y: lower bound culumn
    """
    (l, h) = np.shape(img)

    for y in range(h):
        n=0
        for x in range(l):
            if img[x, y] ==255:
                n = n + 1
                if n > 5:
                   print ("Column 1 is the  = ", y)
                   return y


def black_pixels_column_2(img):
    """
    This function is used to find the upper bound culumn of the black picture
    :param img: the image in black and white
    :return: y: upper bound culumn
    """

    (l, h) = np.shape(img)
    for y in range( black_pixels_column_1(img)+1 ,h):
        n=0
        for x in range(l):
            if img[x, y] ==0:
                n = n + 1
                if n > 95:
                   print ("Culumn 2 is the ", y)
                   return y


def black_pixels_ligne_1(img):
    """
    This function is used to find the lower bound ligne of the black picture
    :param img: the image in black and white
    :return: y: lower bound ligne
    """
    (l, h) = np.shape(img)

    for x in range(l):
        n=0
        for y in range(h):
            if img[x, y] ==255:
                n = n + 1
                if n > 5:
                   print("Ligne 1 is the  = ", x)
                   return x


def black_pixels_ligne_2(img):
    """
    This function is used to find the upper bound ligne of the black picture
    :param img: the image in black and white
    :return: y: upper bound ligne
    """

    (l, h) = np.shape(img)
    for x in range( black_pixels_ligne_1(img)+1 ,h):
        n=0
        for y in range(h):
            if img[x, y] ==0:
                n = n + 1
                if n > 95:
                   print ("Ligne 2 is the ", x)
                   return x