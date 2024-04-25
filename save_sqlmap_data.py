import json

import mitmproxy.http
from mitmproxy import http,ctx

class Counter:
    def __init__(self,filter_url: str):
        self.url = filter_url
    def request(self,flow:mitmproxy.http.HTTPFlow):
        if self.url in flow.request.url:
            if flow.request.method == 'POST':
                if 'query'or'elete'or'get' in flow.request.path:
                    self.method = flow.request.method
                    self.path  =flow.request.path
                    self.host = flow.request.host
                    self.headers_dict = {key.decode(): value.decode() for key, value in (list(flow.request.headers.fields)[1:-1])}
                    self.user_agent =self.headers_dict.get('User-Agent')
                    self.content_type = self.headers_dict.get('Content-Type')
                    self.body = flow.request.get_text()


                    self.f = 'C:/Users/86185/Desktop/mimt/sqlmap/'+self.path.split('/')[-1][:-3]+'.txt'
                    with open(self.f,"w", encoding='utf-8') as f:
                        f.write(self.method+" "+self.path+' HTTP/1.1\n')
                        f.write('Host:'+self.host+'\n')
                        f.write('User-Agent:'+str(self.user_agent)+'\n')
                        f.write('Content-Type:'+str(self.content_type)+'\n')
                        f.write(' '+'\n')
                        f.write(self.body)
            self.data = []
            if flow.request.method == 'GET':
                self.url = flow.request.url
                self.save_data = self.url+' HTTP/1.1'
                self.data.append(self.save_data)
            for i in self.data:
                with open('C:/Users/86185/Desktop/mimt/get.txt',"w",encoding='utf-8') as f:
                    f.write(i+'\n'+' \n')


addons=[
    Counter('https://qnjy.xyy001.com')

]
