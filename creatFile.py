#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import time as t
from os import path

def createFile(dest):
	

    # 먼저 time 라이브러리를 통하여 시간정보를 불러온다. 
    # 그후 파일명으로 시간정보를 이용한다.
    # 조건문을 통하여 파일이 이미 존재하지 않으면 타임벙보를 이름으로 텍스트 파일을 만든다.




	date = t.localtime(t.time())

	## FileName = Month_Day_Year
	name = '%d_%d_%d.txt'%(date[1],date[2],(date[0]% 100))

	if not (path.isfile(dest + name)):
		f = open(dest + name, 'w')
		f.write('동해물과 백드산이 음하하하 \n'*30)
		f.close()

if __name__ == '__main__':
	destination = '/home/jake/python_programs/'
	createFile(destination)
	raw_input("done!!!!")