import cv2
from ultralytics import YOLO

# Load YOLOv8 Pose model
model = YOLO("yolov8n-pose.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Perform pose estimation
    results = model(frame, conf=0.5)

    # Draw pose keypoints and skeleton
    annotated_frame = results[0].plot()

    # Display output
    cv2.imshow("YOLOv8 Pose Estimation", annotated_frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()