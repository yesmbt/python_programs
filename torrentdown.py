#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib2
import re
import os
import codecs

plists = ["백종원의 3대천왕", "접속 무비월드", "영화가 좋다", "신서유기 2","김제동의 톡투유", "엄마가 뭐길래", "유희열의 스케치북", "일밤 2부 진짜 사나이", "속풀이쇼 동치미", "그것이 알고 싶다", "무한도전", "썰전", "강적들", "라디오스타", \
 "차이나는 도올", "최고의 사랑", "복면가왕", "무비월드", "영화가 좋다", "애니월드", "섹션 TV 연예통신", "쿡가대표", "JTBC 냉장고를 부탁해", "해피 투게더", "대박", \
 "JTBC 김제동의 톡투유", "힐링캠프", "개그 콘서트", "황금어장", "맛있는 녀석들", "수요미식회", "그것이 알고싶다", "슈퍼맨이 돌아왔다", "디어 마이 프렌즈", "비정상회담", \
 "옥중화", "불타는 청춘", "뮤비뱅크", "스페이스 공감"]

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
content = opener.open('https://torrentkim3.net/bbs/s.php?k=720p-NEXT&b=&q=').read()
# content = opener.open('https://torrentkim3.net/bbs/rss.php?k=HDTV.H264.720p+WITH&b=').read()
SERVER = 'localhost:9091 -n transmission:hannara'
# transmission-remote $SERVER --torrent
for m in re.finditer("<a href='\.\.\/torrent_(.*?).html.*?>\s*(.*?\..*?)[\s+|\.].*?<\/a>.*?<td class=\"hit\">(.*?)<", content, re.S):
# for m in re.finditer("torrent_variety\/(\d*).html'>(.*?)<", content, re.S):
    torrentUrl = 'https://torrentkim3.net/torrent_%s.html' % m.group(1)
    torrentDetail = opener.open(torrentUrl).read()
    goodCount = re.search('추 천\((.*?)\)', torrentDetail)
    badCount = re.search('불량신고\((.*?)\)', torrentDetail)
    magNet = re.search("value=\'magnet:(.*?)\'", torrentDetail)
    magnetlink = 'magnet:%s' % magNet.group(1)

############################################################################################

    
    print '#################################################################################'
    path = m.group(1)
    print path
    pname = m.group(2)
    print pname
    print magnetlink
    gcount = goodCount.group(1)
    print 'goodCount= ' + gcount
    fsize = m.group(3)
    print fsize[:-2]
    print "love you"
    # print plist1

    # break

#     plist = codecs.open('/home/jake/python_programs/programList.txt', encoding="utf-8")
#     plists = plist.readlines()
#     plists1 = []
#     plists1 = [el.replace('\n', '') for el in plists]
#     print plists1.decode("UTF-8").encode("UTF-8")
    dlist = open('/home/jake/python_programs/downloaded.txt', 'r')
    dlists = dlist.readlines()
    if (any(pl in pname for pl in plists) and gcount > 0 and 1 < float(fsize[:-2]) < 2.5):
        if pname not in open('/home/jake/python_programs/downloaded.txt').read():
            os.system("transmission-remote %s --add %s" % (SERVER, magnetlink))
            fob = open('/home/jake/python_programs/downloaded.txt', 'a')
            fob.write(pname + '\n')
            fob.close()
            print '#############################################################################'
    # plist.close()
    dlist.close()

    # if ( any( t in m.group(2) for t in plist1.splitlines() ) and goodCount.group(1) > 0 and 1 < float(m.group(3)[:-2]) < 2.5 ):
    #     if m.group(2) not in open('/home/jake/python_programs/downloaded.txt').read():
    #         os.system("transmission-remote %s --add %s" % (SERVER, magnetlink))
    #         fob = open('/home/jake/python_programs/downloaded.txt', 'a')
    #         fob.write(m.group(2)+'\n')
    #         fob.close()
    #         print '#############################################################################'

