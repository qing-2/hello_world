import requests
import json

def get():
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"
    op = input("Enter the restaurant name or address : ")
    params = {
        'cname': None,
        'pid': None,
        "keyword": op,
        "pageIndex": '1',
        "pageSize": '10'
    }
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    response = requests.post(url,params,headers=headers) 

    # print(type(response.text))
    list_data = response.text
    print(response.text)
    # 写入json文件中
    # f = open("./douban"+op+".json",'w',encoding='utf-8')
    # json.dump(list_data,f,ensure_ascii=False)
    # page_text = response.text
    # f = open("./kfc" + op +".html",'w',encoding = 'utf-8')
    # f.write(page_text)

if __name__ == "__main__":
    get()