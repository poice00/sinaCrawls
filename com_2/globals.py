#coding: utf-8
'''
Created on 2016年8月2日

@author: ssy110
'''
import mysql.connector
next_cursor=''
conn=mysql.connector.connect(host='192.168.1.96',user='root',passwd='123',db='weibodatabase',port=3306,charset='utf8')