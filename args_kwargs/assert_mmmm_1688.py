import json
import time
#3762277419940498520, 3719556936381498520,3770093702102498520, 3768896341535498520, 3766046043667498520, 3765718153221498520, 3748081394003498520, 3735279864361498520
import requests
shopid1 = 1623492085
shopid2 = 1624961198
shopids = str(shopid1)+','+str(shopid2)
platform = ['kuaishou','douyin','1688','xiaohongshu','thyny','pinduoduo']
for p in platform:
    ml = []  # 密文
    l = []  # 非密文
    a = []  # 过滤剩下
    # 发送请求
    h = {'Content-Type':'application/x-www-form-urlencoded'}
    body = {
    'shopIds': shopids,
    'status': 1,
    'sort': 'payTime',
    'desc': 'true',
    'channel':p,
    'startConfirmTime': 1706716800,
    'endConfirmTime': 1711814400,
    'page': 1,
    'pageSize': 200,
    'referer': 'albbportal',
    'token': '%7EXVEABQlfBgEITQBcXxdUQxJSVhYNEkcHUU1WDVoQBEsRB11AWRVBAANNUBwHVAAAVwYIVVBWBgE%3D%7E1%7E'}
    response = requests.post('https://albbapi.fhd001.com/albb/multiShopQueryAlbbOrder.do',body,h)
    # 检查请求是否成功
    if response.status_code == 200:
        # 解析响应数据
        data = response.json()
        # print(data)
        for i in data['data']['list']:
            # print(i)
            if i['refundStatus'] == "":
                order = i['info']['orderSn']
                orderinfo = i['info']['orderInfo']
                if '"fromEncryptOrder":true' in orderinfo:
                    ml.append(order)
                elif '"fromEncryptOrder":fals' in orderinfo:
                    l.append(order)
                else:
                    a.append(order)
        print("============================================",p,"============================================")
        print("密文",len(ml),ml)
        print("非密文",len(l),l)
        print("剩余订单",len(a),a)

