#coding:utf-8
import sys
import os
import re
for line in sys.stdin:
	if len(line)<=0:
		continue
	line=line.strip()
	print line.decode('gbk').encode('utf-8')
