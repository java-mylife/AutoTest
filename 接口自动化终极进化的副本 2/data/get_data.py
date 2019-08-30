# coding:utf-8
from util.operation_excel import OperationExcel
import data_config
from  util.operation_json import OperationJson
from util.connect_db import OperationMysql
class GetData:
    def __init__(self):
        self.oprera_excel = OperationExcel()
    def get_case_lines(self):
       return self.oprera_excel.get_lines()
                                                        #获取是否执行
    def get_is_run(self,row):
        flag = None
        col =int(data_config.get_run())
        run_model = self.oprera_excel.get_cell_value(row,col)
        if run_model == "yes":
            flag = True
        else:
            flag = False
        return  flag
                                                    #是否携带header
    def is_header(self,row):
        col = int(data_config.get_header())
        header = self.oprera_excel.get_cell_value(row,col)
        if header !="":
            return header
        else:
            return None
                                                    #获取请求方式
    def get_request_method(self,row):
         col = int(data_config.get_run_way())
         request_method = self.oprera_excel.get_cell_value(row,col)
         return request_method
                                                    #获取url
    def get_request_url(self,row):
        col = int(data_config.get_url())
        request_url =self.oprera_excel.get_cell_value(row,col)
        return  request_url


                                                     #获取exclee请求json关键字数据
    def get_request_data(self,row):
        col = int(data_config.get_data())
        requests_data = self.oprera_excel.get_cell_value(row,col)
        if requests_data == "":
            return  None
        return requests_data

                                                        #获取请求头 header关键字
    def get_header_data(self,row):
        col = int(data_config.get_header())
        data =self.oprera_excel.get_cell_value(row,col)
        return data


                                                 #通过json关键字 拿到json里面data数据
    def get_data_for_json(self,row):
        opera_json = OperationJson()
        #str = self.get_request_data(row)
        request_data = opera_json.get_data(self.get_request_data(row))
        return  request_data

                                                     #通过 json文件拿到 header、数据
    def get_data_header_json(self,row):
        opera_json = OperationJson()
        #str = self.get_request_data(row)
        header_data = opera_json.get_data(self.get_header_data(row))
        return  header_data


                                                    #获取预期结果
    def get_expect_data(self,row):
        col = int(data_config.get_expect())
        expect = self.oprera_excel.get_cell_value(row,col)
        if expect =="":
            return None
        return expect
    def get_expcect_data_for_mysql(self,row):    #通过sql过去预期结果
        op_mysql = OperationMysql()
        sql = self.get_expect_data(row)
        res = op_mysql.serch_one(sql)
        return res.decode('unicode-escape')


                                                        #写入数据
    def write_value(self,row,value):
        col = int(data_config.get_result())
        self.oprera_excel.write_value(row,col,value)

    def get_depend_key(self,row):                      #获取依赖数据的values
        col = int(data_config.get_data_depend())
        depend_key = self.oprera_excel.get_cell_value(row,col)
        if depend_key =="":
            return None
        else:
            return depend_key
    def is_depend(self,row):                            #获取依赖的caseID 并判断是否有依赖的case
        col = int(data_config.get_case_depend())
        depend_case_id = self.oprera_excel.get_cell_value(row,col)
        if depend_case_id =="":
            return None
        else:
            return depend_case_id
    def get_depend_field(self,row):
        col = int(data_config.get_field_depend())      #获取 依赖的返回数据 的字段
        depend_field = self.oprera_excel.get_cell_value(row,col)
        if depend_field =="":
            return None
        else:
            return depend_field

if __name__=="__main__":
    a = GetData()
    # print a.get_request_data(2)
    # print a.get_request_method(2)
    # print a.get_is_run(2)
    # print a.get_request_url(2)
    # print  a.get_header_data(2)
    # print a.get_data_header_json(2)
    # print a.get_request_data(2)
    # print a.get_data_for_json(2)
    # b= a.get_expect_data(2)
    print a.get_depend_key(5)
    print a.get_depend_field(5)
    # print b