import os
import random
import shutil

# Define base dataset path
dataset_base = "datasets/Psoriasis"  # Adjust if needed

# Define source (valid) and destination (test) paths
valid_images_path = os.path.join(dataset_base, "valid/images")
valid_labels_path = os.path.join(dataset_base, "valid/labels")
test_images_path = os.path.join(dataset_base, "test/images")
test_labels_path = os.path.join(dataset_base, "test/labels")

# Ensure test folders exist
os.makedirs(test_images_path, exist_ok=True)
os.makedirs(test_labels_path, exist_ok=True)

# Get all image files in valid/images
image_files = [f for f in os.listdir(valid_images_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Determine how many files to move (15%)
num_to_move = max(1, int(len(image_files) * 0.15))
files_to_move = random.sample(image_files, num_to_move)

# Move images and labels
for img_file in files_to_move:
    img_src = os.path.join(valid_images_path, img_file)
    img_dest = os.path.join(test_images_path, img_file)

    label_file = os.path.splitext(img_file)[0] + ".txt"  # Convert image filename to .txt for label
    label_src = os.path.join(valid_labels_path, label_file)
    label_dest = os.path.join(test_labels_path, label_file)

    # Move image
    shutil.move(img_src, img_dest)
    
    # Move label (if it exists)
    if os.path.exists(label_src):
        shutil.move(label_src, label_dest)

print(f"Moved {num_to_move} images and their labels from 'valid/' to 'test/'.")
