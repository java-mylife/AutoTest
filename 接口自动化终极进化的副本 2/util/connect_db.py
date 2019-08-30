# coding:utf-8
import pymysql
class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host = "120.27.244.111",
            port = 3306,
            user = "train_db",
            passwd = "123456",
            db = "train-ticket",
            charset = "utf8",)
        self.cur = self.conn.cursor()

    def serch_one(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return  result


if __name__ =="__main__":
    op_mysql = OperationMysql()
    res = op_mysql.serch_one("select * from ticket_order where id =14")
    print res
