from PIL import Image, ImageDraw, ImageFont
import os
import time

def save(img, file_name):
    if os.path.isfile(file_name + '.png'):
        save(img, file_name + '-')
    else:
        img.save(file_name + '.png')

def main():
    lena = Image.open("E:\\图片\\猪lena_L.jpg")
    #绝对路径，我觉得通过其他方式应该可以用相对路径吧
    lena_L =lena.convert("L")
    # lena_L =lena.convert("1")另一种模式，纯黑或白像素点
    save(lena_L,"file_name")
    
if __name__ == "__main__":
    main()
