# coding:utf-8
class global_var:
    #caseid
    Id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'
                                 #获取caseid
def get_id():
    return global_var.Id
                                 #获取url
def get_url():
	return global_var.url

                                #是否执行
def get_run():
	return global_var.run

                                #请求方法
def get_run_way():
	return global_var.request_way

                            #获取请求头
def get_header():
	return global_var.header

                             #获取case依赖 ID，用例标号
def get_case_depend():
	return global_var.case_depend

                                #获取  数据依赖的返回数据  Value
def get_data_depend():
	return global_var.data_depend
                             ##获取 数据依赖的返回字段  Key
def get_field_depend():
	return global_var.field_depend

def get_data():             #获取请求数据
	return global_var.data
                            #获取逾期结果
def get_expect():
	return global_var.expect
                            #获取实际结果
def get_result():
	return global_var.result

def get_header_value():
	return global_var.header
if __name__ =="__main__":
    a= global_var()
    print  a.get_header_value()