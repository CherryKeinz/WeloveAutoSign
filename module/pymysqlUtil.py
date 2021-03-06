# -*-coding:utf-8-*-

import json
import codecs
import sys
import pymysql


reload(sys)
sys.setdefaultencoding('utf-8')

# conn = pymysql.connect(host='192.168.1.101', port=3306, user='hhlt', passwd='hhlt', db='shuitu', charset='utf8')
class PymysqlUtil():
    #初始化方法
    def __init__(self,host,port,user,passwd,dbName,charsets):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.dbName = dbName
        self.charsets = charsets
    #链接数据库
    def getCon(self):
        self.db = pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.dbName,
            charset=self.charsets
        )
        self.cursor = self.db.cursor()
    #关闭链接
    def close(self):
        self.cursor.close()
        self.db.close()
    #查询单行记录
    def get_one(self,sql):
        res = None
        try:
            self.getCon()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
        except:
            print("查询失败!")
        return res
    #查询列表数据
    def get_all(self,sql):
        res = None
        try:
            self.getCon()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print("查询失败！")
        return res
    #插入数据
    def __insert(self,sql):
        count = 0
        try:
            self.getCon()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print("操作失败！")
            self.db.rollback()
        return count
    #修改数据
    def __edit(self,sql):
        return self.__insert(sql)
    #删除数据
    def __delete(self,sql):
        return self.__insert(sql)
    #更新数据
    def __update(self,sql):
        return self.__insert(sql)
