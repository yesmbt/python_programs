#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib2
import re
import os

plist = open('/home/jake/python_programs/programList.txt', 'r')
lines = plist.read()


opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
content = opener.open('https://torrentkim3.net/bbs/popular.html').read()
# content = opener.open('https://torrentkim3.net/bbs/rss.php?k=HDTV.H264.720p+WITH&b=').read()
SERVER = 'localhost:9091 -n transmission:hannara'
# transmission-remote $SERVER --torrent

for m in re.finditer("/torrent_(.*?).html'>(.*?)</a><br>", content, re.S):
# for m in re.finditer("/torrent_(.*?).html'>(.*?)</a><br>", content, re.S):
# for m in re.finditer("torrent_variety\/(\d*).html'>(.*?)<", content, re.S):

    torrentUrl = 'https://torrentkim3.net/torrent_%s.html' % m.group(1)
    torrentDetail = opener.open(torrentUrl).read()
    goodCount = re.search('추 천\((.*?)\)', torrentDetail)
    badCount = re.search('불량신고\((.*?)\)', torrentDetail)
    magNet = re.search("value=\'magnet:(.*?)\'", torrentDetail)
    # filesize = re.search("파일크기: (.*?) ", torrentDetail)
    if magNet is not None:
        magnetlink = 'magnet:%s' % magNet.group(1)
        print magnetlink

############################################################################################

    
        print '#################################################################################'
        print m.group(1)
        mtype = re.sub('/\d+','',m.group(1))
        print mtype
        if mtype == 'mid':
            break
        
        fname = re.sub(r'^\s','',m.group(2))
        fname = re.sub(r'(.*?[e|E]\d+)\.*?',$1 ,fname)
        print fname
        print 'goodCount= ' + goodCount.group(1)
        # print m.group(3)
        # print filesize.group(1)
        print "love you"
        print '#################################################################################'


    # break

        if any( t in fname for t in lines.splitlines() ):
            if fname not in open('/home/jake/python_programs/downloaded.txt').read():
                os.system("transmission-remote %s --add %s" % (SERVER, magnetlink))
                fob = open('/home/jake/python_programs/downloaded.txt', 'a')
                fob.write(m.group(2)+'\n')
                fob.close()
                print '#############################################################################'

    # if ( any( t in m.group(2) for t in plist1.splitlines() ) and goodCount.group(1) > 0 and 1 < float(m.group(3)[:-2]) < 2.5 ):
    #     if m.group(2) not in open('/home/jake/python_programs/downloaded.txt').read():
    #         os.system("transmission-remote %s --add %s" % (SERVER, magnetlink))
    #         fob = open('/home/jake/python_programs/downloaded.txt', 'a')
    #         fob.write(m.group(2)+'\n')
    #         fob.close()
    #         print '#############################################################################'

plist.close()
