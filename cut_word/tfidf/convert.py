#coding:utf-8
import sys
import os
import re
for line in sys.stdin:
	if len(line)<=0:
		continue
	line=line.strip()
	tmp=line.split('\t')
	if len(tmp)!=2:
		continue
	l=tmp[0]+' '+tmp[1]
	t=re.split(r'\s',l)
	if len(t)!=2:
		continue
	w,v=l.strip().split(' ')
	print '%s %s' %(w.decode('utf-8').encode('utf-8'),v)
