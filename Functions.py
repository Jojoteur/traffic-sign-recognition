import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

def detectCircles(img):
    """
    Function used to detect Circles in a image, return the list of the circles and the image which drawn circles
    """
    n = 0

    original = img.copy()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.medianBlur(img, 5)  # Apply filter to reduce false circles

    rows = img.shape[0]
    result = []
    while (n < 100):
        max = 100 - n  # Use standard ration size of traffic sign
        min = int(0.65 * max)

        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=250, param2=40, minRadius=min,
                                   maxRadius=max)

        if circles is not None:  # If circle has been found
            circles = np.round(circles[0, :]).astype("int")
            for elt in circles:
                result.append(elt)  # Add the circle found to an array
            for j in range(np.shape(result)[0]):
                print result[j]
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


def cropCircles(img, circles):
    """
    Function used to crop the image around the detected circles
    """
    croped = []
    if circles is not None:
        for (x, y, r) in circles:
            h = int(r/1.95)
            w = int(r/1.95)

            temp = img[y - h :y + h, x - w :x + w ]           # on enregistre canny + resized      La fonction renvoit resized pour pouvoir travailler dessus mais on doit modifier ca  bisous je t'aime

            resized_image = cv2.resize(temp, (50, 50), interpolation=cv2.INTER_LANCZOS4)

            final = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
            final = cv2.Canny(final, 0, 200)

            cv2.imwrite('assets/ImageFinal.png', final)

            croped.append(resized_image)
            cv2.imwrite('assets/resized_image.png', resized_image)
    return croped

def cropCirclesOld(img, circles):
    """
    Function used to crop the image around the detected circles
    """
    croped = []
    margin = 5
    if circles is not None:
        for (x, y, r) in circles:
            h = r
            w = r
            temp = img[y-h-margin:y+h+margin, x-w-margin:x+w+margin]
            croped.append(temp)
    return croped



def detectRed(img):
    """
    Function used to detect if the image is a sign (to eliminate false)
    """
    sign = False

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Convert to HSV color-type

    #hue_hist = cv2.calcHist([imgHSV], [0], None, [180], [0, 180])  # Find the histogram for the hue band
    # plt.plot(hue_hist)
    # plt.xticks(np.arange(0, 190, step=10))  # Config the x axis for better view
    # plt.show()

    h, s, v = cv2.split(imgHSV);  # Split to work only on h (hue)

    redthreshold = np.where(((h > 170) & (h <= 180)) | ((h >= 0) & (h < 10)))

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

    imgThresholdr = cv2.cvtColor(imgThresholdr, cv2.COLOR_HSV2BGR)

    nbred = np.shape(redthreshold)[1]
    nbtotal = np.shape(h)[0] * np.shape(h)[0]
    ratio = float(nbred) / float(nbtotal)

    print ratio

    if ratio > 0.2:
        sign = True

    return imgThresholdr, sign


def test(img):
    """
    Function used to test the algorithm
    """
 #   cv2.imshow("Img", img)
    c, d = detectCircles(img)

  #  cv2.imshow("Circles detected", d)

    croped = cropCircles(img, c)
    j = 0

    for j in range(np.shape(croped)[0]):
        #    cv2.imshow("Croped " + str(j), croped[j])
        colored, sign = detectRed(croped[j])
        #  cv2.imshow("Croped colored " + str(j), colored)
        print sign

    print("END")
    #cv2.waitKey(0)
    cv2.destroyAllWindows()

    print "\n" * 10
