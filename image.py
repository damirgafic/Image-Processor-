from PIL import Image, ImageFilter

img = Image.open('./Pokedex/original.jpg')
filtered_img = img.filter(ImageFilter.BoxBlur(30))
filtered_img.save("blur.png",'png')