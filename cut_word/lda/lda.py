#coding:utf-8
import sys
import os
import codecs
import re
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora,models 
for line in sys.stdin:
	if len(line)<=0:
		continue
	line=line.strip()
	tmp=re.split(r'\s',line)
	if len(tmp)<=0:
		continue
	a=[]
	nums={}
	for i in tmp:
		a.append([i])
		if nums.get(i,-1)==-1:
			nums[i]=1
		else:
			nums[i]+=1
	dict=corpora.Dictionary(a)
	corpus=[dict.doc2bow(text) for text in a]
	lda=LdaModel(corpus=corpus,id2word=dict,num_topics=5,alpha='auto')
	for i in lda.show_topics():
		for j in i[1].encode('utf-8').split(' + '):
			j=j.replace('"','')
			ww,vv=j.split('*')
			nums_w=nums[vv]
			print '%s\t%s\t%s\t%s' %(tmp[0],vv,ww,nums_w)

