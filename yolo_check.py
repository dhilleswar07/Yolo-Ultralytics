import ultralytics
ultralytics.checks()

from ultralytics import YOLO
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)