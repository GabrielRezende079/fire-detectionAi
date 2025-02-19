from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Modelo pré-treinado
model.train(data="fire.yaml", epochs=10, imgsz=640, batch=8)
