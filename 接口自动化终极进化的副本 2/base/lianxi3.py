# # coding:utf-8
import json
# import requests
# url = ' http://47.97.208.158:8092/ticket/train/trainSearch'
# data = {"fromStation":"hangzhoudong","toStation":"beijing","searchType":"0","trainDate":"20190227","ticketType":"1"}
# header = {'Authorization':'N5drNRtp8cHg9aqpfaEk/zQfivlEUKwJCYPHBjTV6Gk=','Content-Type':'application/json'}
# res = requests.get(url = url,params = data,headers = header)
# print res.text
# a ={"aa":"aaas"}
# # b = json.loads(a)
# print a.text
# print type(a)
#coding:utf-8
import requests
import json

base_url="http://api.codai.vip/"

def login():
   data={
        "mobile" :"17680727701",
        "password":"yyc1234567",
        "device"  :"30"
      }
   rq=requests.get(url=base_url+"login.json?",params=data)
   z=rq.text.encode('utf-8')
   print("接口:"+base_url+"login.json?",
      "\n" "传参：" + str(data),
      "\n" "回参：" + str(z),
      "\n" "响应时间：" + str(rq.elapsed))
   y=json.loads(z)
   assert y["success"]==True,y["success"]
login()