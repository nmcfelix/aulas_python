import os
import sys
from PIL import Image, ImageFilter

source_folder = sys.argv[1]
destination_folder = sys.argv[2]


# Find all photos inside source directory
img_list = []
print(os.getcwd())
for img in os.listdir(source_folder):
    if img.endswith(".jpg"):
        img_list.append(os.path.join(source_folder, img))

if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

for i in img_list:
    original = Image.open(i)
    filename = os.path.splitext(os.path.basename(i))[0]
    print(filename)
    #new_name = os.path.join(destination_folder, filename)
    # original.save(os.path.join(new_name))
