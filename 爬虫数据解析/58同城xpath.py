import requests
from lxml import etree

if __name__ == "__main__":

    url = 'https://bj.58.com/ershoufang/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    page_text = requests.get(url, headers).text
    
    # 实例化etree对象，并且将被解析的源码加载到对象中

    # 保存到本地再解析容易出问题，格式不规范等等
    # f = open('./58.html','w',encoding='utf-8')
    # f.write(page_text)
    # tree = etree.parse('./58.html')

    # 不写入本地
    tree = etree.HTML(page_text)

    # 调用xpath方法，参数要用xpath表达式
    # /表示从根节点开始定位，//表示任意定位，即取出所有
    # 属性定位，索引定位
    # text()取文本,返回的是个列表
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')

    f = open('./58title.txt', 'w', encoding='utf-8')
    
    for li in li_list:
        # /表示整个文档的根标签，./表示当前标签下.局部解析
        title = li.xpath('./div[2]/h2/a/text()')[0]
        f.write(title+'\n')