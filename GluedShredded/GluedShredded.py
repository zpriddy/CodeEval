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

		shreds = input_string.split('|')
		shreds = [a for a in shreds if a != '']


		outputString = shreds[0]

		for shred in shreds:
			if shred[0] == shred[0].upper() and shred[0] not in [" ",",",".","!","1","2","3","4","5","6","7","8","9","0","-","'",'"']:
				#print shred[0]
				outputString = shred
				break


		
		#outputString = shreds[0]

		#outputString = shreds[0]

		#shreds = t - (n - 1)
		#len(shreds) + (len(shreds[0]) - 1) = t

		total_length=len(shreds) + (len(shreds[0]) - 1)
		if debug: print "Total Length: ", total_length
		if debug: print "Total Shreds: ", len(shreds)

		#Remove the first one
		shreds.pop(shreds.index(outputString))



		for x in range(0,1000):
			for shred in shreds: 
				changed = False

				#if debug: print "Starting testing"
				
				

				#if right_test['changed'] and left_test['changed']:
				#	print "ERROR"
				#	quit()
				if x < 100 or x % 2 == 0:
					right_test = testRight(shred, outputString, 1)
					if right_test['changed']:
						outputString = right_test['result']
						shreds.pop(shreds.index(shred))
						changed = True
				else:
					left_test = testLeft(shred, outputString, 1)
					if left_test['changed']:
						outputString = left_test['result']
						shreds.pop(shreds.index(shred))
						changed = True
				

		print outputString




#Test adding to right
def testRight(newString, outputString,groupSize):

	#print "Test String:", newString, "Current Output:", outputString
	testString = newString[:-groupSize]
	outputTestString = outputString[-len(testString):]
	#print "Testing", testString, "VS", outputTestString

	if testString == outputTestString:
		outputTestString = outputString + newString[len(newString)-1]
		#print "Returning:", outputTestString
		return {'changed':True,'result':outputTestString}

	return {'changed':False}


def testLeft(newString, outputString,groupSize):

	#print "Test String:", newString, "Current Output:", outputString
	testString = newString[groupSize:]
	outputTestString = outputString[:len(testString)]
	#print "Testing", testString, "VS", outputTestString

	if testString == outputTestString:
		outputTestString = newString[0:groupSize]+outputString
		#print "Returning:", outputTestString
		return {'changed':True,'result':outputTestString}

	return {'changed':False}






			







	


###########################
# PROG DECLARE
###########################
if __name__ == '__main__':
	main(sys.argv[1:])
