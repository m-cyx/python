import cv2
import numpy as np

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    h = int(cap.get(3))
    w = int(cap.get(4))
    center = (int(h / 2), int(w / 2))
    lastX = -1
    lastY = -1
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.GaussianBlur(frame, (7, 7), 0)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        kernel = np.ones((5, 5), np.uint8)
        lower_red = np.array([[161, 155, 84]])
        upper_red = np.array([179, 255, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        red = cv2.bitwise_and(frame, frame, mask=mask)

        gray = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
        threshed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

        threshed = cv2.erode(threshed, kernel, iterations=1)
        threshed = cv2.dilate(threshed, kernel, iterations=1)

        threshed = cv2.dilate(threshed, kernel, iterations=1)
        threshed = cv2.erode(threshed, kernel, iterations=1)

        cnts, _ = cv2.findContours(threshed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            M = cv2.moments(c)
            # cX = int(M["m10"] / M["m00"])
            # cY = int(M["m01"] / M["m00"])
            #draw the contour and center of the shape on the image
            # cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
            # cv2.circle(frame, (cX, cY), 7, (255, 255, 255), -1)
            # cv2.putText(frame, "center", (cX - 20, cY - 20),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)]
            # принятие решений. метод анализа иерархии. Саати.
            area = int(M["m00"])
            if area > 1000:
                cX = int(M["m10"] / area)
                cY = int(M["m01"] / area)
                if lastX >= 0 and lastY >= 0 and cX >= 0 and cY >= 0:
                    cv2.line(frame, (cX, cY), (lastX, lastY), (0, 0, 255), 2)
                lastX = cX
                lastY = cY
        cv2.imshow('rgb', frame)
        cv2.imshow('threshed', threshed)

        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
