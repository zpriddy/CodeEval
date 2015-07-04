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
		data.append(line.split(" "))

	readfile.close()

	lines = []

	for line in data:
		array_max = int(line[2])
		line_x = int(line[0])
		line_y = int(line[1])

		line_data = list(range(1,array_max+1))
		
		line_data = map(lambda x: "FB" if x % line_x == 0 and x % line_y  == 0 else "F"  if x % line_x == 0 else "B" if x % line_y == 0 else x, line_data)

		lines.append(line_data)

	for line in lines:
		print " ".join([str(x) for x in line])

		






###########################
# PROG DECLARE
###########################
if __name__ == '__main__':
	main(sys.argv[1:])
