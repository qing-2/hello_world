"""
有些网页极慢，有些html有报错？
明明都是utf-8编码呀，还是有乱码，可能是因为百度？
生成的html拖到浏览器打开，图片显示不出来？？但是应该可以保存
"""

import requests

def get():
    base_url = "https://www.icourse163.org/?from=study"#目标网址
    response = requests.get(base_url)#获取响应
    page_text = response.text#获取字符串形式的html
    f = open("./mooc.html",'w',encoding = 'utf-8')#创建HTML文件
    f.write(page_text)#保存到本地

if __name__ == "__main__":
    get()
