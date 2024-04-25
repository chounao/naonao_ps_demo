from urllib.parse import urlparse
import yaml
from mitmproxy import http,ctx
#京东
# jd_url=['activity.fhd001.com','commonapi.fhd001.com','aiapi.fhd001.com','jdapione.fhd001.com']
#1688
# albb_url = ['commonapi.fhd001.com','common.fhd001.com','www.fhd001.com','activity.fhd001.com','ai.fhd001.com','albb.xyy001.com','albbapi.fhd001.com','download.xyy001.com']
#千牛
# qnfhd_url =['fhd001.com','xyy001.com']
s_url = ['fhd001','xyy001']
list_l = []
new_l = []
path = "C:/Users/86185/Desktop/mimt/save_url.txt"
def request(flow: http.HTTPFlow):

    # 判断抓包的请求是否在自己需要的列表内
    # for i in url:
    #     if i in flow.request.url:
    #         print(i,"----------------------------")
    #         url_all = flow.request.url
    #         list_l.append(url_all)
    #     # 去重

    url = flow.request.url#当前抓包url
    get_url = split_url(url)#抓包后截取掉https://xxxx.（get_url）.xxxxxxx

    if get_url in s_url:#判断截取掉的内容是否在写死的list内
        url_all = url
        list_l.append(url_all)#存找到的完整的url
    for n in list_l:#去重
        if n not in new_l:#判断去重
            new_l.append(n)
    #存储操作
    save_data(new_l)
def split_url(url):
    #截取url
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split('.')[-2]
    # print(domain)
    return domain
def save_data(data):
    # 存到文件
    with open(path, "w", encoding='utf-8') as f:
        yaml.dump(data, f)
        print(data)


#mitmdump -p 8080 -s  C:/Users/86185/Desktop/mimt/save_url.py