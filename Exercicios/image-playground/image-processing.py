from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
image_blur = img.convert("L")
image_blur.save('blur.png', 'png')
