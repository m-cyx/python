import cv2
import sys

# Set up tracker.
tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 
                 'MEDIANFLOW', 'CSRT']

# Ask user wich tracker need to be used
print("Trackers: \n 1) Boosting \n 2) MIL \n 3) KCF \n 4) TLD \n 5) MEDIANFLOW \n 6) CSRT")
tracker = int(input("Select tracker type: ")) - 1
tracker_type = tracker_types[tracker]

# тут некоторые методы перенесены в легаси. если не работает, то дописать легаси как в бустинге 
if tracker_type == 'BOOSTING': #10-15 fps
    tracker = cv2.legacy.TrackerBoosting_create()
if tracker_type == 'MIL': #8-10 fps
    tracker = cv2.TrackerMIL_create()
if tracker_type == 'KCF': #50-70 fps
    tracker = cv2.TrackerKCF_create()
if tracker_type == 'TLD': #10-15 fps, но хорошо восстанавливает
    tracker = cv2.legacy.TrackerTLD_create()
if tracker_type == 'MEDIANFLOW': #100-120 fps не очень хорошо ищет
    tracker = cv2.legacy.TrackerMedianFlow_create()
if tracker_type == "CSRT": #15 fps восстанавливает не очень
    tracker = cv2.TrackerCSRT_create()

# Read video
video = cv2.VideoCapture("inputs/3.mp4") # Чтобы включить камеру - 0


# Read first frame.
ok, frame = video.read()

# Параметры для записи
frame_width = int(video.get(3))
frame_height = int(video.get(4))
frame_size = (frame_width,frame_height)
fps = 30

# Объект записи видео
output = cv2.VideoWriter('outputs/CSRT3.avi', cv2.VideoWriter_fourcc('M','J','P','G'), fps, frame_size)


# Define an initial bounding box
bbox = (287, 23, 86, 320)

# Uncomment the line below to select a different bounding box
bbox = cv2.selectROI(frame, False)

# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)

while True:
    # Read a new frame
    ok, frame = video.read()
    if not ok:
        break
    
    # Start timer
    timer = cv2.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(frame)

    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

    # Draw bounding box
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else :
        # Tracking failure
        cv2.putText(frame, "Tracking failure", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
    
    # Display tracker type on frame
    cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
    
    # Display result
    cv2.imshow("Tracking", frame)

    # Записать результат
    output.write(frame)
    
    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break