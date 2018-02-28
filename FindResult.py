#/usr/bin/env python
#coding=utf8
import requests
import sys,re,os
reload(sys)
sys.setdefaultencoding('utf-8')
import requests.packages.urllib3.util.ssl_

def FindShowBaidu(str):
#    str_temp = ''
#    index = 0
#    lines = re.split(r'[\r\n]+',str)
#    for line in lines:
#        index += 1
#        if index < 3:
#            str_temp = str_temp + line
#        else:
#            break
#    print str_temp

#    x = re.findall(r'^(.*)1',str,re.S|re.M)
#    if len(x):
#        str_temp = x[0]
    titleRe = '['+ '题'.decode('utf-8') +'|' + '第'.decode('utf-8') + ']'
    hasTitle = re.findall(titleRe,str,re.S|re.M);
    if (hasTitle):
        if len(hasTitle):
            return

    items = []
    lines = re.split(r'[\r\n]+',str)
    str_temp = ''
    if len(lines)>2:
        str_temp = str_temp + lines[0] + lines[1]


    isRight = True
    titleRe = '['+ '没有'.decode('utf-8') +'|' + '不'.decode('utf-8') + '|' + '错误'.decode('utf-8') + ']'
    hasTitle = re.findall(titleRe,str_temp,re.S|re.M);
    if (hasTitle):
        if len(hasTitle):
            isRight = False


    if len(lines) > 4:
        for i in range(len(lines)-4,len(lines)):
            item = lines[i]
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
    urlStr = "http://www.baidu.com/s?wd=" + str_temp
    res = requests.get(urlStr)
    res.encoding = 'utf-8'
#    print res.text
#    f = open('Found.html','w')
#    f.write(res.text)
#    f.close()
#    os.system('open Found.html')

    lines = re.split(r'[\r\n]+',str)
    if len(lines) > 4:
        for i in range(len(lines)-5,len(lines)):
            item = lines[i]
            if item:
                x0 = re.findall(item,res.text,re.S|re.M)
                if x0:
                    print '+++++++++++++'
                    print item
                    print len(x0)
        print '***************\r\n\r\n'
'''    x0 = re.findall(r'1.?(.*)[\r\n]{0:3}2',str,re.S|re.M)
    x1 = re.findall(r'2.?(.*)\r?\n?3',str,re.S|re.M)
    x2 = re.findall(r'3.?(.*)\r?\n?4',str,re.S|re.M)
    x3 = re.findall(r'4.?(.*)\r?\n?',str,re.S|re.M)


    print x0[0];
    print x1[0];
    print x2[0];
    print x3[0];

    if len(x0) > 0:
        t0 = re.findall(x0[0],res.text,re.S|re.M)
        if len(t0):
            print t0[0].decode('utf-8')

    if len(x1) > 0:
        t1 = re.findall(x1[0],res.text,re.S|re.M)
        if len(t1):
            print t1[0].decode('utf-8')'''

def FindShowBaiduFromXiGua(str):
        str_temp = ''
        question = ''
        index = 0
        lines = re.split(r'\r\n',str)
        head = lines[0]
        head_res = re.findall(r'\d*',head,re.S|re.M)
        t0 = lines[1];
        t0_res = re.findall(r'[\d\.]+(.*)',t0,re.S|re.M)
        if t0_res:
            pass
        else:
            return
        if t0_res[0]:
            t0_hasTail = re.findall(r'\?',t0_res[0],re.S|re.M)
            if t0_hasTail:
                question = t0_res[0]
            else:
                question = t0_res[0] + lines[2]
            print '################################'
            print question
            print '################################'

        isRight = True
        titleRe = '['+ '没有'.decode('utf-8') +'|' + '不'.decode('utf-8') + '|' + '错误'.decode('utf-8') + ']'
        hasTitle = re.findall(titleRe,question,re.S|re.M);
        if (hasTitle):
            if len(hasTitle):
                isRight = False
        if isRight is False:
            print '\r\n**否定**\r\n'

        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
#        urlStr = "http://wap.baidu.com/s?word=" + question
        urlStr = "http://www.baidu.com/s?wd=" + question
        res = requests.get(urlStr)

        res.encoding = 'utf-8'
        f = open('Found.html','w')
        f.write(res.text)
        f.close()
        os.system('open Found.html')

        anwser=[]
        j = 0
        for i in range(0,len(lines)):
            line = lines[len(lines)-i - 1]
            if  line == '':
                continue
            anCount = re.findall(line,res.text,re.S|re.M)
            an = (line,len(anCount))
            anwser.insert(0,an)
            j = j + 1
            if j > 2:
                break
        sorted(anwser,reverse = isRight)#逆转

        for an,count in anwser:
            print '--------------'
            print an
            print count
        print '*****************************'






#        for line in lines:
#            index += 1
#            if index < 3:
#                str_temp = str_temp + line
#            else:
#                break
#        print str_temp
#
#        x = re.findall(r'^(.*)1',str,re.S|re.M)
#        if len(x):
#            str_temp = x[0]

if __name__ == '__main__':
#    FindShowBaidu('今日股票\r\n'.decode('utf-8'))
    FindShowBaiduFromXiGua('」登对一题也能分钱?\r\nS全新玩法火热上线!O\r\ncct"9表示?\r\n安全入口\r\n安全出口\r\n停车场\r\n'.decode('utf-8'))
#    FindShowBaidu('下面那种食物不能生吃\r\n 1.土豆\r\n 2.西红柿\r\n 3.黄瓜\r\n 4.辣椒\r\n'.decode('utf-8'))

#    x0 = u'土豆'
#    x1 = u'冬瓜'
#    x2 = u'西红柿'
#    x3 = u'黄瓜'
#    t0 = re.findall(x0,res.text,re.S|re.M)
#    t1 = re.findall(x1,res.text,re.S|re.M)
#    t2 = re.findall(x2,res.text,re.S|re.M)
#    t3 = re.findall(x3,res.text,re.S|re.M)
#    print x0.decode('utf-8') + str(len(t0))
#    print x1.decode('utf-8') + str(len(t1))
#    print x2.decode('utf-8') + str(len(t2))
#    print x3.decode('utf-8') + str(len(t3))


