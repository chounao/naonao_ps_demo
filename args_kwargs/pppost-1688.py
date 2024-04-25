import requests

# 发送请求
h = {'Content-Type':'application/x-www-form-urlencoded'}
body = {'shopId': 1624961198,
'status': 1,
'sort': 'itemId',
'desc': 'true',
'startConfirmTime': 1691596800,
'endConfirmTime': 1699631999,
'page': 1,
'pageSize': 100,
'referer': 'albbportal',
'token': '%7EU1MABQlfBgEITQBcXxdUQxJSVhYNEkcHUU1WDVoQBEsRB11AWRVBAANNUBwHVQgJUwwKVFJZAQY%3D%7E1%7E'}
response = requests.post('https://albbapi.fhd001.com/albb/queryAlbbOrder.do',body,h)



# 检查请求是否成功
if response.status_code == 200:
    # 解析响应数据
    data = response.json()
    # print(data)


#     seen = set()
    l = []
    for item in data['data']['list']:
        l.append(item['caid'])
    print(l)
    print(len(l))
    a = len(l) != len(set(l))
    print(a)


    #根据某个值判断个数
#     value_to_check = "DEkkk251FblOeXQRkO4qph8Ys04z47ibJebARtuoiaPa8Y1ibhpibaoWic9uz6pzv3HbtNFI1bs-DRP1USibxrepPibyxIhIBibHcxXtAR6joEl135RDjc8V9lBOfsQwtJ0yxKaDf3ichmibA1"
#
#     count = 0
#
#     for item in data['data']['list']:
#         if item['caid'] == value_to_check:
#             count += 1
#
#     # 打印结果
#     print(f"个数：{count}")
# else:
#     print("请求失败")
#     is_duplicate = False
#     for item in data['data']['list']:
#         if item['caid'] in seen:
#             is_duplicate = True
#             break
#         seen.add(item['caid'])
#
#         # 打印结果
#         if is_duplicate:
#             print("返回参数重复")
#         else:
#             print("返回参数不重复")
#     else:
#         print("请求失败")