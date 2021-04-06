import os
import sys
from PIL import Image, ImageFilter

source_folder = sys.argv[1]
destination_folder = sys.argv[2]


# Find all photos inside source directory
img_list = []
for img in os.listdir(source_folder):
    if img.endswith(".jpg"):
        img_list.append(os.path.join(source_folder, img))

if os.path.exists(destination_folder):
    pass
else:
    os.mkdir(destination_folder)

for i in img_list:
    original = Image.open(i)
    filename, file_extension = os.path.splitext(os.path.basename(i))
    filename += '.png'
    new_name = os.path.join(destination_folder, filename)
    original.save(os.path.join(new_name))
