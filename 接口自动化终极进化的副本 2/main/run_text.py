# coding: utf-8
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.send_email import SendEmail
from data.dependent_data import DependdentData
import json


class RunText:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.common_util = CommonUtil()
        self.sendmail = SendEmail()
        # 执行程序的主入口

    def go_on_run(self, pr=None):
        res = None
        pass_count = []
        fail_count = []
        row_count = self.data.get_case_lines()
        for i in range(1, row_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            data = self.data.get_data_for_json(i)
            is_run = self.data.get_is_run(i)
            header = self.data.get_data_header_json(i)
            expect = self.data.get_expect_data(i)
            depend_case = self.data.is_depend(i)
            # if depend_case != None:
            #     self.depend_data = DependdentData(depend_case)
            #     #获取相应数据的依赖
            #     depend_response_data = self.data.get_depend_key(i)
            #     #获取依赖的key
            #     depend_key = self.data.get_depend_field(i)
            #     data[depend_key] = depend_response_data
            # res = self.run_method.run_main(method,url,header,data)
            # print res'''
            '''if header == 'write':
                res = self.run_method.run_main(method, url, request_data)
                op_header = OperationHeader(res)
                op_header.write_cookie()

            elif header == 'yes':
                op_json = OperetionJson('../dataconfig/cookie.json')
                cookie = op_json.get_data('apsid')
                cookies = {
                    'apsid': cookie
                }
                res = self.run_method.run_main(method, url, request_data, cookies)
            else:
                res = self.run_method.run_main(method, url, request_data)'''

            if is_run:
                res = self.run_method.run_main(method, url, header, data)
                if self.common_util.is_contain(expect, res):
                    # print "测试通过"
                    print self.data.write_value(i, "pass")
                    pass_count.append(i)
                else:
                    # print "测试失败"
                    print self.data.write_value(i, res)
                    fail_count.append(i)

        self.sendmail.send_main(pass_count,fail_count)



if __name__ == "__main__":
    a = RunText()
    a.go_on_run()
