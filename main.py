import cv2
import numpy as np
from numpy import asarray

image = cv2.imread('./Assets/Panel 1.jpg')

image = cv2.resize(image, (500, 500), interpolation = cv2.INTER_AREA)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

blur = cv2.GaussianBlur(gray, (171,171), cv2.BORDER_DEFAULT)

canny = cv2.Canny(hsv, 450, 450)
# canny = cv2.Canny(blur, 200, 200)

percentage = 0

ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cv2.imshow('Binary image', thresh)

lb = np.array([0, 25, 10])
hb = np.array([20, 155, 150])

mask = cv2.inRange(hsv, lb, hb)

segmented_img = cv2.bitwise_and(image, image, mask=mask)

numpydata = asarray(mask)

brown = np.count_nonzero(numpydata != 0)

percentage = brown / numpydata.size * 100

print(percentage, '%')

cv2.imshow('Segmented Image', segmented_img)

cv2.imshow('Original Image', image)

# cv2.imshow('Grayscale', gray)

# cv2.imshow('Blur', blur)

# cv2.imshow('Canny edge', canny)

cv2.imshow('Mask', mask)

# cv2.imshow('HSV', hsv)

cv2.waitKey(0)

cv2.destroyAllWindows()