import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL.Image import *

final = cv2.imread('assets/ImageFinal.png', -1)
cv2.imshow('assets/ImageFinal.png',final)


Traffic70Ref = cv2.imread('assets/ref70.png', -1)
cv2.imshow('assets/ref70.jpg',Traffic70Ref)
Traffic70Ref = Traffic70Ref[50:195, 50:195]
Traffic70Ref = cv2.resize(Traffic70Ref, (50, 50), interpolation=cv2.INTER_LANCZOS4)
Traffic70Ref = cv2.cvtColor(Traffic70Ref, cv2.COLOR_BGR2GRAY)
Traffic70Ref = cv2.Canny(Traffic70Ref, 0, 1360)
cv2.imwrite('assets/Traffic70Ref.png', Traffic70Ref)
cv2.imshow('Traffic70Ref',Traffic70Ref)













cv2.waitKey(0)
cv2.destroyAllWindows()
exit(0)