from ultralytics import YOLO

model = YOLO("yolo11n.pt")

model.train(data="/media/prethiviraj/R'kived Lab/Projects/2025/Computer vision/Prethivi-Hand.v1i.yolov11/data.yaml",epochs=60,imgsz=640)

model.save("/media/prethiviraj/R'kived Lab/Projects/2025/Computer vision/face_recog.pt")
