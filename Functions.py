import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
from PIL.Image import *


def detectCircles(img):
    """
    This function is used to detect the circles in an image
    :param img: the image where we want to detect circles
    :return: result: an array of circles (x, y, r) if at least one circle has been found or FALSE if none circle has been found
    :return: orginal: the orginal image with drawn circles to show what circles have been found
    """

    original = img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to Gray color
    img = cv2.medianBlur(img, 5)  # Apply filter to reduce false circles
    cv2.imshow("test", img)
    cv2.moveWindow("test",0,0)
    rows = img.shape[0]
    cols = img.shape[1]

    result = []
    sizeMax = 101 # Size max of the Radius
    n = 0

    while (n < sizeMax):
        max = sizeMax - n  # Use standard ratio size of traffic sign
        min = int(0.65 * max)

        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=40, minRadius=min,
                                   maxRadius=max)

        if circles is not None:  # If circle has been found
            circles = np.round(circles[0, :]).astype("int")
            for elt in circles:
                result.append(elt)  # Add the circle found to an array
            for j in range(np.shape(result)[0]):
                x = result[j][0]
                y = result[j][1]
                r = result[j][2]
                h = r
                w = r
                img[y - h:y + h, x - w:x + w] = 0  # Replace the circle by a black square

        n = n + 5

    if result is not None:
        for j in range(np.shape(result)[0]):
            x = result[j][0]
            y = result[j][1]
            r = result[j][2]
            cv2.circle(original, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(original, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

        return result, original

    return False, original


def extractCirclesAfterDetection(img, circles):
    """
    This function is used to crop the circles one they have been detected
    :param img: original image
    :param circles: array of circles (x, y, r) which have been detected in the orginal image
    :return: croped: array of images which have been extracted thanks to the array of circles
    """
    extracted = []
    print circles
    if circles is not None:
        for (x, y, r) in circles:
            h = r
            w = r
            temp = img[y - h: y + h, x - w: x + w]
            temp = cv2.resize(temp, (100, 100), interpolation=cv2.INTER_LANCZOS4)
            #cv2.imwrite('assets/temp.png', temp)

            extracted.append(temp)
    return extracted

def cropCirclesCanny(img):
    """
    This function is used to crop the image more precisely and keep only the number if the image is a traffic sign and then apply the canny filter
    :param img: the image containing the circle which has been extracted thanks to extractCirclesAfterDetection()
    :return: final: the croped image
    """
    temp = img[25:75, 25:50]  # half of the image
    final = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    final = cv2.Canny(final, 0, 200)

    #cv2.imwrite('assets/ImageFinal.png', final)
    cv2.imshow('Canny croped',final)
    cv2.moveWindow('Canny croped', 0, 0)

    return final





def detectRed(img):
    """
    This function is used to detect the red color on an image and decide if the image is a sign or not, it enable to
    eliminate false positives found by detectCircles
    :param img: the image croped by extractCirclesAfterDetection
    :return: imgThresholdr: the image with the red highlighted
    :return: sign: TRUE if the image is a sign or FALSE if not
    """
    sign = False

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Convert to HSV color-type

    # hue_hist = cv2.calcHist([imgHSV], [0], None, [180], [0, 180])  # Find the histogram for the hue band
    # plt.plot(hue_hist)
    # plt.xticks(np.arange(0, 190, step=10))  # Config the x axis for better view
    # plt.show()

    h, s, v = cv2.split(imgHSV);  # Split to work only on h (hue)

    redthreshold = np.where(((h >= 175) & (h <= 180)) | ((h >= 0) & (h <= 5)))

    imgThresholdr1 = np.zeros((np.shape(img)[0], np.shape(img)[1]))
    imgThresholdr2 = np.zeros((np.shape(img)[0], np.shape(img)[1]))
    imgThresholdr3 = np.zeros((np.shape(img)[0], np.shape(img)[1]))

    imgThresholdr1[redthreshold] = h[redthreshold]
    imgThresholdr2[redthreshold] = s[redthreshold]
    imgThresholdr3[redthreshold] = v[redthreshold]

    imgThresholdr = imgHSV

    imgThresholdr[:, :, 0] = imgThresholdr1
    imgThresholdr[:, :, 1] = imgThresholdr2
    imgThresholdr[:, :, 2] = imgThresholdr3
    cv2.imshow(",,", imgThresholdr)
    imgThresholdr = cv2.cvtColor(imgThresholdr, cv2.COLOR_HSV2BGR)


    nbred = np.shape(redthreshold)[1]
    nbtotal = np.shape(h)[0] * np.shape(h)[0]
    ratio = float(nbred) / float(nbtotal)

    print ratio

    if ratio > 0.25:
        sign = True


    return imgThresholdr, True


# Image.putpixel(i, (x, y), 255)
def whitePixels(img):
    """
    This function is used to count the number of white pixels
    :param img: the image with canny filter
    :return: n: the number of pixels white
    """
    n = 0
    (l, h) = np.shape(img)
    for y in range(h):
        for x in range(l):
            if (img[x,y] == 255):
                n = n + 1
    print"nombre de pixels blanc = ", n
    return n


def detectNumber(img):
    """
    This function is used to detect the number is the traffic sign
    :param img: the img with canny filter
    :return:
    """
    nbWhite = whitePixels(img)
    #nbTotal = np.shape(img)[0] * np.shape(img)[0]
    #ratio = float(nbWhite) / float(nbTotal)
    validation(nbWhite)






def validation(nbWhite):
    if (nbWhite > 175 and nbWhite < 180):
        panneau = 30
        print "La limitation est de                         :" , panneau

    if (nbWhite > 123 and nbWhite < 143):
        panneau = 70
        print "La limitation est de                         :" , panneau

    if (nbWhite > 161 and nbWhite < 165):
        panneau = 50
        print "La limitation est de                         :" , panneau



def Algorithm(img):
    """
    Function used to launch the algorithm
    """
    # cv2.imshow("Img", img)
    c, d = detectCircles(img)                                               # Detect circles in the image

    cv2.imshow("Circles detected", d)
    cv2.moveWindow('Circles detected', 0, 0)

    extracted = extractCirclesAfterDetection(img, c)                        # Extract the detected circles


    for j in range(np.shape(extracted)[0]):                                 # Loop through the array containin the extracted image
        if extracted[j] is not None:
            cv2.imshow("Croped " + str(j), extracted[j])
            cv2.moveWindow('Croped', 0, 0)
            colored, sign = detectRed(extracted[j])                         # Detect presence of red in the extracted image

            print "Image is a traffic sign: "+str(sign)

            if sign == True:                                                # If we are sure than the image is traffic sign
                cv2.imshow("Croped colored" + str(j), colored)
                cv2.moveWindow("Croped colored", 0, 0)
                ImageCropCanny = cropCirclesCanny(extracted[j])             # Crop to keep the number and apply canny filter
                detectNumber(ImageCropCanny)

    print("END")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print "\n"





