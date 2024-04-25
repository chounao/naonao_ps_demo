import yaml
from mitmproxy import http
import json
import urllib.parse

"""
针对http，常用的API
http.HTTPFlow 实例 flow
flow.request.headers #获取所有头信息，包含Host、User-Agent、Content-type等字段
flow.request.url #完整的请求地址，包含域名及请求参数，但是不包含放在body里面的请求参数
flow.request.pretty_url #同flow.request.url目前没看出什么差别
flow.request.host #域名
flow.request.method #请求方式。POST、GET等
flow.request.scheme #什么请求 ，如https
flow.request.path # 请求的路径，url除域名之外的内容
flow.request.get_text() #请求中body内容，有一些http会把请求参数放在body里面，那么可通过此方法获取，返回字典类型
flow.request.query #返回MultiDictView类型的数据，url直接带的键值参数
flow.request.get_content()#bytes,结果如flow.request.get_text()
flow.request.raw_content #bytes,结果如flow.request.get_content()
flow.request.urlencoded_form #MultiDictView，content-type：application/x-www-form-urlencoded时的请求参数，不包含url直接带的键值参数
flow.request.multipart_form #MultiDictView，content-type：multipart/form-data
时的请求参数，不包含url直接带的键值参数


以上均为获取request信息的一些常用方法，对于response，同理
flow.response.status_code #状态码
flow.response.text#返回内容，已解码
flow.response.content #返回内容，二进制
flow.response.setText()#修改返回内容，不需要转码

"""



"""
 mitmdump -p 8080 -s  C:/Users/86185/Desktop/mimt/demo.py
 mitmdump -p 端口 -s 文件执行路径
"""
list_l = []
new_l = []
def response(flow: http.HTTPFlow):
    re = flow.response
    text = re.text
    print("------------------------------------------------------------")
    # print(text)
def request(flow:http.HTTPFlow):
    urlpath = [
        '/print/queryShippingAddress.do',
        "/template/getExpressTemplates.do",
        "/template/getCommonExpressTemplates.do",
        "/printCore/getWaybillAccounts.do"
    ]
    re = flow.request

    # print(re)
    if re.path in urlpath:
        # print(re.get_text())
        # print(re.url)
        print(re.headers)
    # if "https://jd.fhd001.com/" in flow.request.url:
        params = urllib.parse.parse_qs(re.get_text())
        params_dict = {key: list(value)[0] for key, value in params.items()}
        data = {re.path: {"method": re.method, "body": params_dict}}
        #print("post请求内容",data)
        list_l.append(data)


    #去重
    for i in list_l:
        if i not in new_l:
            new_l.append(i)
    save_data(new_l)

def save_data(data):
    #存到文件
    with open("C:/Users/86185/Desktop/mimt/1688_case.yaml", "w", encoding='utf-8') as f:
        yaml.dump(data, f)
        print("SAVE YAML")
        # print(data)
    with open("C:/Users/86185/Desktop/mimt/1688_case.json", "w", encoding='utf-8') as f:
        json.dump(data, f,indent=4)
        print("SAVE JSON")

    def __init__(self,filter_url: str):
        self.url = filter_url
        self.NotFound_lits = []
        self.Error_list = []
        self.headers_list =["referer","origin"]
        self.host = "host"



a =((b'content-length', b'166'), (b'pragma', b'no-cache'), (b'cache-control', b'no-cache'), (b'sec-ch-ua', b'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"'), (b'sec-ch-ua-platform', b'"Windows"'), (b'sec-ch-ua-mobile'
, b'?0'), (b'user-agent', b'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'), (b'content-type', b'application/x-www-form-urlencoded'), (b'accept', b'*/*'), (b'origin',
 b'https://albbstatic.xyy001.com'), (b'sec-fetch-site', b'cross-site'), (b'sec-fetch-mode', b'cors'), (b'sec-fetch-dest', b'empty'), (b'referer', b'https://albbstatic.xyy001.com/'), (b'accept-encoding', b'gzip, deflate, br'), (b'accept-language', b'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'))

data_dict={}

for i in (list(a)):

    h = str(i).split("b'")[1].split("',")[0]
    data_dict[h] = str(i).split(h+"', b'")[1].split("')")[0]
print(list(a))
dictionary = {key.decode(): value.decode() for key, value in list(a)}
print(dictionary)
#
# data = {"name": "John", "age": 30, "city": "New York"}
# with open("C:/Users/86185/Desktop/mimt/1688_case.json", "w", encoding='utf-8') as f:
#     json.dump(data, f, indent=4)
#     print("SAVE JSON")

# a = '/fhd/thirdplatform/queryOrder.do'
# c = a.split('/')[-1][:-3]
#
# print(c)


