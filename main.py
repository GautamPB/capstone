import cv2
import numpy as np

image = cv2.imread('./Assets/Panel 1.jpg')

image = cv2.resize(image, (500, 500), interpolation = cv2.INTER_AREA)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

blur = cv2.GaussianBlur(gray, (171,171), cv2.BORDER_DEFAULT)

canny = cv2.Canny(hsv, 500, 500)

ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cv2.imshow('Binary image', thresh)

# lb = np.array([255, 228, 196])
# hb = np.array([165, 42, 42])

# mask = cv2.inRange(hsv, lb, hb)

cv2.imshow('Original Image', image)

# cv2.imshow('Grayscale', gray)

# cv2.imshow('Blur', blur)

# cv2.imshow('Canny edge', canny)

# cv2.imshow('Mask', mask)

cv2.imshow('HSV', hsv)

cv2.waitKey(0)

cv2.destroyAllWindows()