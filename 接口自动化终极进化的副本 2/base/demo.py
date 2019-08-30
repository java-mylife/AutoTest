# coding:utf-8
import requests
import json
class RanMain:

    def sent_get(self,header,url,data):
		res = requests.get(headers=header,url=url,data=data).json()
		return res

    def sent_post(self,header,url,data):
		res = requests.post(headers=header,url=url,data=data).json()
		return res

    def run_main(self,header,url,method,data=None):
		res = None
		if method == "GET":
			res = self.sent_get(header,url,data)
              # print "get"
		else:
			res = self.sent_post(header,url,data)
		return res
if __name__ == '__main__':
    run = RanMain()
    url = 'http://47.97.208.158:8095/oto/pay/commit'
    data = {"orderNo":"263924429134192640","payMethod":1,"payScene":"wap","returnUrl":"http://xyt.trtpfbdfzs.kevglt","source":"wap"}
    header={'Authorization':'N5drNRtp8cHg9aqpfaEk/zQfivlEUKwJCYPHBjTV6Gk=','Content-Type':'application/json'}
# run = RanMain(headers,url,method,data=None)
    print run.sent_post(header,url,'post')