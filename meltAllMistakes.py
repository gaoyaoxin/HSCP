#!/usr/bin/python
# -*- coding: <utf-8> -*-


import glob
theList = glob.glob('*/mistakes.txt')

bigData = []

for i in theList:
	fo = open(i, encoding='UTF-8')
	data = fo.read() + '\n\n\n\n'
	fo.close()
	
	fo = open('allMistakes.txt', 'a', encoding='UTF-8')
	fo.write(data)
	fo.close()