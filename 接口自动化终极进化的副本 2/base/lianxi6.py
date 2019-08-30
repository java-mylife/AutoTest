# coding:utf-8
from jsonpath_rw import jsonpath,parse
string = u'127米'
string2 = string.encode('gbk')
print (type(str))
print (filter(str.isdigit, string2))