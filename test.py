"""
Bonjour
"""
import sys
import cv2
import Processing

img = cv2.imread("assets/Traffic5.jpg", cv2.IMREAD_UNCHANGED)
PreProcessedImg = Processing.pre_processing(img)







# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)[1]
# thresh = improve(thresh) 
# contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contours = contours[0] if len(contours) == 2 else contours[1]

# result = img.copy()
# for c in contours:
#     cv2.drawContours(result, [c], -1, (0, 255, 0), 1)

cv2.waitKey(0)
sys.exit(0)

# TODO peut-être créer un objet sign