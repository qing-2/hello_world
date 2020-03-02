"""想爬取'https://huaban.com/explore/bohelvsexi/'的图片
主页的respnse 有很多app.page?页面确实挺像手机app的，preview没有图片
xjax请求图片
这里的k.html是硬生生复制过来的，不是请求的。。。
最终爬取了20张图片
"""
import requests
from bs4 import BeautifulSoup
import os

def get():
    if not os.path.exists('./薄荷'):
        os.mkdir('./薄荷')
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    f = open('./k.html','r',encoding='utf-8')
    soup = BeautifulSoup(f,'lxml')

    img_list = soup.select('.layer-view > img')
    index = 0
    for img in img_list:
        src = 'https:'+img['src']
        img_data = requests.get(src,headers).content
        f = open('./薄荷./'+str(index)+'.jpg','wb')
        f.write(img_data)
        print('over')

if __name__ == "__main__":
    get()
