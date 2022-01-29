import cv2

img = cv2.imread('C:/Users/Pixel/Documents/python/FuzzyMath_7sem/lab4/input/3.png')
blur = cv2.GaussianBlur(img, (11, 11), 1)
while True:
    cv2.imshow('nikita', img)
    cv2.imshow('nikita_blur', blur)
    if cv2.waitKey(10) == 27:
            break