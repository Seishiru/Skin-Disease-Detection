import os

dataset_path = "Melasma (Mix)"

# List subfolders
subfolders = ["imagesTest", "imagesTrain", "imagesValid"]

for subfolder in subfolders:
    folder_path = os.path.join(dataset_path, subfolder)
    
    if os.path.exists(folder_path):
        images = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
        
        print(f"📂 {subfolder}: {len(images)} images found")
        
        if images:
            print("🔍 First 5 images:", images[:5])  # Show first 5 images
    else:
        print(f"❌ {subfolder} folder not found!")
