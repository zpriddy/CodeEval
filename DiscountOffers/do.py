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
debug = True
debug_less = False


def main(args):
	filename=args[0]
	readfile=open(filename,'r')
	lines = readfile.read().splitlines()
	lines = [a for a in lines if a != '']

	if debug: print lines

	for line in lines:
		if debug: print line
		try:
			names = line.split(';')[0]
			products = line.split(';')[1]

			products = products.split(',')
			#products = [Product(a) for a in products]

			names = names.split(',')
			#names = [Customer(a) for a in names]


			myData = DataStore(names,products)
			myData.printDataStore()

			#print products

			for name in names:
				for product in products:
					if product != '' and product != ' ':
						SS = 0
						if totalLength(product) %2 == 0:
							SS = countVowels(name) * 1.5
						else:
							SS = countConsonants(name)
						if hcf(totalLength(name), totalLength(product)) != 1:
							SS = SS * 1.5

						#print "Name:",name,"Product:",product,"SS:", SS

						myData.addScore(name,product,SS)

			#myData.printDataStore()		
			#myData.getOptColValue()
			myData.ev_gt = True
			t1 = myData.calculateSum()

			myData.usedNames = []
			myData.usedProducts = []
			myData.ev_gt = False
			t2 = myData.calculateSum()

			myData.printDataStore()

			t3 = myData.calcMaxTry2()

			if t3 > t2 and t3 > t1:
				print("%.2f" % t3)

			elif t3 > t2 and t3 < t1:
				print("%.2f" % t1)

			elif t3 < t2 and t2 > t1:
				print("%.2f" % t2)

			elif t3 < t2 and t2 < t1:
				print("%.2f" % t1)

			elif t3 == t1 and t1 > t2:
				print("%.2f" % t1)

			elif t3 == t1 and t1 < t2:
				print("%.2f" % t2)

			elif t2 == t1 and t2 > t3:
				print("%.2f" % t2)

			elif t2 == t1 and t2 < t3:
				print("%.2f" % t3)

			elif t3 == t2 and t2 < t1:
				print("%.2f" % t1)

			elif t3 == t2 and t2 > t1:
				print("%.2f" % t2)

			elif t1 == t2 and t2 == t3:
				print("%.2f" % t1)



			#print t1, t2, t3


		except:
			pass


		'''
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

		#print scores
		#print usedProducts
		#for name in names:
		#	print name.name

		print("%.2f" % sum(scores))
		'''



def maxScore(products,usedNames,usedProducts,scores):
	maxScore = 0
	maxScoreProduct = None
	maxScoreName = None

	for product in products:

		#print product.name
		for score in product.scores.values():
			#print score
			if score[1] > maxScore and product.name not in usedProducts and score[0] not in usedNames:
				maxScore = score[1]
				maxScoreName = score[0]
				maxScoreProduct = product.name

			elif score[1] > maxScore and product.name in usedProducts and score[0] not in usedNames:
				#print "NEED TO POP"
				index = usedProducts.index(product.name)
				usedProducts.pop(index)
				usedNames.pop(index)
				scores.pop(index)

				maxScore = score[1]
				maxScoreName = score[0]
				maxScoreProduct = product.name

				usedProducts.append(maxScoreProduct)
				usedNames.append(maxScoreName)
				scores.append(maxScore)
				break








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


class DataStore:
	'''
	This is the class for the dataStore as illustrated blow
	[     ][Prod 1][Prod 2][Prod 3].....[        ]  << Products Table
	[Name1][  SS  ][  SS  ][  SS  ].....[Row Sum1]
	[Name2][  SS  ][  SS  ][  SS  ].....[Row Sum2]
	  ^^									^^
	Names Table							Row Sums Table
	[     ][ColSum][ColSum][ColSum].....[		 ] << Col Sums Table

	'''
	def __init__(self,names,products):
		self.names = names
		self.products = products
		self.dataTable = []
		self.rowSums = []
		self.colSums = []
		self.scores = []

		## Prepare Tables
		self.products.insert(0,'')
		self.products.append(' ')
		self.colSums.insert(0,'')

		#Set Print Vars
		self.lJustProduct = max(len(a) for a in products)
		self.lJustName = max(len(a) for a in names)

		#build Scores Table
		for name in self.names:
			row = []
			for x in range(0,len(self.products) -2 ):
				row.append(0)
			self.scores.append(row)
			self.rowSums.append(-99)

		for x in range(0,len(self.products) -2 ):
			self.colSums.append(-99)

		#Future Holders
		self.usedNames = []
		self.usedProducts = []


	def getLowestCol(self):
		lowestColValue = None
		lowestColIndex = None
		for x in reversed(range(1,len(self.scores[0])+1)):
			if lowestColValue == None and self.products[x] not in self.usedProducts:
				lowestColValue = self.colSums[x]
				lowestColIndex = x
			else:
				if self.ev_gt:
					if self.colSums[x] > lowestColValue and self.products[x] not in self.usedProducts:
						lowestColValue = self.colSums[x]
						lowestColIndex = x
				else:
					if self.colSums[x] < lowestColValue and self.products[x] not in self.usedProducts:
						lowestColValue = self.colSums[x]
						lowestColIndex = x

		#print "Lowest Col Value:",lowestColValue, "Lowst Col Index:",lowestColIndex

		return lowestColIndex


	def getOptColValue(self):
		'''
		Finds the value in the column that has the smallest difference between itself and the max of the row its in

		1 [3] 2  < best row fit (it is max so difference is 0)
		5 3 9 
		7 1 8 
		  ^
		  Test Col
		'''

		colIndex = self.getLowestCol() -1

		colInfo = {}
		for x in range(0,len(self.names)):
			colInfo[x] = {'value':self.scores[x][colIndex],'diff':max(self.scores[x]) - self.scores[x][colIndex],'rowTotal':self.rowSums[x],'name':self.names[x],'product':self.products[colIndex + 1]}
			#print colInfo[x]

		
		bestValue = None
		for x in reversed(range(0,len(colInfo))):
			if bestValue == None and colInfo[x]['name'] not in self.usedNames:
				bestValue = colInfo[x]
			elif len(self.usedNames) < len(self.names)-1 and len(self.usedProducts) < len(self.products) -3:
				if colInfo[x]['name'] not in self.usedNames:
					if bestValue['diff'] == colInfo[x]['diff']:
						#bestValue = colInfo[x] if colInfo[x]['rowTotal'] < bestValue['rowTotal'] else bestValue
						pass

					if colInfo[x]['diff'] < bestValue['diff']:
						#print colInfo[x]
						#print self.usedNames
						bestValue = colInfo[x]
			else:
				pass

		

		return bestValue


	def calculateSum(self):
		totalValue = 0

		while len(self.usedNames) < len(self.names) and len(self.usedProducts) < len(self.products) -2 :
			bestFit = self.getOptColValue()
			
			#print bestFit
			totalValue += bestFit['value']
			self.usedNames.append(bestFit['name'])
			self.usedProducts.append(bestFit['product'])

		#print self.usedProducts

		#print("%.2f" % totalValue)

		secondTotal = self.calculateSecondSum()

		#print secondTotal if secondTotal > totalValue else totalValue
		if totalValue > secondTotal:
			return totalValue
		else:
			return secondTotal



	def calculateSecondSum(self):
		totalValue = 0 
		secondUsedNames = []
		secondUsedProducts = []
		testValue = 0
		testName = ''
		testProduct = ''

		while len(secondUsedNames) < len(self.names) and len(secondUsedProducts) < len(self.products) -2 :
			testValue = 0
			for x in reversed(range(0,len(self.names))):
				for y in reversed(range(0,len(self.scores[x]))):
					if self.scores[x][y] > testValue and self.names[x] not in secondUsedNames and self.products[y] not in secondUsedProducts:
						testValue = self.scores[x][y]
						testName = self.names[x]
						testProduct = self.products[y]

			totalValue += testValue
			secondUsedNames.append(testName)
			secondUsedProducts.append(testProduct)

		#print totalValue, secondUsedProducts, secondUsedNames

		thirdSum = self.calculateThirdSum()

		if thirdSum > totalValue:
			return thirdSum
		else:
			return totalValue
		

		#return totalValue

	def calculateThirdSum(self):
		totalValue = 0 
		secondUsedNames = []
		secondUsedProducts = []
		testValue = 0
		testName = ''
		testProduct = ''

		while len(secondUsedNames) < len(self.names) and len(secondUsedProducts) < len(self.products) -2 :
			testValue = 0
			for x in range(0,len(self.names)):
				for y in range(0,len(self.scores[x])):
					if self.scores[x][y] > testValue and self.names[x] not in secondUsedNames and self.products[y] not in secondUsedProducts:
						testValue = self.scores[x][y]
						testName = self.names[x]
						testProduct = self.products[y]

			totalValue += testValue
			secondUsedNames.append(testName)
			secondUsedProducts.append(testProduct)

		#print totalValue, secondUsedProducts, secondUsedNames

		return totalValue

	def calcMaxTry2(self):
		totalsArray = []
		indexMax = 0
		valueMax = 0
		totalValue = 0 
		usedNames = []
		usedProducts = []
		for startIndex in range(0,len(self.names)):
			totalValue = 0 
			usedNames = []
			usedProducts = []
			
			#startIndex = startIndex - len(self.names) if startIndex >= len(self.names) else startIndex
			#print "Start Index:",startIndex
			for x in range(0,len(self.names)):
				indexMax = 0
				valueMax = 0
				indexValue = x + startIndex
				indexValue = indexValue - len(self.names) if indexValue >= len(self.names) else indexValue

				#indexMax, valueMax = max(enumerate(self.scores[indexValue]))

				for productIndex in range(0,len(self.scores[indexValue])):
					if self.scores[indexValue][productIndex] >= valueMax and self.products[productIndex+1] not in usedProducts:
						valueMax = self.scores[indexValue][productIndex]
						indexMax = productIndex

				usedProducts.append(self.products[indexMax+1])
				totalValue += valueMax

				#print "Index Value:", indexValue, indexMax, valueMax

			#print "Toal Value:", totalValue
			totalsArray.append(totalValue)

		for startIndex in reversed(range(0,len(self.names))):
			totalValue = 0 
			usedNames = []
			usedProducts = []
			
			#startIndex = startIndex - len(self.names) if startIndex >= len(self.names) else startIndex
			#print "Start Index:",startIndex
			for x in reversed(range(0,len(self.names))):
				indexMax = 0
				valueMax = 0
				indexValue = x + startIndex
				indexValue = indexValue - len(self.names) if indexValue >= len(self.names) else indexValue

				#indexMax, valueMax = max(enumerate(self.scores[indexValue]))

				for productIndex in range(0,len(self.scores[indexValue])):
					if self.scores[indexValue][productIndex] >= valueMax and self.products[productIndex+1] not in usedProducts:
						valueMax = self.scores[indexValue][productIndex]
						indexMax = productIndex

				usedProducts.append(self.products[indexMax+1])
				totalValue += valueMax

				#print "Index Value:", indexValue, indexMax, valueMax

			#print "Toal Value:", totalValue
			totalsArray.append(totalValue)
		return max(totalsArray)









	def addScore(self,name,product,score):
		nameIndex = self.names.index(name)
		productIndex = self.products.index(product)-1

		#print name,product,nameIndex, productIndex

		self.scores[nameIndex][productIndex] = score

		self.rowSums[nameIndex] = sum(self.scores[nameIndex])

		self.colSums[productIndex + 1] = sum(list(self.scores[x][productIndex] for x in range(0,len(self.names))))




	def printDataStore(self):
		for product in self.products:
			if product == '':
				print 'Names'.ljust(self.lJustName,' '),
			elif product == ' ':
				print "|",'Total Row'.ljust(self.lJustName,' '),
			else:
				print product.ljust(self.lJustProduct, ' '),
		print ''

		rowDiv = ''
		for x in range(0,self.lJustName + self.lJustProduct * (len(self.products) -1)):
			rowDiv += '-'
		print rowDiv

		for x in range(0,len(self.names)):
			print self.names[x].ljust(self.lJustName, ' ') + "|",
			for score in self.scores[x]:
				print str(score).ljust(self.lJustProduct, ' '),
			print "|", self.rowSums[x]

		print rowDiv

		for colSum in self.colSums:
			if colSum == '':
				print ''.ljust(self.lJustName,' '),
			else:
				print str(colSum).ljust(self.lJustProduct,' '),
		print ''










###########################
# PROG DECLARE
###########################
if __name__ == '__main__':
	main(sys.argv[1:])
