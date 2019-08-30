# coding:utf-8
import requests
import json
from base import  demo

url = 'http://47.97.208.158:8095/oto/pay/commit'
data = {"orderNo":"263924429134192640","payMethod":1,"payScene":"wap","returnUrl":"http://xyt.trtpfbdfzs.kevglt","source":"wap"}
header = {'Authorization': '46xujjprBWPqTjuHDhlYOIWkZu8MRKwWEBOM5xZksIDf1k/os2xCqcp5E7aVw4EnGi9r1ZK69uXVPaoMZjsq0214L6KYM8pgYQUhRPuZu0ohU9niSgyqoYoKvf+142sAFwcNF5g0Wl993A7bpLYAyDkNofeqlEmWAT+UNdJI+bzdT6UyRqx+2wjZWrNfRkqWPNMBGrsxCchYwXgYckQK9u5kvqfY0iTWUtKuWVo2APvuJzj8gQBNydsiISbkao7S',
    'Content-Type': 'application/json'}
def sent_get(header,url,data):
    res = requests.post(headers=header,url=url,data=json.dumps(data)).text
    # print res
    # print res.json()['code']
    return res
# print sent_get(header,url,data)
if __name__ == '__main__':
    print  sent_get(header,url,data)
    print type(sent_get(header,url,data))

    data = json.dumps(data)
    print type(data),data
# def diaoyong():
#    a = demo.RanMain
#    b = a.run_main("N5drNRtp8cHg9aqpfaEk/zQfivlEUKwJCYPHBjTV6Gk=","http://dev.lvtudiandian.com/train-tickets/api/ticket/train/hotCity","GET")
#    print  b
