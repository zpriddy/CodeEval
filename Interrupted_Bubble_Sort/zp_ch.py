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

def main(args):
	filename=args[0] 
	readfile=open(filename,'r')
	lines = readfile.read().splitlines()
	data = []
	for line in lines:
		data.append([map(int, line.split(" |")[0].split(" ")),int(line.split("|")[1])])
	
	for item in data:

		for x in range(0,item[1]):
			for i in range(0,len(item[0])):
				try:
					if(item[0][i] > item[0][i+1]):
						temp = item[0][i]
						item[0][i] =  item[0][i+1]
						item[0][i+1] = temp
						del temp
				except:
					pass

		print " ".join([str(x) for x in item[0]])









###########################
# PROG DECLARE
###########################
if __name__ == '__main__':
	main(sys.argv[1:])
