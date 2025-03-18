import os

def count_files(folder):
    return len([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])

test_img_count = count_files("datasets/Psoriasis/test/images")
test_lbl_count = count_files("datasets/Psoriasis/test/labels")

valid_img_count = count_files("datasets/Psoriasis/valid/images")
valid_lbl_count = count_files("datasets/Psoriasis/valid/labels")

print(f"Valid Images: {valid_img_count}, Valid Labels: {valid_lbl_count}")
print(f"Expected Test Count (15%): {int(valid_img_count * 0.15)}")


print(f"Test Images: {test_img_count}, Test Labels: {test_lbl_count}")
