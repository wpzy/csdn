#coding:utf-8
import sys
import os
import logging
import multiprocessing

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
if __name__=='__main__':
	program=os.path.basename(sys.argv[0])
	logger=logging.getLogger(program)

	logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
	logging.root.setLevel(level=logging.INFO)
	logger.info("running %s" %' '.join(sys.argv))
	if len(sys.argv)<4:
		print globals()['__doc__'] % locals()
		sys.exit()
	inp,outp1,outp2=sys.argv[1:4]
	model=Word2Vec(LineSentence(inp),size=400,window=5,min_count=5,workers=multiprocessing.cpu_count())
	model.save(outp1)
	model.wv.save_word2vec_format(outp2,binary=False)
