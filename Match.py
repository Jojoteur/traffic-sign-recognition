import cv2
import numpy as np
from matplotlib import pyplot as plt

final = cv2.imread('assets/ImageFinal.png', -1)
cv2.imshow('assets/ImageFinal.png',final)


panneau50 = cv2.imread('assets/panneau50.png', -1)
cv2.imshow('assets/panneau50.png',panneau50)
panneau50 = panneau50[10:220, 10:220]
panneau50 = cv2.resize(panneau50, (50, 50), interpolation=cv2.INTER_LANCZOS4)
panneau50 = cv2.cvtColor(panneau50, cv2.COLOR_BGR2GRAY)
panneau50 = cv2.Canny(panneau50, 0, 100)
cv2.imshow('panneau50',panneau50)

















cv2.waitKey(0)
cv2.destroyAllWindows()
exit(0)