import requests
import datetime
def date(time):
    date_string = time
    date_format = '%Y/%m/%d %H:%M:%S'
    dt = datetime.datetime.strptime(date_string, date_format)
    timestamp = int(dt.timestamp())
    print(timestamp)
    return timestamp


url = 'http://qnjyapi.fhd001.com/ownFhdUtil/finance/orderBuy'
headers = {'Content-Type':'application/x-www-form-urlencoded'}
#抖店代发
# data = {'orderId': '6924912858952636010',
#         'platformStr': 'iop',
#         "platformKey":"23836114",
#         'createTime':date('2023/12/20 10:49:23'),
#         'startTime':date('2023/12/20 10:49:36'),
#         'endTime':date('2024/01/20 10:49:36'),
#         "price":20,
#         'comboCode':"测试code",
#         "comboName":"测试套餐",
#         "duration":1,
#         'payType':1,
#         "note":'ssss'
# }

#通用版抖店
# data = {'orderId': '6924937458948314730',
#         'platformStr': 'fxg',
#         "platformKey":"1664646",
#         'createTime':date('2023/12/20 10:33:14'),
#         'startTime':date('2024/10/03 20:43:39'),
#         'endTime':date('2024/11/03 20:43:39'),
#         "price":42,
#         'comboCode':"测试code",
#         "comboName":"测试套餐",
#         "duration":1,
#         'payType':1,
#         "note":'ssss'
# }

#通用版抖店供应链
# data = {'orderId': '6924926376760121213',
#         'platformStr': 'ddsc',
#         "platformKey":"7129813107433537827",
#         'createTime':date('2023/12/20 12:04:53'),
#         'startTime':date('2024/08/17 10:34:39'),
#         'endTime':date('2024/09/17 10:34:39'),
#         "price":20,
#         'comboCode':"测试code",
#         "comboName":"测试套餐",
#         "duration":1,
#         'payType':1,
#         "note":'ssss'
# }
#w微盟
#
# data = {'orderId': '2594988918628319232',
#         'platformStr': 'wm',
#         "platformKey":"4020058083638",
#         'createTime':date('2023/12/19 17:39:45'),
#         'startTime':date('2023/12/19 20:43:39'),
#         'endTime':date('2024/01/19 20:43:39'),
#         "price":20,
#         'comboCode':"测试code",
#         "comboName":"测试套餐",
#         "duration":1,
#         'payType':1,
#         "note":'ssss'
# }
#有赞
# data = {'orderId': 'E20190730104714038900036',
#         'platformStr': 'youzan',
#         "platformKey":"40267703",
#         'createTime':date('2023/12/20 11:39:45'),
#         'startTime':date('2023/12/20 11:39:45'),
#         'endTime':date('2024/12/20 11:39:45'),
#         "price":20,
#         'comboCode':"测试code",
#         "comboName":"测试套餐",
#         "duration":1,
#         'payType':1,
#         "note":'ssss'
# }

#微信小商店
data = {'orderId': '3244495339662639110',
        'platformStr': 'youzan',
        "platformKey":"40267703",
        'createTime':date('2023/12/20 11:39:45'),
        'startTime':date('2023/12/20 11:39:45'),
        'endTime':date('2024/12/20 11:39:45'),
        "price":20,
        'comboCode':"测试code",
        "comboName":"测试套餐",
        "duration":1,
        'payType':1,
        "note":'ssss'
}
response = requests.post(url, data=data,headers=headers)
print(response.text)
