# coding:utf-8
# coding:utf-8
import requests
import json
class RunMethod:
    def post_main(self,url,data):
        # res =None
        header = str("Authorization':'N5drNRtp8cHg9aqpfaEk/zQfivlEUKwJCYPHBjTV6Gk=','Content-Type':'application/json")
        # if headers !="":
        res = requests.post(url=url,data=data,headers=header).json()
        # else:
        #     res = requests.post(url=url,data=data).json()
        return res

    def get_sent(self,url,data=None):
        # if header !="":
        header = str("Authorization':'N5drNRtp8cHg9aqpfaEk/zQfivlEUKwJCYPHBjTV6Gk=','Content-Type':'application/json")
        res = requests.get(url=url,data=data,headers=header).json()
        # else:
        #     res = requests.get(url=url,data=data).json()
        # res = requests.get(url=url,data=data,headers=header).json()
        return res
    def run_main(self,method,url,data=None):
        res = None
        if method =="post":
            res = self.post_main(url,data)
        else:
            res = self.get_sent(url,data)
        return res
if __name__ =="__main__":
    a =RunMethod()
    url = 'http://dev.lvtudiandian.com/train-tickets/api/ticket/train/hotCity'
    # data = {"openid":'1'}
    header={'Authorization':'N5drNRtp8cHg9aqpfaEk/zQfivlEUKwJCYPHBjTV6Gk=','Content-Type':'application/json'}

    print a.run_main("get",url)