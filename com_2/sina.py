#coding: utf-8
'''
Created on 2016年7月24日

@author: Administrator
'''
import requests,re,util,globals,time,datetime
def getdata():
#     cookies = open('cookie4').readline()#
    cookies = open('cookie4-1').readline()#
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
               'cookie': cookies
    }
    data={
          'containerid' :'2305301008080f2b0e1930f5b30eae8d2b95f3c58232__timeline__mobile_guide_-_pageapp:23055763d3d983819d66869c27ae8da86cb176',
        #  'uid' :'5516440808'#听心跳的声音
          'uid' :'5621836332'#李宏
    }
    url='http://m.weibo.cn/p/index'
    html = requests.get(url,headers=headers,params=data ,timeout=3)
    reg0=r'"next_cursor":"(.+?)","loadMore".+?"'#获取next_cursor的reg
    next_cursorList = re.findall(reg0, html.text, re.S)
    globals.next_cursor = next_cursorList[0].replace('\\','')
    reg=r'"user":{"id":(.+?),.+?"created_timestamp":(.+?),"bid":"(.+?)",'
    dataList = re.findall(reg, html.text, re.S)
    for data in dataList:
        print '.....................'
        print '用户id: ',data[0]
        print '个人主页profile_url: ','/u/'+data[0]
        print '创建时间created_timestamp: ',data[1],util.timestamp2string(float(data[1]))
        print '帖子主键bid: ',data[2]    
        print 'mid: ',data[1]+'/'+data[2]
        #writer(data,'D:/eclipse_workspace/Crawls/com_2/data')
        try:
            dateString = util.timestamp2string(float(data[1]))
            postTime = datetime.datetime.strptime(dateString,'%Y-%m-%d %H:%M:%S')
            params = (data[2],postTime,data[0])
            util.saveOrigindata(params,globals.conn)
        except Exception,e:
            print 'saveOrigindata-failed!..','exception is: ',e
def getPagedata(page):
#     cookies = open('cookie5').readline()
    cookies = open('cookie5-1').readline()
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
               'cookie': cookies
    }
    data={
          'containerid' :'2305301008080f2b0e1930f5b30eae8d2b95f3c58232__timeline__mobile_guide_-_pageapp:23055763d3d983819d66869c27ae8da86cb176',
          'page': page,
          #'uid':'5516440808',
          'uid':'5621836332',
          'next_cursor':globals.next_cursor
    }
    url='http://m.weibo.cn/page/pageJson'
    html = requests.get(url,headers=headers,params=data ,timeout=10)
    reg0=r'"next_cursor":"(.+?)"}'#获取next_cursor的reg
    next_cursorList = re.findall(reg0, html.text, re.S)
    globals.next_cursor = next_cursorList[0].replace('\\','')
    reg=r'"user":{"id":(.+?),.+?"created_timestamp":(.+?),"bid":"(.+?)",'
    dataList = re.findall(reg, html.text, re.S)
    for data in dataList:
        print '.....................'
        print '用户id: ',data[0]
        print '个人主页profile_url: ','/u/'+data[0]
        print '创建时间created_timestamp: ',data[1],util.timestamp2string(float(data[1]))
        print '帖子主键bid: ',data[2]    
        print 'mid: ',data[1]+'/'+data[2]   
        #writer(data,'D:/eclipse_workspace/Crawls/com_2/data') 
        try:
            dateString = util.timestamp2string(float(data[1]))
            postTime = datetime.datetime.strptime(dateString,'%Y-%m-%d %H:%M:%S')
            params = (data[2],postTime,data[0])
            util.saveOrigindata(params,globals.conn)
        except Exception,e:
            print 'saveOrigindata-failed!..','exception is: ',e
def writer(data,path):
    f=open(path,'a')  
    f.write('...................\n')
    f.write('用户id: '+data[0]+'\n')
    f.write('创建时间: '+util.timestamp2string(float(data[1]))+'\n')
    f.write('帖子id: '+data[2]+'\n')
    f.close()
if __name__ == '__main__':
    #The start time 
    start = time.clock()
    getdata()
    print '=================='
    for i in range(2,2000):
        print '=====第',i,'次出发======='
        try:
            getPagedata(i)
        except Exception,e:
            print 'failed!..','exception is: ',e
    end = time.clock()
    print("The function run time is : %.03f seconds" %(end-start))
    
    
    
    
    
    
    
