import http

from mitmproxy import http,ctx,log
import json



class Counter:
    def __init__(self,filter_url: str,):
        self.url = filter_url

    def save_txt(self, url_name, txt_name):
        with open('C:/Users/86185/Desktop/mimt/1688_text/' + txt_name, "w", encoding='utf-8') as f:
            json.dump(url_name, f)
    def request(self,flow:http.HTTPFlow):
        test_data = 'https://jdapione.fhd001.com/'
        for self.url in flow.request.url:
            txt_name = self.url.split('/')[-1][:-3]+'.txt'
            # """XSS测试"""
            # if "text/html" in flow.response.headers.get("content-type", ""):
            #     # 获取原始的HTML内容
            #     html = flow.response.get_text()
            #
            #     # 在HTML中插入XSS注入代码
            #     xss_payload = "<script>alert('XSS注入测试');</script>"
            #     modified_html = html.replace("</head>", xss_payload + "</head>")
            #
            #     # 更新响应内容
            #     flow.request.set_text(modified_html)

            """CSRF漏洞"""
            headers = flow.request.headers
            print(headers)

            try:
                headers["referer"] = test_data
                if test_data in flow.request.headers["referer"]:
                        self.save_txt(self.url,txt_name='referer_'+txt_name)
                else:
                    print(self.url+"refererpass")
                    try:
                        headers["origin"] = test_data
                        if test_data in flow.request.headers["origin"]:
                            self.save_txt(self.url, txt_name='origin_'+txt_name)
                        else:
                            print(self.url+"Originpass")
                            try:
                                headers["host"] = test_data
                                if test_data in flow.request.headers["host"]:
                                    self.save_txt(self.url, txt_name="host_"+txt_name)
                                else:
                                    print(self.url + "hostpass")

                            except:
                                print(self.url + "NOT FOUND host")
                    except:
                        print(self.url+"NOT FOUND origin")

            except:
                print(self.url+"NOT FOUND Referer")




            # """跨域防护测试"""
            # # 修改请求头
            # flow.request.headers["Origin"] = "https://www.example.com"
            # # 打印修改后的请求头
            # print(flow.request.headers)
            #
            #
            # """ host头攻击"""
            # # 修改Host头
            # flow.request.headers["Host"] = "www.attacker.com"
            # flow.request.set_text()
            # # 打印修改后的请求头
            # print(flow.request.headers)


    # def response(self,flow:http.HTTPFlow):
    #     for self.url in flow.request.url:
    #         """CSRF漏洞"""
    #         if "csrf_token" in flow.response.text:
    #             print("Potential CSRF vulnerability found!")
    #             # 保存响应数据到文
    #             with open("csrf_results.txt", "a") as f:
    #                 f.write(flow.response.text + "\n")
    #
    #         """跨域防护测试"""
    #         with open("request.txt", "a") as f:
    #             f.write(flow.request.pretty_url + "\n")
    #
    #         """host头攻击"""
    #         # 打印修改后的Host头
    #         print("Modified Host: ", flow.request.headers["Host"])
    #
    #         # 保存请求和响应到文件
    #         with open("request.txt", "w") as f:
    #             f.write(str(flow.request))
    #         with open("response.txt", "w") as f:
    #             f.write(str(flow.response))







addons=[
    Counter('https://albbapi.fhd001.com/')

]
