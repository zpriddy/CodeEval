#! /usr/bin/python
#################################################
#			Python Template						#
#################################################
# Zachary Priddy - 2015 						#
# me@zpriddy.com 								#
#												#
# Features: 									#
#	- XXXXXX									#
#	- XXXXXX 									#
#################################################
#################################################

#########
#IMPORTS
#########
import sys
import os

#########
#VARS
#########
debug = False 


def main(args):
	filename=args[0] 
	readfile=open(filename,'r')
	lines = readfile.read().splitlines()
	for line in lines:
		input_string = line

		matrixb = []
		matrixc = []

		matrix = input_string.split('|')
		matrix = [a.split(' ') for a in matrix if a != '']
		for a in matrix:
			for b in a:
				if b == '':
					a.pop(a.index(b))

		for a in matrix:
			for b in a:
				a[a.index(b)] = int(b)

		if debug: print matrix

		for a in range(0,len(matrix)):
			temp = []
			for b in range(0,len(matrix[0])):
				temp.append(matrix[b][a])
			if debug: print temp
			matrixb.append(temp)

		matrixb.sort()


		if debug: print '',matrixb,''


		matrix = []

		for a in range(0,len(matrixb)):
			temp = []
			for b in range(0,len(matrixb[0])):
				temp.append(matrixb[b][a])
				print matrixb[b][a],
			if debug: print temp
			if a != len(matrixb[0]) -1 : print "|",
			matrix.append(temp)

		print ''
		if debug: print '',matrixb,''



###########################
# PROG DECLARE
###########################
if __name__ == '__main__':
	main(sys.argv[1:])
