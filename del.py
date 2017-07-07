#coding:utf-8
import sys
import os
import re
for line in sys.stdin:
	if len(line)<=0:
		continue
	line=line.strip()
	line=line.decode('utf-8')
	tmp=line.strip().split(' ')
	if len(tmp)==2:
		print line.encode('utf-8')
