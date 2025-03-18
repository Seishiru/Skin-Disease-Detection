from ultralytics import YOLO

# Load the trained model
model = YOLO("runs/detect/train5/weights/best.pt")  

# Run prediction on a new image
results = model("path/to/your/image.jpg", save=True, conf=0.3)  # Adjust confidence threshold
