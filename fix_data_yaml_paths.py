import os
import yaml

# Define dataset directories
dataset_dirs = [
    "Acne", "Eczema", "Melasma", "Monkeypox", "Psoriasis", "Rosacea"
]

# Base path to your datasets folder
base_path = r"C:\Users\rapha\OneDrive\Desktop\CS 3201\Thesis\datasets"

def update_yaml_file(yaml_path):
    """ Updates the paths inside a data.yaml file. """
    with open(yaml_path, "r") as file:
        data = yaml.safe_load(file)

    # Update paths to absolute paths
    data["train"] = os.path.join(base_path, os.path.basename(os.path.dirname(yaml_path)), "train", "images").replace("\\", "/")
    data["val"] = os.path.join(base_path, os.path.basename(os.path.dirname(yaml_path)), "valid", "images").replace("\\", "/")
    data["test"] = os.path.join(base_path, os.path.basename(os.path.dirname(yaml_path)), "test", "images").replace("\\", "/")

    # Save back to file
    with open(yaml_path, "w") as file:
        yaml.dump(data, file, default_flow_style=False)

    print(f"✅ Updated: {yaml_path}")

# Iterate over each dataset directory
for dataset in dataset_dirs:
    yaml_path = os.path.join(base_path, dataset, "data.yaml")
    if os.path.exists(yaml_path):
        update_yaml_file(yaml_path)
    else:
        print(f"⚠️ Missing: {yaml_path}")

print("🎯 All YAML files processed.")
