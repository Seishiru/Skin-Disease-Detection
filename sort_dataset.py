import cv2
import os
import shutil

# Define dataset paths
melasma_mix_path = "Melasma (Mix)"  # Change this to the actual path
acne_path = "Acne Vulgaris/imagesTrain"
eczema_path = "Eczema/imagesTrain"
melasma_path = "Melasma/imagesTrain"

# Ensure the destination folders exist
os.makedirs(acne_path, exist_ok=True)
os.makedirs(eczema_path, exist_ok=True)
os.makedirs(melasma_path, exist_ok=True)

# Get list of images
image_files = [f for f in os.listdir(melasma_mix_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

for image_file in image_files:
    image_path = os.path.join(melasma_mix_path, image_file)
    
    # Load and show the image
    image = cv2.imread(image_path)
    cv2.imshow("Sort Image: Press (A) Acne, (E) Eczema, (M) Melasma, (X) Skip", image)
    
    # Wait for key input
    key = cv2.waitKey(0) & 0xFF  # Wait indefinitely for key press

    # Move file based on key press
    if key == ord('a'):  # Move to Acne
        shutil.move(image_path, os.path.join(acne_path, image_file))
        print(f"Moved {image_file} to Acne folder.")
    elif key == ord('e'):  # Move to Eczema
        shutil.move(image_path, os.path.join(eczema_path, image_file))
        print(f"Moved {image_file} to Eczema folder.")
    elif key == ord('m'):  # Move to Melasma
        shutil.move(image_path, os.path.join(melasma_path, image_file))
        print(f"Moved {image_file} to Melasma folder.")
    elif key == ord('x'):  # Skip image
        print(f"Skipped {image_file}")

    cv2.destroyAllWindows()  # Close the image window

print("✅ Dataset sorting completed!")
