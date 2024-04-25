import time
import requests
import datetime
import json
class send_it:
    def __init__(self):
        self.url ='https://dev-chcapi.fhd001.com/fhd/css/sendMessage?token={}&referer=fhdportal&platFrom=fhdportal&platform=fhd&specificPlatform='
        #platformId = 9
        self.get_session_url ='https://dev-chcapi.fhd001.com/fhd/css/saveSession?platformId={}&token={}&referer=fhdportal&platform=fhd&specificPlatform='
        self.transferAgent_url = 'https://dev-chcapi.fhd001.com/fhd/css/transferAgent?token={}&referer=fhdportal&platFrom=fhdportal&platform=fhd&specificPlatform=&sessionId={}'
    def session(self):
        h = {
            'Content-Type': 'application/json'
        }
        s = requests.session()
        return s
    def get_session_id(self,platformId,token):
        '''
        获取对应的sessionid
        :param platformId:
        :param token:
        :return:
        '''
        s = self.session()
        new_session = self.get_session_url.format(platformId,token)

        # print(new_session)
        try:
            data = s.get(new_session)
            sessionid = data.json()['data']
        except ValueError as e:
            raise e
        return sessionid,s
    def transferAgent(self,platformId,token):
        '''
        进入人工
        :param platformId:
        :param token:
        :return:
        '''
        sessionid,s= self.get_session_id(platformId,token)

        new_transferAgent = self.transferAgent_url.format(token,sessionid)
        try:
            data = s.get(new_transferAgent)
            print(data.json())
            if data.json()['data'] != 'true':
                print('没有进入人工')
            else:
                print("进入人工")
        except ValueError as e:
            raise e
        return sessionid,s




    def post(self,agentId, customerId, token,platformId):
        sessionid, s = self.transferAgent(platformId, token)
        new_url = self.url.format(token)
        content = ['hello', 'code', 'world', 'set', 'big']
        for i in content:
            try:
                body = {"agentId": agentId,
                        "content": i,
                        "customerId": customerId,
                        "sessionId": sessionid,
                        "specialType": 0,
                        "type": 1,
                        "token": token
                        }
                r = s.post(new_url,json.dumps(body,ensure_ascii=False))
                print(datetime.datetime.now())
                print(r.json())
                s.close()
                print('结束')
            except AttributeError as e:
                raise e





if __name__ == '__main__':
    send_body ={
        'token': '~UFcFBQdRAAcGVlYHAVsAAFcNFS4RD2hYFQR7TXkRD2EKF1d%252BHFcbAQZQUgcDVAAJUhgJVlQ%253D~1~',
        'picture_data': '/ctkTfSXDYpic4UOdZOsIvXWUM9GJwP8ib9sp5I4lLbktLt7iaKfFGCahEHTnyZ0sgjwwE0CHNUtWNDNhDuQyDmMfQ/132',
        'name': 'JunYoveL',
        'customerId': 2,
    },{
        'token': '~VlUDAgBWBhxSGAJTTwBSSQUYWh0HAkhUABhUTQJIUA9UUgoGCVICBB1RUQE%3D~1~',
        'picture_data': '/Q0j4TwGTfTLRrXUnQ7n5vG2bXPMooFQYxyGw4vadia79F5plrgQdkrwBA3d2ObyDcpiaNYII98sBUIVxAqQmmKJA/132',
        'name': 'cyccyccyc',
        'customerId': 4,

    },{
        'token': '~UlMABQlfAwEFTUR1A0ZwBUMNDkEhVBR2V0R2IBYhWB1cVhdwCUNyCRRYVhV0WhR1XxEAU0EjCBImWBJYBEEjAUAkCxcJURJyCEQkCRNaBhUkDRVBIVQUdlZEDlYWIVQdJFUXc3FDcgkUWFYVdFoUdV8RAFNBIwgSJlgSWARBIwFAJAsXCVEScghEJAkTWgYVJA0cIV1ECABGIw5NAUhQD1RSCgYJXgMBHVFSAg%3D%3D~1~',
        'picture_data': '/Q0j4TwGTfTLRrXUnQ7n5vG2bXPMooFQYxyGw4vadia79F5plrgQdkrwBA3d2ObyDcpiaNYII98sBUIVxAqQmmKJA/132',
        'name': '套太闹闹闹闹闹闹',
        'customerId': 7,

    }

    a = send_it()
    '''
   :param agentId:客服id
   :param content:消息内容
   :param customerId:客户id
   :param sessionId:会话id
   :param specialType:特殊类型：0 无 1 点击联系人工客服 2 问题没有解决吗？点击联系人工客服
   :param type:消息类型：1 文本 2 图片 3 文件 4 视频
   :return:
   '''
    #同一个客服一个平台
    def send_data(agentId,platformId):
        a.post(agentId, send_body[0]['customerId'], send_body[0]['token'], platformId)
        a.post(agentId, send_body[1]['customerId'], send_body[1]['token'], platformId)
        a.post(agentId, send_body[2]['customerId'], send_body[2]['token'], platformId)
        # for i in send_body:
        #     a.post(agentId,i['customerId'],i['token'],platformId)



    send_data(1,9)



