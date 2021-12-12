"""
Определить цвета центрального пикселя 
с помощью HSV представления 
и нарисовать крест указанного цвета

если объект зелёный, то показывать полностью зелёный
если синий, то только синий
для этого нужно указать диапазон в hsv

"""

import cv2
import numpy as np

# Определяю диапазон HSV цветов
lower_blue = np.array([110,50,50])      
upper_blue = np.array([130,255,255])

lower_green = np.array([53, 55, 147])    
upper_green = np.array([83, 160, 255])

lower_red = np.array([155,25,0])    
upper_red = np.array([179,255,255])

# Объект захвата
input_cam = cv2.VideoCapture(0)

while input_cam.isOpened():         # Пока объект захвата открыт
    ret, frame1 = input_cam.read()
    height, width, channels = frame1.shape

    # Convert BGR to HSV
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    
    # Threshold the HSV image to get only blue, red or green colors
    mask_blue = cv2.inRange(frame1, lower_blue, upper_blue)
    mask_green = cv2.inRange(frame1, lower_green, upper_green)
    mask_red = cv2.inRange(frame1, lower_red, upper_red)

    center_blue = mask_blue[240, 320] # [255] or [0]
    center_green = mask_green[240, 320]
    center_red = mask_red[240, 320]

    #обратно в бгр 
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_HSV2BGR)

    # Цветной прямоугольник
    upper_left = (300, 220)
    bottom_right = (340, 260)
    center = frame1[240, 320] # Центральный пиксел фрейма height, width
    b = center[0]      # Цвета центрального пиксела фрейма 
    g = center[1]
    r = center[2]
    rect_img = frame1[upper_left[1]: bottom_right[1] + 1, upper_left[0]: bottom_right[0] + 1]
    rect_img[:] = (b, g, r)  # modify value

    # Проверка попадания цвета
    white = 255
    if center_blue == white:
        rect_img[:] = (255, 0, 0)  
    elif center_green == white:
        rect_img[:] = (0, 255, 0)  
    elif center_red == white:
        rect_img[:] = (0, 0, 255)  
    

    print ('Center color: ' + str(center))
    
    cv2.imshow('Cam', frame1)
    cv2.imshow('blue', mask_blue)
    cv2.imshow('green', mask_green)
    cv2.imshow('red', mask_red)
    if cv2.waitKey(10) == 27:
        break

input_cam.release()
cv2.destroyAllWindows()

print(center)