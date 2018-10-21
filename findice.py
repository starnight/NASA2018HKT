#!/usr/bin/env python3

import sys

import cv2
import numpy as np
from matplotlib import pyplot as plt

org = cv2.imread(sys.argv[1])

hist = cv2.calcHist([org],[0],None,[256],[0,256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

thres = 50

img = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
img = cv2.blur(img,(3,3))
cv2.imwrite(sys.argv[2].replace('.jpg', '-blur.jpg'), img)

ret,gray = cv2.threshold(img, thres, 255, cv2.THRESH_TOZERO)
cv2.imwrite(sys.argv[2], gray)

ret,snow_gray = cv2.threshold(img, thres, 255, cv2.THRESH_TOZERO)
invsnowgray = cv2.bitwise_not(snow_gray)
cv2.imwrite(sys.argv[2].replace('.jpg', '-snow_gray.jpg'), snow_gray)

snow_thres = 200
ret,snow_mask = cv2.threshold(snow_gray, snow_thres, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite(sys.argv[2].replace('.jpg', '-snow_mask.jpg'), snow_mask)

snow = cv2.bitwise_and(snow_gray, snow_gray, mask=snow_mask)
snow = cv2.addWeighted(snow, 1, snow, 0, -snow_thres)
cv2.imwrite(sys.argv[2].replace('.jpg', '-snow.jpg'), snow)

ret,snowland_mask = cv2.threshold(gray, thres, 255, cv2.THRESH_BINARY)
cv2.imwrite(sys.argv[2].replace('.jpg', '-snowland_mask.jpg'), snowland_mask)

edges = cv2.Canny(img,100,200)
cv2.imwrite(sys.argv[2].replace('.jpg', '-edge.jpg'), edges)

