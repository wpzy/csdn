#coding:utf-8
import sys
import os
for line in sys.stdin:
	if len(line)<=0:
		continue
	line=line.strip()
	tmp=line.split('\001')
	for i in tmp[1:]:
		print i
	
