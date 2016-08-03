#coding: utf-8
'''
Created on 2016年8月1日

@author: ssy110
'''
import datetime,time
def string2timestamp(strValue):  
    try:          
        d = datetime.datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S.%f")  
        t = d.timetuple()  
        timeStamp = int(time.mktime(t))  
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond))/1000000  
        return timeStamp  
    except ValueError as e:  
        print e  
def timestamp2string(timeStamp):  
    try:  
        d = datetime.datetime.fromtimestamp(timeStamp)  
#         str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")  
        str1 = d.strftime("%Y-%m-%d %H:%M:%S")  
        # 2015-08-28 16:43:37.283000'  
        return str1  
    except Exception as e:  
        print e  
def saveOrigindata(params,conn):
    cur=conn.cursor()
    sql = "insert into origindata(mid,postTime,uid)\
             values(%s,%s,%s)" 
    #保存数据库
    cur.execute(sql,params)
    conn.commit()
    print '数据库插入成功 =====================================================saveOrigindata!'
    cur.close()
#if __name__ == '__main__':
    #print timestamp2string(1470026978)#1470026978 
    #print string2timestamp('2016-08-01 12:49:38.000000')#2016-08-01 12:49:38.000000
    