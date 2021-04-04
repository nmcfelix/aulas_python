import os
import sys
from PIL import Image, ImageFilter

source_folder = sys.argv[1]
#destination_folder = sys.argv[2]

# Find all photos inside source directory
img_list = []
for img in os.listdir(source_folder):
    if img.endswith(".jpg"):
        img_list.append(os.path.join(source_folder, img))

print(img_list)
