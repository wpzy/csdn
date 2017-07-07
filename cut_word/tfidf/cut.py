#coding:utf-8
import sys
import os
import jieba
import jieba.analyse

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
jieba.enable_parallel(10)
jieba.analyse.set_idf_path('idf.txt')
jieba.analyse.set_stop_words('stopword.txt')
for line in sys.stdin:
	if len(line)<=0:
		continue
	line=line.strip()
	length=len(line)
	output=line[:8]
	tmp=line.split('\001')
	title=jieba.cut(tmp[1])
	title_d={}
	for i in title:
		if stop.get(i,-1)==-1 and len(i)>=2:
			title_d[i.encode('utf-8')]=1
			print '%s\t%s' %(output,i.encode('utf-8'))
	for w,v in jieba.analyse.extract_tags(line[8:], topK=10, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v')):
		if title_d.get(w.encode('utf-8'),-1)!=-1:
			idx=line.find(w.encode('utf-8'))
			if float(idx)/length<=0.2:
				print '%s\t%s\t%s\t%s\t%s\t%s' %(output,w.encode('utf-8'),v,'***','1','1')
			else:
				print '%s\t%s\t%s\t%s\t%s\t%s' %(output,w.encode('utf-8'),v,'***','1','0')
		else:
			idx=line.find(w.encode('utf-8'))
			if float(idx)/length<=0.2:
				print '%s\t%s\t%s\t%s\t%s\t%s' %(output,w.encode('utf-8'),v,'***','0','1')
			else:
				print '%s\t%s\t%s\t%s\t%s\t%s' %(output,w.encode('utf-8'),v,'***','0','0')


	for w,v in jieba.analyse.textrank(line[8:], topK=10, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'    )):
		if title_d.get(w.encode('utf-8'),-1)!=-1:
			idx=line.find(w.encode('utf-8'))
			if float(idx)/length<=0.2:
				print '%s\t%s\t%s\t%s\t%s\t%s' %(output,w.encode('utf-8'),'***',v,'1','1')
			else:
				print '%s\t%s\t%s\t%s\t%s\t%s' %(output,w.encode('utf-8'),'***',v,'1','0')
		else:
			idx=line.find(w.encode('utf-8'))
			if float(idx)/length<=0.2:
				print '%s\t%s\t%s\t%s\t%s\t%s' %(output,w.encode('utf-8'),'***',v,'0','1')
			else:
				print '%s\t%s\t%s\t%s\t%s\t%s' %(output,w.encode('utf-8'),'***',v,'0','0')
