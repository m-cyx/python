"""
Реализовать приложение на Python, позволяющее определить
красный объект в центре изображения и отслеживать после этого его
перемещения на видео.
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_red = np.array([155,25,0])    # Красный
upper_red = np.array([179,255,255])

while True:
    flag, frame = cap.read() # Читаем фрейм 
    frame = cv2.flip(frame, 1) # отражение кадра вдоль оси Y
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )
    #blur = cv2.GaussianBlur(hsv, (7, 7), 0) # Нифигово так размываем
    thresh = cv2.inRange(hsv, lower_red, upper_red)

    moments = cv2.moments(thresh, 1) # Берём моменты. Вес точки = 1, если цвет не 0
    dM10 = moments['m10'] # Сумма Х координат точек 
    dM01 = moments['m01'] # Сумма У координат точек
    dArea = moments['m00']# Это кол-во всех точек, составляющих пятно.

    if dArea > 100: # Если пятно больше 100, то рисую кружок в центре пятна.
        # Средние координаты всех точек, т.е центр пятна.
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)

        # Рисую кружок
        cv2.circle(frame, (x, y), 10, (255,0,0), -1)

    cv2.imshow('result', frame)
    cv2.imshow('th', thresh)

    ch = cv2.waitKey(5)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()