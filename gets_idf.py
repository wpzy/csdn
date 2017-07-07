#coding:utf-8
import sys
import os
import re
import math
dict={}
nums_line=0
for line in sys.stdin:
	if len(line)<=0:
		continue
	line=line.strip()
	nums_line+=1
	tmp=re.split(r'\s',line)
	d={}
	for i in tmp:
		if d.get(i,-1)==-1:
			if dict.get(i,-1)==-1:
				dict[i]=1
				d[i]=1
			else:
				dict[i]+=1
				d[i]=1
		else:
			continue
for i in dict.keys():
	 nums_word=float(dict[i])
	 idf=float(math.log(nums_line/(nums_word+1)))
	 print '%s\t%s' %(i,idf)
