import requests
import pandas as pd
import openpyxl
# 读取 Excel 文件
s=requests.session()
d = {}
df = pd.read_excel('C:/Users/86185/Desktop/周超杰/mimt/args_kwargs/到期未续费未登录用户.xlsx')
url = 'https://mgr.xyy001.com/qnfhdcs/base/queryBaseInfo.do'

# 获取第一列（从第二行开始）的数据
data_list = df.iloc[1:, 0].tolist()

h = {
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}
s.headers.update(h)

for i in data_list:
    data = {
        'sellerNick':int(i),
        'token':'VmRSYgZmBDMAZlUtB3UAHwBkUCRSOAc7VycNFVA9C35VEwI6UiZVF1AyUiMCbVQ7VyMNGV86V39XOwAdVycGFFZlUn4GMQRlADhVcgc1AHYAN1BgUm0HeVdnDXhQNQt3VXoCMlIvVXlQNVIxAmRUNlcxDWxfPldsVzQAbg%3D%3D'}

    r = s.post(url,data)
    # print(r.json())
    data = r.json()
    if 'sellerInfo' not in data['data']:
       print("11111")
    else:
        try:
             phone = data['data']['sellerInfo']['cellphone']
             
        except AttributeError as e:
            raise e
    print(i,phone)


