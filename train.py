from ultralytics import YOLO

# Load a YOLOv8 model (you can use yolov8n, yolov8s, yolov8m, yolov8l, yolov8x)
model = YOLO("yolov8n.pt")  # Using YOLOv8 nano model for training

# Train the model
results = model.train(
    data="datasets/Acne/data.yaml",  # Path to your dataset config
    epochs=50,  # Number of epochs
    batch=16,   # Batch size (adjust based on your GPU)
    imgsz=640,  # Image size for training
    device="cpu"  # Use GPU if available
)
