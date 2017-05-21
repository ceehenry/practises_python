# edit image

from PIL import Image

from PIL import ImageDraw

from PIL import ImageFont


img = Image.open("p1_icon.jpg")
font = ImageFont.truetype(font="file:///Library/Fonts/AppleMyungjo.ttf", size=30)
draw = ImageDraw.Draw(img)
draw.text((120, 10), u'5', fill=(255, 0, 0), font=font)
draw = ImageDraw.Draw(img)
img.show()
