#coding:utf-8
import sys
import os
import gensim
import logging
k=0
logging.basicConfig(filename='logger.log', level=logging.WARNING)
model = gensim.models.KeyedVectors.load_word2vec_format("vector2", binary=False)
for line in sys.stdin:
	if len(line)<=0:
		continue
	line=line.strip()
	k+=1
	if k%2000==0:
		logging.info('+2K')
	tmp=line.split('\t')
	if len(tmp)!=2:
		continue
	try:
		re=model.most_similar(tmp[0])
	except KeyError:
		continue
	print tmp[0]
	for i in re:
		print '\t%s' %(i[0].encode('utf-8'))
