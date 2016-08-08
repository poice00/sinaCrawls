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
def saveUser(params,conn):
    cur=conn.cursor()
    sql = "insert into user(id,attnum,mblogNum,fansNum,name,mbrank)\
             values(%s,%s,%s,%s,%s,%s)" 
    #保存数据库
    cur.execute(sql,params)
    conn.commit()
    print '数据库插入成功 =====================================================saveUser!'
    cur.close()
def saveBlog(params,conn):#`mid``attitudesCount``bid``commentsCount``createdTime``repostsCount``weibotext``uid`
    cur=conn.cursor()
    sql = "insert into blog(weibotext,repostsCount,commentsCount,attitudesCount,createdTime,mid,uid,bid)\
             values(%s,%s,%s,%s,%s,%s,%s,%s)" 
    #保存数据库
    cur.execute(sql,params)
    conn.commit()
    print '数据库插入成功 =====================================================saveBlog!'
    cur.close()
def saveToRepoRelation(params,conn):#`mid``attitudesCount``bid``commentsCount``createdTime``repostsCount``weibotext``uid`
    cur=conn.cursor()
    sql = "insert into repostrelation(mid,uid,content)\
             values(%s,%s,%s)" 
    #保存数据库
    cur.execute(sql,params)
    conn.commit()
    print '数据库插入成功 ==========saveToRepoRelation!'
def saveToCommRelation(params,conn):#`mid``attitudesCount``bid``commentsCount``createdTime``repostsCount``weibotext``uid`
    cur=conn.cursor()
    sql = "insert into commentrelation(id,mid,uid,content)\
             values(%s,%s,%s,%s)" 
    #保存数据库
    cur.execute(sql,params)
    conn.commit()
    print '数据库插入成功 ==========saveToCommRelation!'
    cur.close()
def selectFromOrigindata(conn):
    cur=conn.cursor()
    sql = "select * from origindata where state='no' order by postTime DESC "
    #保存数据库
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    return rows
def selectFromOrigindata2(conn):
    cur=conn.cursor()
    sql = "select * from origindata where userstate='未处理' order by postTime DESC "
    #保存数据库
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    return rows
def getByMid(mid,conn):
    cur=conn.cursor()
    sql = "select * from origindata where mid='%s'"%mid
    #保存数据库
    cur.execute(sql)
    row= cur.fetchone()
    cur.close()
    return row
def changeStateToYes(mid,conn):
    cur=conn.cursor()
    sql = "UPDATE origindata SET state = 'yes' WHERE mid='%s'"%mid
    #保存数据库
    cur.execute(sql)
    conn.commit()
    print '状态更改成功 =====================================================state!'
    cur.close()
def changeStateTohandle(mid,conn):
    cur=conn.cursor()
    sql = "UPDATE origindata SET userstate='已处理' WHERE mid='%s'"%mid
    #保存数据库
    cur.execute(sql)
    conn.commit()
    print '状态更改成功 =====================================================state!'
def changeBlogStateTohandle(mid,conn):
    cur=conn.cursor()
    sql = "UPDATE blog SET state='已处理' WHERE mid='%s'"%mid
    #保存数据库
    cur.execute(sql)
    conn.commit()
    print '状态更改成功 =====================================================state!'
def changeBlogStateToNoHandle(mid,conn):
    cur=conn.cursor()
    sql = "UPDATE blog SET state='未处理' WHERE mid='%s'"%mid
    #保存数据库
    cur.execute(sql)
    conn.commit()
    print '状态更改成功 =====================================================state!'
    cur.close()
def changeStateToNone(mid,conn):
    cur=conn.cursor()
    sql = "UPDATE origindata SET state = 'none' WHERE mid='%s'"%mid
    #保存数据库
    cur.execute(sql)
    conn.commit()
    print '状态更改成功 =====================================================state!'
    cur.close()
def readBlogData(conn):
    cur=conn.cursor()
    sql = "select * from blog where state='未处理' order by createdTime DESC "
    #保存数据库
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    return rows
#if __name__ == '__main__':
    #print timestamp2string(1470026978)#1470026978 
    #print string2timestamp('2016-08-01 12:49:38.000000')#2016-08-01 12:49:38.000000
    