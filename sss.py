#
# import requests
# import json
#
#
# # SQLMap API的基本URL
# api_url = 'http://127.0.0.1:8775/'
# scan_url = 'https://jdapione.fhd001.com'
# admin_token= "da781ab419862bf2285b3f92e52081e6"
#
#
#
#
# #发起新的扫描任务
# def start_scan(headers):
#     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#     data = {
#             'url':scan_url,
#             'token':admin_token}
#     response = requests.get(api_url + 'task/new', headers=headers, json=data)
#     print(response.json())
#     task_id = response.json()['taskid']
#     print(task_id)
#     return task_id
#
# # 获取扫描任务的状态
# def get_scan_status(task_id):
#     response = requests.get(api_url + f'scan/{task_id}/status')
#     status = response.json()['status']
#
#     print(status,"+++++++++++++++")
#     return status
#
# # 获取扫描结果
# def get_scan_results(task_id):
#     response = requests.get(api_url + f'task/{task_id}/data')
#     results = response.json()
#     print(results,"-----------------")
#     return results
#
# # 扫描HTTP头部
# def scan_headers(headers):
#     scan_task_id = start_scan(headers)
#     while True:
#         status = get_scan_status(scan_task_id)
#         if status == 'terminated':
#             break
#         elif status == 'running':
#             continue
#         else:
#             print('扫描任务出错')
#             break
#     scan_results = get_scan_results(scan_task_id)
#     print(scan_results)
#
# # 要扫描的HTTP头部
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#     'Referer': 'https://oss.fhd001.com/'
# }
#
# # 扫描HTTP头部
# scan_headers(headers)
#
#
#
#
#
import requests

import json

import time

def sqlmapapi(url):

    headers = {

        'Content-Type': 'application/json'

    }

    scan_url={

        'url':url

    }

    scan_task_url='http://127.0.0.1:8775/task/new'

    scan_task=requests.get(scan_task_url)

    #print(scan_task.json())

    scan_task_id=scan_task.json()['taskid']

    #print(scan_task_id)

    if 'success' in scan_task.content.decode('utf-8'):

        print('sqlmapapi task create success...')

        scan_task_set_url = 'http://127.0.0.1:8775/option/' + scan_task_id + '/set'

        scan_task_set = requests.post(scan_task_set_url,data=json.dumps(scan_url),headers=headers)

        #print(scan_url)

        #print(scan_task_set.content.decode('utf-8'))

        if 'success' in scan_task_set.content.decode('utf-8'):

            print('sqlmapapi taskid set success')

            scan_start_url='http://127.0.0.1:8775/scan/'+scan_task_id+'/start'

            scan_start=requests.post(scan_start_url,data=json.dumps(scan_url),headers=headers)

            #print(scan_start.content.decode('utf-8'))

            if 'success' in scan_start.content.decode('utf-8'):

                print('sqlmapapi scan start success')

                while 1:

                    scan_status_url = 'http://127.0.0.1:8775/scan/' + scan_task_id + '/status'

                    scan_status = requests.get(scan_status_url)

                    #print(scan_status.content.decode('utf-8'))

                    if 'running' in scan_status.content.decode('utf-8'):

                        print(url + '->the scan is running')

                        pass

                    else:

                        print('sqlmapapi scan end')

                        scan_data_url='http://127.0.0.1:8775/scan/' + scan_task_id + '/data'

                        scan_data=requests.get(scan_data_url).content.decode('utf-8')

                        with open(r'scan_result.txt','a+') as f:

                            f.write(url+'\n')

                            f.write(scan_data+'\n')

                            f.write('==========python sqlmapapi=========='+'\n')

                            f.close()

                        #print('delete taskid')

                        scan_deltask_url = 'http://127.0.0.1:8775/task/' + scan_task_id + '/delete'

                        scan_deltask=requests.get(scan_deltask_url)

                        if 'success' in scan_deltask.content.decode('utf-8'):

                            print('delete taskid success')

                        break

                    time.sleep(3)

if __name__ == '__main__':

    print("url check finished.....")

    for url in open('C:/Users/86185/Desktop/post.txt'):

        url=url.replace('\n','')

        sqlmapapi(url)
