import cv2
import os
import random
import matplotlib.pyplot as plt

# Path to dataset (update this if needed)
dataset_path = "Acne Vulgaris/imagesTrain"

# List all image files in the directory
image_files = [f for f in os.listdir(dataset_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Select a random image
random_image = random.choice(image_files)
image_path = os.path.join(dataset_path, random_image)

# Read the image
image = cv2.imread(image_path)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize to 224x224 (standard size for deep learning models)
resized_image = cv2.resize(gray_image, (224, 224))

# Apply Gaussian blur (for noise reduction)
blurred_image = cv2.GaussianBlur(resized_image, (5, 5), 0)

# Display original and processed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(blurred_image, cmap="gray")
plt.title("Blurred")
plt.axis("off")

plt.show()
