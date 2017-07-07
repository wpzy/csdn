import jieba
import sys
import os
import re
import jieba.posseg
import jieba.analyse

jieba.analyse.set_idf_path('/search/odin/wupei/lda/idf.txt')
for line in sys.stdin:
	if len(line)<=0:
		continue
	line=line.strip()
	id=line[:8]
	print id
	print 'tfidf:'
	for x,w in jieba.analyse.extract_tags(line[8:],topK=20, withWeight=True):
		print '\t%s\t%s' %(x.encode('utf-8'),w) 
	print 'textrank:'
	for x,w in jieba.analyse.textrank(line[8:],topK=20,withWeight=True):
		print '\t%s\t%s' %(x.encode('utf-8'),w) 

