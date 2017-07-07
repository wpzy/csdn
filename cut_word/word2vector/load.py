#coding:utf-8
import sys
import os
import gensim
import logging
import pickle
k=0
dict={}
logging.basicConfig(filename='logger.log', level=logging.WARNING)
model = gensim.models.KeyedVectors.load_word2vec_format("vector", binary=False)
for line in sys.stdin:
	if len(line)<=0:
		continue
	line=line.strip()
	print line
	try:
		re=model.most_similar(line,topn=10)
	except KeyError:
		continue
	print len(re)
	result=[]
	for i in re:
		t=[i[0].encode('utf-8'),i[1]]
		result.append(t)
	dict[line]=result
#pickle.dump(dict,open('result.txt','w'))
