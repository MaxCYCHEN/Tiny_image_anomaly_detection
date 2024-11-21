import numpy as np
import cv2

img_bg = cv2.imread(r'pictures_sample\WIN_20241017_13_48_07_Pro_empty.jpg')
img_now = cv2.imread(r'pictures_sample\WIN_20241017_13_47_40_Pro.jpg')
print(img_now.shape)
img_bg = cv2.cvtColor(img_bg, cv2.COLOR_BGR2GRAY)
img_now = cv2.cvtColor(img_now, cv2.COLOR_BGR2GRAY)
print(img_now.shape)


resImg = cv2.absdiff(img_bg, img_now)

(T, resImg) = cv2.threshold(resImg, 30, 255, cv2.THRESH_BINARY)

resImg = cv2.dilate(resImg, None, iterations=36)
resImg = cv2.erode(resImg, None, iterations=36)
resImg = cv2.dilate(resImg, None, iterations=12)










cv2.imshow("resImg ", resImg)
cv2.waitKey(0)