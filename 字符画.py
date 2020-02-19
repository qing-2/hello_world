"""
注意事项：图片要先处理好（裁剪等），因为生成的图片不好二次处理；处理图片需要一些时间，所以运行需要一小会儿
原理：先转成灰度图像，再根据灰度值填充字符
适合对象：大部分留白的图片
影响图片效果的参数：bg_color，f_color，font_map
(调色无止境。。。
"""
from PIL import Image, ImageDraw, ImageFont
import os
# import time #time()可以测量运行时间

def save(img, file_name):
    if os.path.isfile(file_name + '.png'):
        save(img, file_name + '-')
    else:
        img.save(file_name + '.png')
#保存图片

font_map = [' ', ' ', ' ','I', 'J', 'C', 'D', 'O', 'S', 'Q', 'G', 'F', 'E', '#', '&', '@']
#用这些字符组成图片。字符按下标变大。
img_name = "hua" #新图像的名字
f_size_multiple = 10 #图像与原图像相比的放大倍数。大能看清字符，但是体积也大
bg_color = (	255,255,255)#图片背景颜色
f_color = (219,112,147)#填充的字符颜色

def main():
    img = Image.open("E:\\图片\\hua (2).jpg").convert("L")
    level = img.getextrema()[-1] / (len(font_map) - 1)
    #所有像素点最大的rgb里的一个值/font_map最大下标。/不是整除，//是整除
    img = img.point(lambda i: int(i / level))
    #这句话还不懂。。。point没查到能理解的解释
    new_img = Image.new('RGB', (img.width * f_size_multiple, img.height * f_size_multiple),bg_color)
    #(mode, size, color)，这里color是背景色
    f = ImageFont.truetype('arial.ttf', f_size_multiple)
    #truetype放大不会有锯齿
    d = ImageDraw.Draw(new_img)
    #新建画布绘画对象

    for y in range(0, img.height):
        for x in range(0, img.width):
            p = img.getpixel((x, y))
            #rgb图像这一点的rgb值。灰度图值是一维的。因为R=G=B就是灰度图像
            d.text((x * f_size_multiple, y * f_size_multiple), font_map[len(font_map) - p - 1],f_color, font=f)
            #在新建的对象上坐标(x * f_size_multiple, y * f_size_multiple)处开始画出f_color色文本
    #遍历所有像素点

    save(new_img, img_name)
    # new_img.show()#显示图片
    
if __name__ == "__main__":
    main()