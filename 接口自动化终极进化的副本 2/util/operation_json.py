# coding:utf-8
import json
# fp = open("../dataconfig/user.json")
# data = json.load(fp)
# print data["user1"]
class OperationJson:
    def __init__(self):
        self.data = self.read_data()

                                                                 #读取json文件，
    def read_data(self):
       with open("../dataconfig/user.json") as fp:
          data =  json.load(fp)
          return  data

                                                                # 根据关键字获取数据
    def get_data(self,id):
     #   return id
        #return self.data
        if id == "":
              return None
        return  self.data[id]

if __name__ =="__main__":
    opers = OperationJson()
    print opers.get_data("")
