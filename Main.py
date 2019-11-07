import cv2
import Functions
import time


cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, 1)
    #  cv2.imwrite('assets/hsv_frame.bmp', hsv_frame)
    # hsv_frame = cv2.imread('assets/hsv_frame.bmp', -1)
    Functions.test(hsv_frame)
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
