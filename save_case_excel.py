import json
import xlwt
import yaml
import urllib.parse
from mitmproxy import http,ctx,log




class tools_save_excel:
    def __init__(self,filter_url: str, filename: str ="C:/Users/86185/Desktop/mimt/1688_case.xls"):
        self.url = filter_url
        self.excel_row = ['编号','用例标题','请求头','接口地址','是否执行','请求方式','入参关键字','上传文件','请求数据','提取参数','后置sql','code']
        self.cases = [self.excel_row]
        self.counter = 1
        self.file = filename
        self.info = ctx.log
        self.yaml_ls = []
        self.status_code = None



    def response(self, flow: http.HTTPFlow):
        try:
            self.status_code = flow.response.status_code
        except:
            self.status_code = ''
            log.Log('请确认是否开启代理服务')
        return self.status_code

    def request(self,flow: http.HTTPFlow):
        self.params_dict = {}
        if self.url in flow.request.url:
            """编号"""
            number = "c"+str(self.counter)
            """标题"""
            title = "mitmproxy录制接口" + str(self.counter)
            method =flow.request.method.lower()
            url = flow.request.url

            """
            flow.request.headers.fields返回的数据为((b'',b''),(b'',b''),(b'',b''))格式
            """
            # headers_dict={}
            # for h in (list(flow.request.headers.fields)[1:-1]):#去掉前后的括号后便利
            #     # new_h = h.translate({ord(n):None for n in "b'"})
            #     new_h = str(h).split("b'")[1].split("',")[0]#前获取key
            #     headers_dict[new_h] = str(h).split(new_h + "', b'")[1].split("')")[0]#通过key获取value并放入到字典内

            headers_dict = {key.decode(): value.decode() for key, value in (list(flow.request.headers.fields)[1:-1])}

            data =flow.request.get_text()
            """
            获取content-type 判断那种数据类型
            根据from :application/x-www-form-urlencoded
            根据json :application/json
            """
            try:
                content_type = flow.request.headers['Content-Type']
            except KeyError:
                content_type =''
            if 'from' in content_type:
                data_type = 'data'
            elif 'json' in content_type:
                data_type = 'json'
            else:
                """ 如果get请求或者post某些请求在url里，一般是参数内？后是传参处理传参"""
                data_type = 'params'

                if '?'in url:
                    """ 处理 Content-Type:    application/x-www-form-urlencoded
                    flow.request.get_text()默认生成的数据 username=admin&password=123456
                    """
                    # 一般都是 https://xxxxx?token=xxx&a=XXX&截取？后的数据
                    data = url.split('?')[1]

            data = {key: list(value)[0] for key, value in (urllib.parse.parse_qs(data)).items()}

            """返回值code"""
            status_code = self.status_code
            excel_case = [number,title,headers_dict,url.split('?')[0],"是",method,data_type,"",data,"","",status_code]
            self.cases.append(excel_case)
            self.counter += 1


            """保存成excel"""
            self.excel_cases()



            """ 保存成yaml/json"""
            self.yaml_data = {'number':number,"title":title,"header":headers_dict,"url":url.split('?')[0],"method":method,"data":data,"status_code":status_code}
            self.yaml_ls.append(self.yaml_data)
            self.save_data(self.yaml_ls)
        else:
            log.Log('请确认是否开启代理服务')

    def excel_cases(self):
        """
        对二维列表cases进行循环并将内容写入单元格中
        :return:
        """
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet("case",cell_overwrite_ok=True)

        for x in range(len(self.cases)):
            for y in range(len(self.cases[x])):
                worksheet.write(x, y, str(self.cases[x][y]))
        try:
            workbook.save(self.file)
        except Exception as e:
            print(e)

    def save_data(self,data):
        # 存到文件
        with open("C:/Users/86185/Desktop/mimt/1688_case.yaml", "w", encoding='utf-8') as f:
            yaml.dump(data, f)

        with open("C:/Users/86185/Desktop/mimt/1688_case.json", "w", encoding='utf-8') as f:
            json.dump(data, f,indent=4)



""" 
设置抓包
https://qimg2.xyy001.com/qnjymp/stable/main/index.html?token=%257EVgUIBA9bAAZfVQRXHwYDG1ddDAxUVQoDAgEV04WShrTy1rGj09qGWx8HHwNSWEBSSlUUVxYJXxhYRlVbDAE%253D%257E1%257E#/v5/printList
https://albbstatic.xyy001.com/albb/albb.html#/trades?token=%257EAFIFCgBZDFYAGllYChVSQBJXCRZeRkAAA0pTXFBMBBdMBF9LXhJCUQcaCRhSVw8LVQZSXQ4HBAY%253D%257E1%257E&user_platform=1688
"""
addons=[
    tools_save_excel("https://albbapi.fhd001.com/")
]


"""
mitmdump -p 8080 -s  C:/Users/86185/Desktop/mimt/save_case_excel.py
"""