#coding: utf-8
'''
Created on 2016年8月2日

@author: ssy110
'''
import requests,re,util,globals,time,datetime
def getFromMid1(url):
    cookies = open('user5').readline()#
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
               'cookie': cookies
    }
    html = requests.get(url,headers=headers,timeout=1)
    reg=r'"text".+?a>(.+?)",.+?h5icon.+?reposts_count":(.+?),"comments_count":(.+?),"attitudes_count":(.+?),.+?"created_timestamp":(.+?),.+?mid":"(.+?)",'
    dataList = re.findall(reg, html.text, re.S)
    return dataList
#     for data in dataList:
#         print 'weibo-text:',data[0].decode('unicode-escape')
#         print 'reposts_count: ',data[1]
#         print 'comments_count: ',data[2]
#         print 'attitudes_count: ',data[3]
#         print 'created_timestamp: ',util.timestamp2string(float(data[4]))
#         print 'mid: ',data[5]  
#         print 'uid: ',url.split("/")[-2]  
#         print 'bid: ',url.split("/")[-1] 
def getFromMid2(url):
    cookies = open('user5').readline()#
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
               'cookie': cookies
    }
    html = requests.get(url,headers=headers,timeout=1)
    reg=r'<span class="time">(.+?)</span>.+?class="weibo-text".+?/a>(.+?)</div>.+?<span node-type="zfCount">(.+?)</span>.+?<span node-type="cmtCount">(.+?)</span>.+?<i node-type="zanCount">(.+?)</i>.+?"mid":"(.+?)"}'
    dataList = re.findall(reg, html.text, re.S)
    return dataList
#     for data in dataList:
#         print '.....................'
#         print 'created_timestamp: ',data[0]
#         print 'weibo-text: ',data[1]
#         print 'reposts_count: ',data[2]
#         print 'comments_count: ',data[3]
#         print 'attitudes_count: ',data[4]  
#         print 'mid: ',data[5]  
#         print 'uid: ',url.split("/")[-2]  
#         print 'bid: ',url.split("/")[-1]  
#         #writer(data,'D:/eclipse_workspace/Crawls/com_2/data')
def getFromUid(url):
    cookies = open('user5').readline()#
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
               'cookie': cookies
    }
    html = requests.get(url,headers=headers,timeout=1)
    reg=r'h5icon.+?id":"(.+?)",.+?"attNum":"(.+?)",.+?"mblogNum":"(.+?)","fansNum":"(.+?)",.+?"name":"(.+?)",.+?"mbrank":"(.+?)",'
    dataList = re.findall(reg, html.text, re.S)
#     for data in dataList:
#         print '.....................'
#         print 'id: ',data[0]
#         print 'attNum: ',data[1]
#         print 'mblogNum: ',data[2]
#         print 'fansNum: ',data[3]    
#         print 'name: ',data[4].decode('unicode-escape') 
#         print 'mbrank: ',data[5]  
    return dataList
if __name__ == '__main__':
    baseurl = 'http://m.weibo.cn/'
    #dataList=open('zsina','r').readlines()
    datalist = util.selectFromOrigindata(globals.conn)
    for data in datalist:
        print '.................'
        authorUrl = baseurl + 'u/' + data[2];
        blogUrl = baseurl + data[2] + '/' + data[0]
        print authorUrl,blogUrl,data[1]
        try:
            userList = getFromUid(authorUrl)
            if(userList):
                for user in userList:#id,attnum,mblogNum,mbrank,name
                    try:
                        params = (user[0],user[1],user[2],user[3],user[4].decode('unicode-escape') ,user[5])
                        util.saveUser(params,globals.conn)
                    except Exception,e:
                        print 'saveUser-failed!..','exception is: ',e
            else:
                print 'user not exist!'
            blogList = getFromMid1(blogUrl)
            if(blogList):
                for blog in blogList:#id,attnum,mblogNum,mbrank,name
                    try:
                        params = (blog[0].decode('unicode-escape'),blog[1],blog[2],blog[3],util.timestamp2string(float(blog[4])),blog[5],blogUrl.split("/")[-2],blogUrl.split("/")[-1])
                        util.saveBlog(params,globals.conn)
                        util.changeStateToYes(data[0], globals.conn)
                    except Exception,e:
                        print 'saveBlog-failed!..','exception is: ',e
            elif(getFromMid2(blogUrl)):
                blogList2 = getFromMid2(blogUrl)
                for blog in blogList2:#id,attnum,mblogNum,mbrank,name
                    try:
                        params = (blog[1],blog[2],blog[3],blog[4],blog[0],blog[5],blogUrl.split("/")[-2],blogUrl.split("/")[-1])
                        util.saveBlog(params,globals.conn)
                        util.changeStateToYes(data[0], globals.conn)
                    except Exception,e:
                        print 'saveBlog-failed!..','exception is: ',e
            else:
                print 'not exist！'#http://m.weibo.cn/5886575504/E1I7E1S4S
        except Exception,e:
            print 'sfailed!..','exception is: ',e
    