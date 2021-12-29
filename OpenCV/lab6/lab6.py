import cv2
 
cap = cv2.VideoCapture('C:/Users/Pixel/Desktop/lab6/1.mp4')
tracker = cv2.TrackerCSRT_create()
ret, frame = cap.read()
roi = cv2.selectROI(frame)

# Crop selected roi from raw image
roi_cropped = frame[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
# Show cropped image
cv2.imshow("ROI", roi_cropped)
# Сохраняю roi
cv2.imwrite("C:/Users/Pixel/Desktop/lab6/crop.jpeg", roi_cropped)

# Initialize tracker with first frame and roi
ok = tracker.init(frame, roi)

# Read until video is completed
while(cap.isOpened()):
    ret, frame = cap.read()
    # Update tracker
    ok, roi = tracker.update(frame)

    # Draw bounding box
    if ok:
        # Tracking success
        p1 = (int(roi[0]), int(roi[1]))
        p2 = (int(roi[0] + roi[2]), int(roi[1] + roi[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else :
        # Tracking failure
        cv2.putText(frame, "Tracking failure", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
    

    cv2.imshow('Frame',frame)
    key = cv2.waitKey(20)
    if (key == 27): 
	    break 

cap.release()
cv2.destroyAllWindows()
