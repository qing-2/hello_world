"""往下翻网页的时候，会逐步加载。查看XHS，headers
"""
import requests
import json

def get():
    url = "https://movie.douban.com/j/chart/top_list"
    limit = input("查看剧情分类里前多少名的电影：")
    params = {
        "type": '11',
        "interval_id": '100:90',
        "action": '80',
        "start": '0',
        "limit": limit
    }
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    response = requests.get(url,params,headers=headers)

    # 在网页开发者工具里的Preview看到的是list数据
    list_data = response.json()

    # 写入json文件中
    f = open("./douban"+limit+".json",'w',encoding='utf-8')
    json.dump(list_data,f,ensure_ascii=False)

    # 打印出电影名，从json中看出每个电影是一个字典
    for x in list_data:
        print(x["title"])
    print("\n")
    
    # 打印出电影的全部信息
    # value是list,所以value不能像key一样连接字符串
    for x in list_data:
        for key,value in x.items():
            print('{key}:  {value}'.format(key = key + ' ', value = value ))
        print("\n")

if __name__ == "__main__":
    get()