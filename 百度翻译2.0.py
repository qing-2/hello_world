"""
和教程里一样方法，只能找到 Request URL: https://fanyi.baidu.com/langdetect
因为百度翻译变了吗？
这个url不行，显示不出翻译内容
"""

import requests
import json

def get(kw):
    post_url = "https://fanyi.baidu.com/sug"
    data = {
        "kw":kw
    }
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    response = requests.post(post_url,data,headers=headers)

    #响应对象是json，json()方法可以返回字典
    dic_obj = response.json()

    return dic_obj

def save_json(dic_obj,kw):
    # 保存为json文件
    f = open("./" + kw +".json",'w',encoding = 'utf-8')
    json.dump(dic_obj,f,ensure_ascii = False)

def print_dict(dic_obj):
    # 打印字典,打印所有以此开头的单词
    for x in dic_obj["data"]:
        for key,value in x.items():
            print('{key}:  {value}'.format(key = key + ' ', value = value + ' ')+"\n")

def print_kw_only(dic_obj):
    # 打印字典,只打印唯一单词
    for key,value in dic_obj["data"][0].items():
            print('{key}:  {value}'.format(key = key + ' ', value = value + ' '))

def main():
    kw = input("Enter a keyword :")
    data = get(kw)
    if(data["data"] == []):
        print("Not found ! ")
        return 0
    print_kw_only(data)

if __name__ == "__main__":
    while(True):
        main()