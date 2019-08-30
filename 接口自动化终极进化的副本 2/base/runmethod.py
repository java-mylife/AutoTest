# coding:utf-8
import requests
import json
class RunMethod:
    def post_main(self,url,header,data):
        res =None
        if header !="":
            res = requests.post(url=url,data=json.dumps(data),headers=header,verify=False)
        else:
            res = requests.post(url=url,data=json.dumps(data),verify=False)
        return res.json()

    def get_sent(self,url,header,data=None):
        res = None
        if header !="":
            res = requests.get(url=url,params=data,headers=header,verify=False)
            # print res.status_code
        else:
            res = requests.get(url=url,params=data,verify=False)
        # res = requests.get(url=url,headers=header,params=data)
        return res.json()
    def run_main(self,method,url,header=None,data=None):

        res = None
        if method =="post":
            res = self.post_main(url,header,data)
        else:
            res = self.get_sent(url,header,data)
            # print res.json()
        # return res
        # return json.loads(res)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
if __name__ =="__main__":
    a =RunMethod()
    url = 'http://47.97.208.158:8095/oto/pay/commit'
    data = {"orderNo":"263924429134192640","payMethod":1,"payScene":"wap","returnUrl":"http://xyt.trtpfbdfzs.kevglt","source":"wap"}
    # data = {"fromStation":"hangzhou","toStation":"beijing","searchType":"0","trainDate":"20190228","ticketType":"1"}
    header = {"Authorization": "6BLPrhxJ4HTPaXCOgH12XvwE8t+o1YYtGkcP2oXe0jaaBqubl3PL0+8zj7ac0925lGPxYBrBU/CkiWYueZLVZabwPrMnBQ+Wd3IKIuVeALw0AyMmef8kS8VYE1AKJkwAyLhISqntS8gXnYMHhyblsr9qHSCfz6/RICGDQriTwHLDQ0//51OAp0FizZF4SDMuDWME72DyZWB3ZgRgJk+Big","Content-Type":"application/json"}
    method= "post"
    # print type(url)
    # print type(data)
    # print type(header)
    # print type(method)
    print a.run_main(method,url,header,data)
