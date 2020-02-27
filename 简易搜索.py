"""
UA伪装：设置User-Agent，假装是个浏览器在发请求。
文件名不能有空格和一些符号
"""

import requests

def get():
    base_url = "https://www.sogou.com/web"
    kw = input("Enter a keyword :")
    params = {
        "query":kw
    }
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    response = requests.get(base_url,params = params,headers=headers)

    page_text = response.text
    f = open("./sogou_" + kw +".html",'w',encoding = 'utf-8')
    f.write(page_text)

if __name__ == "__main__":
    get()