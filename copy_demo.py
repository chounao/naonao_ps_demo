#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-

import json

import mitmproxy.http
import xlwt

# 上传文件接口不能录入文件参数 , excel单元格限制： Exception: String longer than 32767 characters
from mitmproxy import ctx


class Counter:
    def __init__(self, filter_url: str, filename: str = "C:/Users/86185/Desktop/mim/case_data1.xls"):
        """
        基于mitmproxy抓包生成用例数据
        :param filter_url: 需要过滤的url
        :param filename: 生成用例文件路径
        """
        self.url = filter_url
        self.excel_row = [
            '编号',
            '用例标题',
            '请求头',
            '接口地址',
            '是否执行',
            '请求方式',
            '入参关键字',
            '上传文件',
            '请求数据',
            '提取参数',
            '后置sql',
            '预期结果']
        self.cases = [self.excel_row]
        self.counter = 1
        self.file = filename

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
        mitmproxy抓包处理响应，在这里汇总需要数据
        :param flow:
        :return:
        """
        if self.url in flow.request.url:
            # 编号
            number = "C" + str(self.counter)
            # 标题
            title = "mitmproxy录制接口" + str(self.counter)
            try:
                token = flow.request.headers["Authorization"]
            except KeyError:
                token = ''
            header = json.dumps({"Authorization": token})
            data = flow.request.text
            # 请求地址，config.yaml 里面基准环境地址 写 空字符串
            method = flow.request.method.lower()
            url = flow.request.url
            try:
                content_type = flow.request.headers['Content-Type']
            except KeyError:
                content_type = ''
            if 'form' in content_type:
                data_type = "data"
            elif 'json' in content_type:
                data_type = 'json'
            else:
                data_type = 'params'
                if '?' in url:
                    data = url.split('?')[1]
            data = self.handle_form(data)
            # 预期结果
            expect = json.dumps(
                {".": json.loads(flow.response.text)}, ensure_ascii=False)

            # 日志
            # log.info(url)
            # log.info(header)
            # log.info(content_type)
            # log.info(method)
            # log.info(data)
            # log.info(flow.response.text)
            case = [
                number,
                title,
                header,
                url.split('?')[0],
                "是",
                method,
                data_type,
                "",
                data,
                "",
                "",
                expect]
            self.cases.append(case)
            self.counter += 1
            # 文件末尾追加
            self.excel_cases()

    def excel_cases(self):
        """
        对二维列表cases进行循环并将内容写入单元格中
        :return:
        """
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('用例数据')
        for x in range(len(self.cases)):
            for y in range(len(self.cases[x])):
                worksheet.write(x, y, self.cases[x][y])

        try:
            workbook.save(self.file)
        except Exception as e:
            print(e)

    def handle_form(self, data: str):
        """
        处理 Content-Type:    application/x-www-form-urlencoded
        默认生成的数据 username=admin&password=123456
        :param data: 获取的data 类似这样  username=admin&password=123456
        :return:
        """
        data_dict = {}
        if data.startswith('{') and data.endswith('}'):
            return data
        try:
            for i in data.split('&'):
                data_dict[i.split('=')[0]] = i.split('=')[1]
            return json.dumps(data_dict)
        except IndexError:
            return ''


addons = [
    Counter("https://albbapi.fhd001.com/")
]

"""
mitmweb -s tools\recording.py 启动
ctrl + C 停止 并生成完整用例
mitmdump -p 8080 -s  C:/Users/86185/Desktop/mimt/copy_demo.py
"""