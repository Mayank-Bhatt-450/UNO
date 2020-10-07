from PIL import Image

import math
from PIL import  ImageDraw, ImageFont
x,y=(110,143)
img = Image.new( 'RGBA', (x,y), "black") # create a new black image
imgs = img.load() # create the pixel map
for i in range(x):
    for k in range(y):
        if (i+k)%2==0:
            imgs[i, k]=(255,255,255,0)
        else:
            imgs[i, k]=(255,255,255,255)



img.save("op.png")
