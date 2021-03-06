from PIL import Image
import os

img = 'c:/Users/Acer/OneDrive/Desktop/Files/AIU/imageProcessingProject/batch-image-processing/img'


for i in os.listdir(img):
    file = f"{img}\\{i}"
    im = Image.open(file)
    im = im.resize((1080, 1080), Image.ANTIALIAS)
    im = im.convert("L")
    
    width, height = im.size
    
    size = (100,100)
    logo = Image.open('img\\logo.png')
    logo.thumbnail(size)
    
    x = width - 100 - 10
    y = height - 100 - 15
    
    im.paste(logo, (x,y))
    im.save(file)