from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
image_blur = img.filter(ImageFilter.BLUR)
image_blur.save('blur.png', 'png')
