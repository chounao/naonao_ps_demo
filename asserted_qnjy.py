import pandas as pd
import requests
import os
import json

def assert_link(token,id):
    url = 'https://qnjy.xyy001.com/top/itemsSellerGet.do'
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    try:
        params = {"format": "json", "num_iid": id,
                  "fields": "num_iid,title,pic_url,price,seller_cids,outer_id,list_time,num,barcode,sku.sku_id,sku.properties_name,sku.properties,sku.quantity,sku.outer_id,sku.price,sku.barcode,property_alias,item_weight,item_size"}
        data = {
            'param': json.dumps(params),
            'timeout': None,
            'token':token
        }
        re = requests.post(url,data,headers)
        r = re.json()
        return r
    except:
        return False
item_list = []
token_list = []
name = os.path.dirname(os.path.abspath(__file__))+'\qnjy.xlsx'
df = pd.read_excel(name)
for index,row in df.iterrows():
    token = row.iloc[5]
    id = row.iloc[3]
    cluster = row.iloc[0]
    re = assert_link(token,id)
    try:
        if '商品服务调用失败' in re['data']:
            item_list.append([cluster,row.iloc[1]])
    except:
        token_list.append([cluster,row.iloc[1]])


if len(item_list) == 0:
    print("现有商品依然有效")
else:
    for data in item_list:
        print("现在无效商品为对应的商家为")
        print(data)

if len(token_list) == 0:
    print("现有token依然有效")
else:
    for data in token_list:
        print("现在无效token为对应的商家为")
        print(data)
