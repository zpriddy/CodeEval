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
debug_less = False


def main(args):
	filename=args[0] 
	readfile=open(filename,'r')
	lines = readfile.read().splitlines()
	lines = [a for a in lines if a != '']

	if debug: print lines

	for line in lines:
		if debug: print line
		names = line.split(';')[0]
		products = line.split(';')[1]

		products = products.split(',')
		products = [Product(a) for a in products]

		names = names.split(',')
		names = [Customer(a) for a in names]

		if debug or debug_less:
			print "Names:"
			for name in names:
				print '\t'+name.name
			print "Products:"
			for product in products:
				print '\t'+product.name
		
		for name in names:
			for product in products:
				SS = 0
				if product.isEvenLength: 
					SS = name.vowels * 1.5
				else:
					SS = name.consonants
				if hcf(name.length, product.length) != 1:
					SS = SS * 1.5

				if debug: print "Name:",name.name,"Product:",product.name,"SS:", SS

				name.addScore(product.name,SS)
				product.addScore(name.name,SS)

			#print name.name,name.scores
			#print '' 
			#print product.name,product.scores

		usedNames = []
		usedProducts = []
		scores = []
		while len(usedNames) < len(names) and len(usedProducts) < len(products):
			maxScore(products,usedNames,usedProducts,scores)

		print("%.2f" % sum(scores))




def maxScore(products,usedNames,usedProducts,scores):
	maxScore = 0
	maxScoreProduct = None
	maxScoreName = None

	for product in products:
		#print product.name
		for score in product.scores.values():
			#print score
			if score[1] >= maxScore and product.name not in usedProducts and score[0] not in usedNames:
				maxScore = score[1]
				maxScoreName = score[0]
				maxScoreProduct = product.name



	#print "MAX:",maxScore,maxScoreProduct, maxScoreName
	usedProducts.append(maxScoreProduct)
	usedNames.append(maxScoreName)
	scores.append(maxScore)



def hcf(x, y):
   while(y):
       x, y = y, x % y
   return x


def countVowels(inputString):
	vowels = ['A','E','I','O','U','Y']
	total_count = 0
	for vowel in vowels:
		total_count += inputString.upper().count(vowel)

	if debug: print 'Vowels:',total_count
	return total_count

def countConsonants(inputString):
	consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
	total_count = 0
	for consonant in consonants:
		total_count += inputString.upper().count(consonant)

	if debug: print 'Consonants:',total_count
	return total_count
'''
def isEvenLength(inputString):
	letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	total_length  = 0
	for letter in letters:
		total_length += inputString.upper().count(letter)

	if debug: print 'Total Length:', total_length

	if total_length % 2 == 0:
		if debug: print 'Is Even'
		return True
	else:
		if debug: print 'Is Odd'
		return False
'''
def totalLength(inputString):
	letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	total_length  = 0
	for letter in letters:
		total_length += inputString.upper().count(letter)

	if debug: print 'Total Length:', total_length

	return total_length

class Customer:
	def __init__(self,name):
		self.name = name
		self.length = totalLength(name)
		self.isEvenLength = self.length % 2 == 0
		self.consonants = countConsonants(name)
		self.vowels = countVowels(name)
		self.scores = {}

	def addScore(self,product,score):
		self.scores[product] = score

class Product:
	def __init__(self,product):
		self.name = product
		self.length = totalLength(product)
		self.isEvenLength = self.length % 2 == 0
		self.consonants = countConsonants(product)
		self.vowels = countVowels(product)
		self.scores = {}

	def addScore(self,name,score):
		self.scores[name] = [name, score]




###########################
# PROG DECLARE
###########################
if __name__ == '__main__':
	main(sys.argv[1:])
