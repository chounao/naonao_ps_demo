import requests
import pandas as pd
import os
import openpyxl
# 读取 Excel 文件
# s=requests.session()
# path = 'C:/Users/86185/Desktop/周超杰/mimt/args_kwargs/到期未续费未登录用户.xlsx'
# sheet_name = 'Sheet1'
# df = pd.read_excel(path,sheet_name)
# url = 'https://mgr.xyy001.com/qnfhdcs/base/queryBaseInfo.do'
#
# h = {
# 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
# }
# s.headers.update(h)
# phone_list = []
# for i in df['sellerId']:
#     data = {
#         'sellerNick':int(i),
#         'token':'VmQBMVExX2gHYVYuUSNaRVE1UiYFb1NvAHBdRQdqBXAKTFdvBnJfHQNhBXRYN1A%2FVSFXQwNmAytUOAgVAnJURlZlAS1RZl8%2BBz9WcVFjWixRZlJiBTpTLQAwXSgHYgV5CiVXZwZ7X3MDZgVmWD5QMlU9VzMDZAM9VDkIaA%3D%3D'}
#     r = s.post(url,data)
#     data = r.json()
#     if 'sellerInfo' in data['data']:
#         phone = data['data']['sellerInfo']['cellphone']
#         phone_list.append(phone)
#     else:
#         phone_list.append('N/A')
#
# df['phone'] = phone_list
#
# with pd.ExcelWriter(path,engine='openpyxl')as writer:
#     df.to_excel(writer,sheet_name=sheet_name,index=False)


def read():
    path = os.getcwd()+'/到期未续费未登录用户.xlsx'
    df = pd.read_excel(path, sheet_name = 'Sheet1')
    return df

def get_phone(token):
    s = requests.session()
    url = 'https://mgr.xyy001.com/qnfhdcs/base/queryBaseInfo.do'
    h = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    s.headers.update(h)
    phone_list = []
    for i in read()['sellerId']:
        data = {
            'sellerNick': int(i),
            'token':token
        }
        r = s.post(url, data)
        data = r.json()
        if 'sellerInfo' in data['data']:
            phone = data['data']['sellerInfo']['cellphone']
            phone_list.append(phone)
        else:
            phone_list.append('N/A')
    return phone_list
def save_excel(token):
    df = read()
    df['phone'] = get_phone(token)
    
    with pd.ExcelWriter(path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)


if __name__ == '__main__':
    token ='VmQBMVExX2gHYVYuUSNaRVE1UiYFb1NvAHBdRQdqBXAKTFdvBnJfHQNhBXRYN1A%2FVSFXQwNmAytUOAgVAnJURlZlAS1RZl8%2BBz9WcVFjWixRZlJiBTpTLQAwXSgHYgV5CiVXZwZ7X3MDZgVmWD5QMlU9VzMDZAM9VDkIaA%3D%3D'
    path = 'C:/Users/86185/Desktop/周超杰/mimt/args_kwargs/到期未续费未登录用户.xlsx'
    save_excel(token)