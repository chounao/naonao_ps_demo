import http

from mitmproxy import http,ctx,log
import json



class Counter:
    def __init__(self,filter_url: str):
        self.url = filter_url
        self.headers_list = ['referer','origin']
        self.set_data = 'https://jdapione.fhd001.com/'#修改的数据
        self.Error_list = []
        self.NotFound_lits =[]
    # def request(self, flow:http.HTTPFlow):
    #     if self.url in flow.request.url:
    #         flow.request.host = '11111'
    #         for i in self.headers_list:
    #             print(i, "开始---------------------------------------")
    #             self.NotFound_txt = "NotFound_" + i + ".txt"
    #             self.Error_txt = "Error_" + i + ".txt"
    #             self.NotFound_message = " header内没有属性" + i
    #             self.Error_message = " 重置后依然存在问题" + i
    #
    #             if i in flow.request.headers:
    #                 try:
    #                     flow.request.headers['HOST'] = None
    #                     if flow.request.headers[i] != None:
    #                         print(flow.request.url, "PASS")
    #                     else:
    #                         print(flow.request.url + self.Error_message)
    #                         self.Error_list.append(flow.request.url)
    #                 except:
    #                     print("无法赋值给" + i)
    #             else:
    #                 print(flow.request.url + self.NotFound_message)
    #                 self.NotFound_lits.append(flow.request.url)
    #
    #             print(i, "结束-----------------------------------")
    #         self.save_txt(self.NotFound_lits, self.NotFound_txt)
    #
    # def response(self,  flow:http.HTTPFlow):
    #     if self.url in flow.request.url:
    #         for i in self.headers_list:
    #             if i in flow.response.headers:
    #                 print("PASS")
    #             else:
    #                 print(flow.response.headers[i])
    #                 self.Error_list.append(flow.request.url)
    #         self.save_txt(self.Error_list, self.Error_txt)
    #
    #         print(
    #             "***************************************************************************************************************************************")
    #
    # def save_txt(self, list_name, txt_name):
    #     with open('C:/Users/86185/Desktop/mimt/save_txt/' + txt_name, "w", encoding='utf-8') as f:
    #         json.dump(list_name, f)
    def request(self, flow: http.HTTPFlow):
        if self.url in flow.request.url:
            #host是在flow.request.host单独判断
            try:
                before_host = flow.request.host
                flow.request.host = self.set_data#改host
                after_host = flow.request.host
                print(before_host,after_host)
                if before_host == after_host:
                    print("Host PASS")
                else:
                    print('HOST FAIL')
            except:
                print("NOT FOUND HOST")
        #'referer','origin'两个便利判断
            for i in self.headers_list:
                if i in flow.request.headers:
                    before = flow.request.headers[i]
                    print(before)
                    try:
                        flow.request.headers[i] = self.set_data#改'referer','origin'
                        after = flow.request.headers[i]
                        # print(after)
                        if after != self.set_data :
                            print(self.url+f'{i} PASS')

                        else:
                            print(self.url+f"{i} FAIL++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    except:
                        print("dont set")
                else:
                    print("NOT FOUND")

    def response(self,flow: http.HTTPFlow):
        if self.url in flow.request.url:
            headers = flow.response.headers
            print(headers)
            if self.set_data in headers:
                print(self.url+'Fail-------------------------------------------------------')

addons=[
    Counter('https://albbapi.fhd001.com/')

]