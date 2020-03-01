# http://125.35.6.84:81/xk/ 主页
# http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList  主页的XHRpost请求
# http://125.35.6.84:81/xk/itownet/portal/dzpz.jsp?id=f573b058a0774799aaa5821db5e16397 次页
# http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById 
# http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById post 次页的XHRpost请求url一样
# 观察网页！！
import requests
import json
def get():
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    id_list = []
    for page in range(1,5):
        params = {
            'on': True,
            'page': page,
            'pageSize': 15,
            'conditionType': 1,
            'productName':'',
            'applyname':'',
            'applysn':'',
        }
    
        # 首页，获取所有厂家的ID
        response = requests.post(url,params,headers)
        dict_obj = response.json()
        for x in dict_obj['list']:
            id_list.append(x['ID'])

    # 根据ID获取信息
    second_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        second_params = {
            'id':id
        }
        second_response = requests.post(second_url,second_params,headers)
        print(second_response.json())
if __name__ == "__main__":
    get()
        