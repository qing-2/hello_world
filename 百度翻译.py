"""
和教程里一样方法，只能找到 Request URL: https://fanyi.baidu.com/langdetect
因为百度翻译变了吗？
这个url不行，显示不出翻译内容
"""
import requests
import json

def get():
    post_url = "https://fanyi.baidu.com/sug"
    kw = input("Enter a keyword :")
    data = {
        "kw":kw
    }
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    response = requests.post(post_url,data,headers=headers)
    #响应对象是json，json()方法可以返回字典
    dic_obj = response.json()
    
    f = open("./" + kw +".json",'w',encoding = 'utf-8')
    json.dump(dic_obj,f,ensure_ascii = False)

if __name__ == "__main__":
    get()