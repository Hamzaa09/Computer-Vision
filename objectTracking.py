import cv2, time

cap = cv2.VideoCapture(0)

def initializeTracker():
    tracker = cv2.legacy.TrackerCSRT_create()
    success, img = cap.read()
    img = cv2.flip(img, 1)
    bbox = cv2.selectROI("Tracking", img, False)
    tracker.init(img, bbox)
    return tracker

def drawBBOX(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.putText(img, "Detecting", (10, 80), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 2)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)


tracker = initializeTracker()
prev_t = 0
record = None

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    
    success, bbox = tracker.update(img)
    
    # fps
    curr_t = time.time()
    fps = 1/(curr_t - prev_t)
    prev_t = curr_t
    
    if success:
        drawBBOX(img, bbox)
    else:
        cv2.putText(img, "Lost Detection", (10, 80), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
    
    cv2.putText(img, f"FPS: {int(fps)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.putText(img, "Press 'r' to Reset, 'q' to Quit", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        
    cv2.imshow("Tracking", img)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    if key == ord('r'):
        tracker = initializeTracker()
    
cap.release()
cv2.destroyAllWindows()