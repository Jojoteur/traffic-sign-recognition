"""
This file contains all the functions used to make the image processing before OCR

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### IMPORTS #####
import cv2
import numpy as np
import math

##### FUNCTIONS #####
def detect_red(img):
    """
    This function is used to highlight red in image to easily detect circles
    :param img: the image where we want to detect red (sign)
    :return img_threshold_red: the image segmented for red
    """
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)              # Convert to HSV color-type

    lower_red = np.array([0, 100, 100])                         # Range for lower red
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(img_HSV, lower_red, upper_red)

    lower_red = np.array([160, 100, 100])                       # Range for upper red
    upper_red = np.array([179, 255, 255])
    mask2 = cv2.inRange(img_HSV, lower_red, upper_red)

    mask1 = mask1 + mask2                                       # Generating the final mask

    img_threshold_red = cv2.bitwise_and(img, img, mask=mask1)   # Detect and keep red

    return img_threshold_red


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


def detect_circles(img, original):
    """
    This function is used to detect the circles in an image
    :param img: the image where red has been highlighted and where we want to detect circles
    :param original: the original image where circles will be drawn
    :return result: an array of circles (x, y, r) if at least one circle has been found or FALSE if none circle has been found
    :return original: the original image with drawn circles to show what circles have been found
    """
    found = 0
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                 # Convert to Gray color
    img = cv2.medianBlur(img, 5)                                # Apply filter to reduce false circles
    rows = img.shape[0]

    min = 5
    max = 1000
    circles = cv2.HoughCircles(                                 # Detect circles thx to Hough-Method
        img,
        cv2.HOUGH_GRADIENT,
        1,
        rows,
        param1=200,
        param2=20,
        minRadius=min,
        maxRadius=max)

    # If at least one circle has been found
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        """
        # For Highlighting circles but useless in production
        for (x, y, r) in circles:
            cv2.circle(original, (x, y), r, (0, 255, 0), 4)
        """
        found = circles.shape[0]

    return found, circles, original


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


def improve(img):
    """
    This function is used to improve the image after black detection (with erosion and dilation)
    :param img: the image where black segmentation has been made
    :return img_open: the image with erosion and dilation
    """
    mask = np.ones((3, 3), np.uint8)
    img_eroded = cv2.erode(img, mask)
    img_open = cv2.dilate(img_eroded, mask)
    return img_open


def pre_processing(img):
    """
    Function used to launch the pre-processing operation
    :param img: the image captured
    :return signs: array of all images detected as traffic sign
    """

    original = img.copy()
    #cv2.imshow("Image", orginal)
    #cv2.moveWindow("Image", 0, 0)

    img_red = detect_red(img)                                       # First highlight red in the image
    #cv2.imshow("Red segmentation", img_red)
    #cv2.moveWindow("Red segmentation", 1000, 0)

    found, circles, drawn = detect_circles(img_red, img)            # Then detect circles
    #cv2.imshow("Circles detected", drawn)
    #cv2.moveWindow('Circles detected', 0, 0)

    # Then extract the part of the image where circles has been detected
    signs = []
    print(found)
    if found > 0:
        extracted = crop(original, circles)         # Extract the detected circles
        for j in range(np.shape(extracted)[0]):     # Loop through the array containing the extracted image
            if extracted[j] is not None:
                #cv2.imshow("Extracted" + str(j), extracted[j])
                #cv2.moveWindow("Extracted" + str(j), 0, 0)

                img_black = detect_black(extracted[j])      # Detect black (the number at the center of the sign)
                #cv2.imshow("Black segmentation on extracted " + str(j), img_black)
                #cv2.moveWindow("Black segmentation on extracted " + str(j), 0, 0)

                img_black = improve(img_black)              # Erosion dilation to reducing number of particles
                cv2.imshow("Improve after black semgentation" + str(j), img_black)
                #cv2.moveWindow("Improve after black semgentation"  + str(j), 0, 0)

                signs.append(img_black)

    return signs