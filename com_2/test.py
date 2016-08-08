#coding: utf-8
'''
Created on 2016年8月3日

@author: ssy110
'''
import util,globals
if __name__ == '__main__':
    #print '\u963f\u5b81\u7684\u5c0f\u8774\u8776'.decode('unicode-escape')
#     rows = util.selectFromOrigindata(globals.conn)
#     for row in rows:
#         print row[0],row[1],row[2],row[3]
#     row = util.getByMid('E1zIW2nhQ', globals.conn)
#     print row[0],row[1],row[2],row[3]
    a = 3;
    try:
        for i in range(10):
            for j in range(10):
                print j
                if j==2:
                    raise Exception("break")
    except:
        pass