import os
import yaml

# Define the main datasets directory
DATASETS_DIR = r"C:\Users\rapha\OneDrive\Desktop\CS 3201\Thesis\datasets"

# List of expected dataset names
DATASET_NAMES = ["Acne", "Eczema", "Melasma", "Monkeypox", "Psoriasis", "Rosacea"]

# Expected subdirectories in each dataset
EXPECTED_SUBDIRS = ["train", "valid", "test"]
EXPECTED_CONTENTS = ["images", "labels"]

def check_dataset_structure():
    errors = []

    for dataset in DATASET_NAMES:
        dataset_path = os.path.join(DATASETS_DIR, dataset)
        
        # Check if dataset folder exists
        if not os.path.exists(dataset_path):
            errors.append(f"❌ Missing dataset folder: {dataset_path}")
            continue
        
        # Check if each dataset has train, valid, test folders
        for subdir in EXPECTED_SUBDIRS:
            subdir_path = os.path.join(dataset_path, subdir)
            if not os.path.exists(subdir_path):
                errors.append(f"❌ Missing folder: {subdir_path}")
                continue

            # Check if 'images' and 'labels' exist inside each subdir
            for content in EXPECTED_CONTENTS:
                content_path = os.path.join(subdir_path, content)
                if not os.path.exists(content_path):
                    errors.append(f"❌ Missing {content} folder in {subdir_path}")

        # Check if data.yaml exists
        yaml_path = os.path.join(dataset_path, "data.yaml")
        if not os.path.exists(yaml_path):
            errors.append(f"❌ Missing data.yaml: {yaml_path}")
        else:
            # Validate paths inside data.yaml
            with open(yaml_path, "r") as f:
                data = yaml.safe_load(f)

            for key in ["train", "val", "test"]:
                if key in data:
                    abs_path = os.path.join(dataset_path, data[key].replace("..", "").strip("/"))
                    if not os.path.exists(abs_path):
                        errors.append(f"❌ Incorrect path in {yaml_path}: {key} -> {data[key]} does not exist.")

    # Print results
    if errors:
        print("\n".join(errors))
    else:
        print("✅ All dataset directories and files are correctly structured.")

# Run the check
check_dataset_structure()
