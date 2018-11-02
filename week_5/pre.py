#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
"""This script extracts terms from a document"""
import re
import os
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

def preprocessing(filename):
	"""Read a file and preprocessing ,return a token list"""
	content = read_file(filename)
	token_list = tokenization(content)
	token_list = remove_stop_word(token_list)
	token_list = sorted(token_list)
	return token_list

def read_file(filename):
	"""Read the file of dictionary and return a string"""
	now_path = os.path.dirname(os.path.abspath(__file__))+'/'
	f_value = open(now_path + filename, 'r', encoding='UTF-8')
	content = f_value.read()
	f_value.close()
	return content


def addJiebaWordDic(filename):
	"""Read jieba word dict from file"""
	# read jieba word dict from file
	jiebaWordDict = read_file(filename)
	# split by \n
	jiebaWordDict = jiebaWordDict.split("\n")
	# remove empty item
	jiebaWordDict = list(filter(None, jiebaWordDict))
	# add word dict
	for word in jiebaWordDict:
		jieba.add_word(word, freq=None, tag=None)

def tokenization(content):
	"""Tokenization"""
	#remove \t\n\r\f\v
	content = re.sub('[\t\n\r\f\v]', '', content)
	#remove " "
	content = re.sub(' ', '', content)
	#remove "　"
	content = re.sub('　', '', content)
	#remove [a-zA-Z]
	content = re.sub('[a-zA-z]', '', content)
	#remove [0-9]
	content = re.sub('[0-9]', '', content)
	#remove punctuation marks -> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
	puncs = '，、：。～「」；？！「」『』—（）…－“–”〃〜─ㄧ＂︰％｢｣╱《》【】〔〕／•＋'
	content = re.sub('['+puncs+']', '', content)
	content = re.sub('['+string.punctuation+']', '', content)

	# to jieba word dict
	token_list = jieba.cut(content, cut_all=False)
	token_list = list(token_list)

	#remove empty item
	token_list = list(filter(None, token_list))

	return token_list


def remove_stop_word(token_list):
	"""remove stop word"""
	#Read Stop Word List
	stop_word_list = read_file('stop-word-list.txt')
	stop_word_list = stop_word_list.split('\n')
	#remove stop word from token_list
	token_list = [token for token in token_list if token not in stop_word_list]
	return token_list

def write_file(filename, token_list):
	"""write files"""
	now_path = os.path.dirname(os.path.abspath(__file__))+'/'
	print(now_path)
	f_value = open(now_path + filename, 'w', encoding='UTF-8')
	for token in token_list:
		f_value.write("%s\n" % token)
	f_value.close()


def main():
	"""main function"""
	addJiebaWordDic("jiebaWordDict.txt")
	token_list = preprocessing('附錄.txt')
	write_file('附錄dic''.txt', token_list)


if __name__ == "__main__":
	main()
