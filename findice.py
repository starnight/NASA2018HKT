#!/usr/bin/env python3

import sys

import cv2
import numpy as np
from matplotlib import pyplot as plt

org = cv2.imread(sys.argv[1])
img = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
img = cv2.blur(img,(3,3))
ret,gray = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)
cv2.imwrite(sys.argv[2], gray)

hist = cv2.calcHist([org],[0],None,[256],[0,256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

ret,snow_gray = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)
invsnowgray = cv2.bitwise_not(snow_gray)
snow_bias = 255-invsnowgray.min()
print('Minimum gray value in this snow_gray {}'.format(snow_bias))
snow = cv2.addWeighted(snow_gray, 0.1, snow_gray, 0, 0)
cv2.imwrite(sys.argv[2].replace('.jpg', '-snow.jpg'), snow)

ret,snow_mask = cv2.threshold(snow_gray, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite(sys.argv[2].replace('.jpg', '-snow_mask.jpg'), snow_mask)

ret,snowland = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
cv2.imwrite(sys.argv[2].replace('.jpg', '-snowland.jpg'), snowland)

edges = cv2.Canny(img,100,200)
cv2.imwrite(sys.argv[2].replace('.jpg', '-edge.jpg'), edges)

