"""
Реализовать приложение на Python, позволяющее определить
красный объект в центре изображения и отслеживать после этого его
перемещения на видео.
"""
# Момент - это сумма всех писклей пятна. Моменты могут быть разными
import cv2
import numpy as np
# https://robotclass.ru/tutorials/opencv-moments-color-object-search/


# Разобратсья с этой фукцией, судя по всему нужна для наложения линии
#def createPath( frame ):
#    h, w = frame.shape[:2] 
#    return np.zeros((h, w, 3), np.uint8)


cap = cv2.VideoCapture(0)

lower_red = np.array([155,25,0])    # Красный
upper_red = np.array([179,255,255])

lastx = 0
lasty = 0
#path_color = (0,0,255)

flag, frame = cap.read()
#path = createPath(frame)

while True:
    flag, frame = cap.read() # Читаем фрейм 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, lower_red, upper_red)

    moments = cv2.moments(thresh, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    if dArea > 100:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(frame, (x, y), 10, (255,0,0), -1)

    #if lastx > 0 and lasty > 0:
    #    cv2.line(path, (lastx, lasty), (x,y), path_color, 5)
    #lastx = x
    #lasty = y

    # накладываем линию траектории поверх изображения
    #frame = cv2.add( frame, path)

    cv2.imshow('result', frame)
    cv2.imshow('th', thresh)

    ch = cv2.waitKey(5)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()