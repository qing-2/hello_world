"""
按道理应该是这样吧，r==g==b的是灰度图
"""
from PIL import Image

img = Image.open("E:\\图片\\手指静脉.jpg")
flag = True
for x in range(img.width):
    for y in range(img.height):
        pix = img.getpixel((x, y))
        if not pix[0]==pix[1]==pix[2] :
            flag = False
            break
    if flag == False:
        break
print(flag)

