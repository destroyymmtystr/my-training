import cv2

img = cv2.imread('images/00000.png')
img = cv2.resize(img, (320 ,240))
cv2.imwrite('resized.png', img)