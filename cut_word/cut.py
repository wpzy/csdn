#coding:utf-8
import sys
import os
import jieba

file1=open('cut_word1.txt','w')
file2=open('cut_word2.txt','w')

dict_add=open('add_dict_word.txt')
stop_file=open('stopword.txt')
stop={}
for i in stop_file.readlines():
	if len(i)<=0:
		continue
	i=i.strip()
	stop[i]=1
d={}
for i in dict_add.readlines():
	if len(i)<=0:
		continue
	i=i.strip()
	d[i]=1
for i in d.keys():
	jieba.add_word(i,10)
jieba.enable_parallel()
for line in sys.stdin:
	if len(line)<=0:
		continue
	line=line.strip()
	t=jieba.cut(line[8:])
	output1=line[:8]
	output2=line[:8]
	for i in t:
		i=i.encode('utf-8').decode('utf-8')
		if len(i)<=1:
			continue
		elif stop.get(i.encode('utf-8'),-1)!=-1:
			continue
		else:
			output1=output1+'#!#'+i.encode('utf-8')
			output2=output2+'\t'+i.encode('utf-8')
	print >>file1,output1
	print >>file2,output2
