import requests
import json


# SQLMap API的基本URL
api_url = 'http://127.0.0.1:8775/'
scan_url = 'https://jd.fhd001.com/'
admin_token= "19f61da5906f66470eeb8308c5a068c4"

data = {
    'url': scan_url,
    'token': admin_token
}
# 发送扫描任务请求
response = requests.get(f'{api_url}/task/new', json=data)
print(response,"response")
# 获取扫描任务ID
task_id = response.json()['taskid']
print(f'Scan task ID: {task_id}')

# 检查扫描任务状态
response = requests.get(f'{api_url}/scan/{task_id}/status')
status = response.json()['status']
print(f'Scan status: {status}')