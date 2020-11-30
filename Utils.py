import cv2

def draw_contours(img, contours, color):
    for i in range(len(contours)):
        cv2.drawContours(img, contours, i, color, 2, cv2.LINE_8)

