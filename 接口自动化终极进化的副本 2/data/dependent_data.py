# coding:utf-8
import sys
import json
from data.get_data import GetData
from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from jsonpath_rw import jsonpath,parse
class DependdentData:
    def __init__(self,case_id):
        self.opera_excel = OperationExcel()
        self.data = GetData()
        self.case_id = case_id


    #通过case_id 获取case_id 整行数据
    def get_case_lines_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data
    #执行依赖测试，获取结果
    def run_dependnt(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        request_method = self.data.get_request_method(row_num)
        request_header = self.data.get_data_header_json(row_num)
        request_url = self.data.get_request_url(row_num)
        res = run_method.run_main(request_method,request_url,request_header,request_data)
        return json.loads(res)
        # return res
    # 根据依赖的key，去获取 执行依赖case的相应 response，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependnt()
        print depend_data
        print response_data
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        # aa = [madle.value for math in madle][0]
        return [madle.value for math in madle]
        # print aa

if __name__ == "__main__":
    # DependdentData("Imooc-01")
    # a = DependdentData("Imooc-02")
    # print a.get_data_for_key(4)
    order = { "code": 200,
              "data": [{"cityId": 383},{"cityId": 384,"cityName": "杭州"}],
              "id": 'null',"lastSearchTime": 'null',
              "memberId": 'null',
            "message": "历史城市查询成功"
              }
    # order = json.loads(orde)
    # print orde['data'][0]['cityId']
    res = "data[*].cityId"
    json_exe = parse(res)
    madle = json_exe.find(order)
    # print type(orde)
    print res
    print [math.value for math in json_exe.find(order)]

    '''- - - - -- - >>'''

    '''order = {
        "data": {
            "_input_charset": "utf-8",
            "body": "1710141907182334",
            "it_b_pay": "1d",
            "notify_url": "http://order.imooc.com/pay/notifyalipay",
            "out_trade_no": "1710141907182334",
            "partner": "2088002966755334",
            "payment_type": "1",
            "seller_id": "yangyan01@tcl.com",
            "service": "mobile.securitypay.pay",
            "sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
            "sign_type": "RSA",
            "string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
            "subject": "慕课网订单-1710141907182334",
            "total_fee": 299
        },
        "errorCode": 1000,
        "errorDesc": "成功",
        "status": 1,
        "timestamp": 1507979239100
    }
    res = "data.payment_type"
    json_exe = parse(res)
    madle = json_exe.find(order)
    print [math.value for math in madle][0]'''

