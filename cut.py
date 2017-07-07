#coding:utf-8
import sys
import os
import re
import jieba
file=open('stopword.txt')
data=file.readlines()
dict={}
for i in data:
	if len(i)<=0:
		continue
	i=i.strip()
	try:
		i=i.decode('utf-8').encode('utf-8')
	except UnicodeError:
		continue
	dict[i]=1
for line in sys.stdin:
	if len(line)<=0:
		continue
	line=line.strip()
	label=line[:8]
	content=line[8:]
	seg_list = jieba.cut_for_search(content)
	sentence=''
	for i in seg_list:
		i=i.encode('utf-8')
		if dict.get(i,-1)!=-1:
			continue
		else:
			sentence=sentence+'\t'+i
	print '%s\t%s' %(label,sentence)
