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
	print len(tmp)
	for i in tmp:
		a.append([i])
	dict=corpora.Dictionary(a)
	corpus=[dict.doc2bow(text) for text in a]
	lda=LdaModel(corpus=corpus,id2word=dict,num_topics=3,alpha='auto')
	for i in lda.show_topics():
		print i[0]
		print i[1].encode('utf-8')
