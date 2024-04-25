import requests
import os
# 设置API服务器地址和管理员令牌
api_url = 'http://127.0.0.1:8775/'
scan_url = 'https://jd.fhd001.com/'
admin_token= "31f39db359ff707d00af11a07568dca3"

# 构建扫描任务的请求数据

headers_file = 'C:/Users/86185/Desktop/mimt/h.txt'
# 请求头文件的路径
data = {
    'url': scan_url,
    'headers': open(headers_file, 'r').read(),
    'token': admin_token
}

# 发送扫描任务请求
response = requests.get(api_url + 'task/new', json=data)
print(response)
# 获取扫描任务ID
task_id = response.json()['taskid']
print(f'Scan task ID: {task_id}')
start = requests.post(api_url + f'scan/{task_id}/start')
print(start)
# 检查扫描任务状态
response = requests.get(api_url + f'scan/{task_id}/status')
status = response.json()['status']
log = requests.get(api_url + f'scan/{task_id}/log')
data = requests.get(api_url+f'scan/{task_id}/data')
print({data},'data')
print({log},"log")
print(f'Scan status: {status}')




