import cv2.videoio_registry
from ultralytics import YOLO
import cv2


model = YOLO('face_recog.pt')


results = model.track(source=0,show=True,)

for i in results:
    print(i.boxes.id)