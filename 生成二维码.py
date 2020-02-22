"""
不好看，应该还有其他方法吧
"""
from MyQR import myqr
myqr.run(
    words='https://github.com/qing-2',
    picture='E:\\图片\\谢谢.jpg',
    colorized=True,
    save_name='MyQRcode.png',
    save_dir="E:\\图片"
)