#!/usr/bin/python
# -*- coding: <utf-8\n> -*-
#export entries https://www.pdawiki.com/forum/forum.php?mod=viewthread&tid=16514&highlight=词头
#
import time, re, sys



def printExercise():
	print('e.g. back, box, chicken, spoon')
	print('#1 back, lamp, people, smart')
	print('#2 book, front, keeper, wide')
	print('#3 finish, front, hard, man')
	print('########################')
	print('#(1) ache, brush, fairy, sweet')
	print('#(2) bags, changer, order, making')
	print('#(3) basket, club, hard, room')
	print('#(4) black, share, research, super')
	print('#(5) book, dead, note, result')
	print('#(6) brain, line, serious, shot')
	print('#(7) coach, count, fore, star')
	print('#(8) fall, flake, man, virgin')
	print('#(9) sleep, contest, queen, shop')
	print('#(10) A, B, C, D')

printExercise()


#1. input four words
def inputWord1():
	global word1
	word1 = input('Please input the first word(7 to exit):\n> ')
	if word1 == '7':
		print('You have exited this program.')
		sys.exit()

def inputWord2():
	global word2
	word2 = input('Please input the second word(7 to exit, 1 to retype the first word.):\n> ')
	if word2 == '7':
		print('You have exited this program.')
		sys.exit()
	elif word2 == '1':
		inputWord1()
		inputWord2()

def inputWord3():
	global word3
	word3 = input('Please input the third word(7 to exit, 1(2) to retype the first(second) word.):\n> ')
	if word3 == '7':
		print('You have exited this program.')
		sys.exit()
	elif word3 == '1':
		inputWord1()
		inputWord3()
	elif word3 == '2':
		inputWord2()
		inputWord3()

def inputWord4():
	global word4
	word4 = input('Please input the fourth word(7 to exit, 1(2 or 3) to retype the first(second or third) word.):\n> ')
	if word4 == '7':
		print('You have exited this program.')
		sys.exit()
	elif word4 == '1':
		inputWord1()
		inputWord4()
	elif word4 == '2':
		inputWord2()
		inputWord4()
	elif word4 == '3':
		inputWord3()
		inputWord4()



def inputAllWords():
	while 1:
		inputWord1()
		inputWord2()
		inputWord3()
		inputWord4()

		print('\n' + 'The words you have input are: ' + word1 + ', ' + word2 + ', ' + word3 + ', ' + word4 + '\n')
		global changeOrNot
		changeOrNot = input('Do you want to make any changes(y for Yes, n for No)?\n> ')
		if changeOrNot == 'y':
			whichToChange = input('Which one do you want to change(1, 2, 3 or 4)?\n> ')
			if whichToChange == '1':
				inputWord1()
			if whichToChange == '2':
				inputWord2()
			if whichToChange == '3':
				inputWord3()
			if whichToChange == '4':
				inputWord4()
		else:
			break

inputAllWords()
	
WORDS_SET = {}
for i in word1, word2, word3, word4:
	WORDS_SET[i] = {}


print(WORDS_SET)