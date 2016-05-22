#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib2
import re
import os

def main():
	file = open("programList.txt","r")
	flists = file.readlines()
	a = "엄마가 뭐길래 love love"
	print any(flist in a for flist in ["엄마가 뭐길래","그것이 알고싶다"])
	if any(flist in a for flist in flists):
		print "Yes it's in it!!"
	else:
		print "It's not here!"
	file.close()

if __name__ == '__main__':
	main()
