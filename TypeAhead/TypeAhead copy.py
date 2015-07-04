#! /usr/bin/python
#################################################
#			CodeEval Type Ahead					#
#################################################
# Zachary Priddy - 2015 						#
# me@zpriddy.com 								#
#												#
# RUN: $python TypeAhead.py <input>				# 									
#################################################
#################################################


#################
# CodeEval Disc.
#################
'''
CHALLENGE DESCRIPTION:

Your task is to build a type-ahead feature for an upcoming product. 

When the user enters a word or set of words, we want to be able to "predict" what they're going to type next with some level of accuracy. We've chosen to implement this using the N-Gram algorithm defined here. 

Your program should return a tuple of predictions sorted high to low based on the prediction score (upto a maximum of three decimal places, or pad with zeroes upto three decimal places i.e. 0.2 should be shown as 0.200), (if predictions share the same score, they are sorted alphabetically.) Words should be split by whitespace with all non-alphanumeric characters stripped off the beginning and end. 
Prediction scores are calculated like this: Occurrences of a word after an N-gram / total number of words after an N-gram e.g. for an N-gram of length 2:

ONE TWO ONE TWO THREE TWO THREE
"TWO" has the following predictions:

THREE:0.666,ONE:0.333
"THREE" occurred 2 times after a "TWO" and "ONE" occurred 1 time after a "TWO", for a total of 3 occurrences after a "TWO". 

Your program will run against the following text, ignoring all punctuation i.e. Hardcode it into your program:

Mary had a little lamb its fleece was white as snow;
And everywhere that Mary went, the lamb was sure to go.
It followed her to school one day, which was against the rule;
It made the children laugh and play, to see a lamb at school.
And so the teacher turned it out, but still it lingered near,
And waited patiently about till Mary did appear.
"Why does the lamb love Mary so?" the eager children cry; "Why, Mary loves the lamb, you know" the teacher did reply."
INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.The input file contains several lines. Each line is one test case. Each line contains a number followed by a string, separated by a comma. E.g.

2,the
The first number is the n-gram length. The second string is the text printed by the user and whose prediction you have to print out.

OUTPUT SAMPLE:

For each set of input produce a single line of output which is the predictions for what the user is going to type next. E.g.

lamb,0.375;teacher,0.250;children,0.125;eager,0.125;rule,0.125
'''
####################
#SAMPLE INPUT FILE:
####################
'''
2,the
2,against
2,was
2,about
2,white
4,school And so
3,Mary had
2,And
3,the lamb
3,rule It
3,went the
3,the rule
3,children laugh
2,little
3,lamb love
2,the
4,it out but
4,still it lingered
4,one day which
4,Mary went the
3,her to
3,followed her
3,it out
3,it lingered
4,know the teacher
4,And so the
3,till Mary
3,which was
2,Why
4,the lamb love
3,appear Why
3,still it
3,cry Why
3,Mary so
2,still
4,school And so
2,Why
3,one day
4,had a little
4,lamb its fleece
2,as
2,Mary
'''

###########################
#IMPORTS FROM ZP_TEMPLATE
###########################
import sys
import os
import string

#########
#VARS
#########
debug = False

testInput = '''Mary had a little lamb its fleece was white as snow;
And everywhere that Mary went, the lamb was sure to go.
It followed her to school one day, which was against the rule;
It made the children laugh and play, to see a lamb at school.
And so the teacher turned it out, but still it lingered near,
And waited patiently about till Mary did appear.
"Why does the lamb love Mary so?" the eager children cry; "Why, Mary loves the lamb, you know" the teacher did reply."'''


def main(args):
	filename=args[0]
	readfile=open(filename,'r')
	lines = readfile.read().splitlines()
	lines = [a for a in lines if a != '']
	if debug: print lines

	for line in lines:
		if debug: print line
		textStart = line.split(',')[1]
		ngram = line.split(',')[0]

		if debug: print textStart, ngram

		cleanText = sanText(testInput)

		if debug: print cleanText

		perdiction = perdict(cleanText,textStart,ngram)

		printPerdiction(perdiction)


def printPerdiction(perdiction):
	if debug: print perdiction
	perdictionList = [v[0] for v in sorted(perdiction.iteritems(), key=lambda (k, v): (-v, k.lower()))]
	if debug: print perdictionList
	outputString = ''

	for item in perdictionList:
		outputString += item + ',' + '%1.3f' % perdiction[item] + ';'

	print outputString[:-1]





def sanText(text):
	'''This function is used to sanitize the text input'''
	returnText = text.replace('\n', ' ')
	alpha = string.lowercase[::]
	alpha += string.uppercase[::]
	alpha += ' '
	returnText = ''.join([a for a in returnText if a in alpha])
	returnText = ' ' + returnText
	return returnText

def perdict(text,startString,ngram):
	'''This function is used to guess the next perdiction and the likelyhood'''
	perdiction = {}
	startString = startString
	startStringCount = text.count(' ' + startString)
	if startStringCount != 0:
		perdictionCountIncerment = 1.00/startStringCount

		if debug: print startStringCount

		startStringIndexies = []
		lastIndex = 0

		try:
			stringExtraCount = startString.count(' ') + 1
		except:
			stringExtraCount = 0

		for x in xrange(0,startStringCount):
			startStringIndexies.append(text.index(startString,lastIndex))
			lastIndex = startStringIndexies[x] + len(startString)

		if debug: print startStringIndexies

		for stringIndex in startStringIndexies:
			textStart = text[stringIndex::]
			if debug: print textStart
			textStart = textStart.split(' ')
			if debug: print textStart

			tempString = ''
			for x in xrange(stringExtraCount,int(ngram)):
				try:
					if x > stringExtraCount:
						tempString += ' '
					tempString += textStart[x]
				except:
					pass

			if debug: print tempString

			if tempString in perdiction:
				perdiction[tempString] += float(perdictionCountIncerment)
			else:
				perdiction[tempString] = float(perdictionCountIncerment)

			if debug: print perdiction
			

		return perdiction
	else:
		return None



###########################
# PROG DECLARE
###########################
if __name__ == '__main__':
	main(sys.argv[1:])
