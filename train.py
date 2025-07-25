from ultralytics import YOLO

model = YOLO("yolov8m.pt")

model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640 
)