import cv2
import os
import random
import matplotlib.pyplot as plt

valid_path = "Melasma (Mix)/imagesValid"

# List all image files
image_files = [f for f in os.listdir(valid_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Select a random image
random_image = random.choice(image_files)
image_path = os.path.join(valid_path, random_image)

# Read and display the image
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image)
plt.axis("off")
plt.title(f"Sample: {random_image}")
plt.show()
