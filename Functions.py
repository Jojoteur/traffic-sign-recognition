import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
from PIL.Image import *

def detect_red(img):
    """
    This function is used to highlight red in image to easily detect circles
    :param img: the image where we want to detect red (sign)
    :return: img_threshold_red: the image segmented for red
    """
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)                                  # Convert to HSV color-type

    lower_red = np.array([0, 120, 70])                                              # Range for lower red
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(img_HSV, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])                                            # Range for upper red
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(img_HSV, lower_red, upper_red)

    mask1 = mask1 + mask2                                                           # Generating the final mask

    img_threshold_red = cv2.bitwise_and(img, img, mask=mask1)                       # Detect and keep red

    return img_threshold_red


def detect_black(img):
    """
    This function is used to highlight black in image to easily detect number
    :param img: the image where we want to detect black
    :return: img_threshold_black: the image segmented for black
    """
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)                                  # Convert to HSV color-type

    lower_black = np.array([0, 0, 0])                                               # Range for lower black
    upper_black = np.array([180, 255, 100])                                         # Range for upper black

    mask = cv2.inRange(img_HSV, lower_black, upper_black)                           # Generating mask

    return mask                                                                     # Return mask


def detect_circles(img, original):
    """
    This function is used to detect the circles in an image
    :param img: the image where red has been highlighted and where we want to detect circles
    :param original: the original image where circles will be drawn
    :return: result: an array of circles (x, y, r) if at least one circle has been found or FALSE if none circle has been found
    :return: original: the original image with drawn circles to show what circles have been found
    """
    result = []
    size_max = 100                                                          # Size max of the Radius
    n = 0
    found = 0

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                             # Convert to Gray color
    img = cv2.medianBlur(img, 5)                                            # Apply filter to reduce false circles
    rows = img.shape[0]

    while n < size_max:
        max = size_max - n                                                  # Use standard ratio size of traffic sign
        min = int(0.7 * max)

        circles = cv2.HoughCircles(                                         # Detect circles thx to Hough-Method
            img,
            cv2.HOUGH_GRADIENT,
            1,
            rows/4,
            param1=200,
            param2=20,
            minRadius=min,
            maxRadius=max)

        if circles is not None:                                             # If at least one circle has been found
            circles = np.round(circles[0, :]).astype("int")
            for elt in circles:
                result.append(elt)                                          # Add the circle found to an array
            for j in range(np.shape(result)[0]):
                x = result[j][0]
                y = result[j][1]
                r = result[j][2]
                h = r
                w = r
                img[y - h:y + h, x - w:x + w] = 255                         # Replace the circle by a white square
        n = n + 5

    if result is not None:
        found = np.shape(result)[0]                                         # Number of circles found
        for j in range(found):
            x = result[j][0]
            y = result[j][1]
            r = result[j][2]
            cv2.circle(original, (x, y), r, (0, 255, 0), 4)

    return found, result, original


def crop(img, circles):
    """
    This function is used to crop the circles one they have been detected, the goal is to keep only the number inside the circle
    :param img: original image
    :param circles: array of circles (x, y, r) which have been detected in the orginal image
    :return: extracted: array of images which have been extracted thanks to the array of circles
    """
    extracted = []
    print circles
    if circles is not None:
        for (x, y, r) in circles:
            # Create mask for the circle
            mask = np.zeros(img.shape, dtype=np.uint8)
            cv2.circle(mask, (x, y), r, (255, 255, 255), -1, 8, 0)
            out = cv2.copyTo(img, mask)

            # Crop to keep the ROI
            margin = 0
            h = r
            w = r
            out = out[y - h - margin: y + h + margin, x - w - margin: x + w + margin]
            xc = out.shape[0]/2
            yc = out.shape[1]/2
            for i in range(out.shape[0]):
                for j in range(out.shape[1]):
                    if math.sqrt( math.pow((i-xc),2) + math.pow((j-yc),2))>=3*r/4:
                        out[i,j]=255;

            out=cv2.resize(out, (100,100))
            extracted.append(out)

    return extracted

def improve(img):
    """

    :param img:
    :return:
    """
    mask = np.ones((3, 3), np.uint8)

    img_eroded = cv2.erode(img, mask)
    img_open = cv2.dilate(img_eroded, mask)

    return img;

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
    print"nombre de pixels blanc = ", n
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
        print "La limitation est de                         :" , panneau

    if (nb_white > 123 and nb_white < 143):
        panneau = 70
        print "La limitation est de                         :" , panneau

    if (nb_white > 161 and nb_white < 165):
        panneau = 50
        print "La limitation est de                         :" , panneau


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
                   print " Column 1 is the  = ", y
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
                   print " Culumn 2 is the ", y
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
                   print " Ligne 1 is the  = ", x
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
                   print " Ligne 2 is the ", x
                   return x











def algorithm(img):
    """
    Function used to launch the algorithm
    """
    cv2.imshow("Image", img)
    cv2.moveWindow("Image", 0, 0)
    original = img.copy()

    # First highlight red in the image
    img_red = detect_red(img)
    cv2.imshow("Red segmentation", img_red)
    cv2.moveWindow("Red segmentation", 1000, 0)

    # Then detect circles
    found, circles, drawn = detect_circles(img_red, img)
    cv2.imshow("Circles detected", img)
    cv2.moveWindow('Circles detected', 0, 0)

    # Then extract the part of the image where circles has been detected
    if found>0:
        extracted = crop(original, circles)                                         # Extract the detected circles
        for j in range(np.shape(extracted)[0]):                                     # Loop through the array containing the extracted image
            if extracted[j] is not None:
                cv2.imshow("Extracted" + str(j), extracted[j])                      # Show the interesting part
                cv2.moveWindow("Extracted" + str(j), 0, 0)

                img_black = detect_black(extracted[j])
                #cv2.imwrite("assets/img_black.png",img_black)
                cv2.imshow("Black segmentation on extracted " + str(j), img_black)
                cv2.moveWindow("Black segmentation on extracted " + str(j), 0, 0)


                # we croped the img at the different boundaries
                (l, h) = np.shape(img_black)
                img_black=img_black[black_pixels_ligne_1(img_black)-3:black_pixels_ligne_2(img_black)+3,  black_pixels_column_1(img_black)-3:black_pixels_column_2(img_black)+3]
                cv2.imshow("Croped black segmentation on extracted ", img_black)
                cv2.imwrite("assets/Cropedblack.png", img_black)






                """     On ne peut pas utiliser cette fonction pour dire quel chiffre c'est ...
                (l, h) = np.shape(img_black)
                img_black = cv2.resize(img_black, (h*10, l*10), interpolation=cv2.INTER_LANCZOS4)
                cv2.imshow("Croped black img_black 800 800 ", img_black)
                white_pixels(img_black)
                """

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    print("END")
    print "\n"






