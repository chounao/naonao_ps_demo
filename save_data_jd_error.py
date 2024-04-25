import json

import mitmproxy.http
from mitmproxy import http,ctx

class Counter:
    def __init__(self,filter_url: str):
        self.url = filter_url
    def response(self,flow:mitmproxy.http.HTTPFlow):

        self.code = flow.response.status_code
        self.data = flow.response.get_text()
        if self.data != None:
            rcode =json.loads(self.data)
            self.r = rcode['rcode']
            self.s = rcode['scode']
            return self.r,self.s
    def request(self,flow:mitmproxy.http.HTTPFlow):
        if self.url in flow.request.url and 'POST' == flow.request.method:
            if self.code == 200 and self.s == 0 and self.r == 0:
                print("URL正常")
            else:
               self.error_url = flow.request.url
               self.f = 'C:/Users/86185/Desktop/mimt/jd_error/error.txt'
               with open(self.f,"w", encoding='utf-8') as f:
                   f.write(self.error_url)




addons=[
    Counter('https://jdapione.fhd001.com')

]
