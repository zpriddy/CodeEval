#! /usr/bin/python
#################################################
#				   Python Template			#
#################################################
# Zachary Priddy - 2015						#
# me@zpriddy.com							#
#										#
# Features:								#
#		   - XXXXXX						#
#		   - XXXXXX						#
#################################################
#################################################
 
#########
#IMPORTS
#########
import sys
 
#########
#VARS
#########
debug = False
 
ones = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
teens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
 
def main(args):
	filename=args[0] 
	readfile=open(filename,'r')
	a = readfile.read().splitlines()
	a = [b for b in a if b.replace(' ','').replace('\t','').isdigit()]

	myarray = []
	for amount in a:
		myarray.append(DollarValue(amount))
 
	for dollar in myarray:
		textOutput = [	dollar.printHundreds('Billions'),dollar.printTens('Billions'),dollar.printOnes('Billions'),\
						dollar.printHundreds('Millions'),dollar.printTens('Millions'),dollar.printOnes('Millions'),\
						dollar.printHundreds('Thousands'),dollar.printTens('Thousands'),dollar.printOnes('Thousands'),\
						dollar.printHundreds('Hundreds'),dollar.printTens('Hundreds'),dollar.printOnes('Hundreds')]
		

		textOutput = [x for x in textOutput if x != None]
		if textOutput != [] : print ''.join(textOutput)
 
		    
 
 
 
class DollarValue:
	def __init__(self,value):
		self.value = int(value)
		self.length = len(str(self.value))
		self.hundreds = None
		self.thousands = None
		self.millions = None
		self.billions = None
		try:
			self.hundreds = (str(self.value)[-3:]) if self.length >= 3 else (str(self.value)[-self.length:])
			self.thousands = (str(self.value)[-6:-3]) if self.length >= 6 else (str(self.value)[-self.length:-3])
			self.millions = (str(self.value)[-9:-6]) if self.length >= 9 else (str(self.value)[-self.length:-6])
			self.billions = (str(self.value)[-12:-9]) if self.length >= 12 else (str(self.value)[-self.length:-9])
		except:
			pass
 
	def printOnes(self,base):
			    
		if self.value == 0 and base.lower() == 'hundreds':
			return "ZeroDollars"
		else:
			value = None
			try:
				value = None if len(self.getBase(base)) == 0 else int(self.getBase(base)[0]) if len(self.getBase(base)) == 1 else int(self.getBase(base)[-1:]) if int(self.getBase(base)[-2]) != 1 else None
			except:
				pass
			if value != None and base.lower() == 'hundreds':
				returnValue = ones[value] + 'Dollars'
				return 'OneDollars' if returnValue == 'OneDollars' and self.value < 10 else returnValue

			elif value != None and int(self.getBase(base)) != 0:
				return ones[value] + base[:-1]
 
	def printTens(self, base):
		value = None
		if self.value != 0:
			try:
				value = None if len(self.getBase(base)) <= 1 else int(self.getBase(base)[-2:-1]) if int(self.getBase(base)[-2]) != 1 else int(self.getBase(base)[-2:])
			except:
				pass
		if value != None and value < 10:
			return tens[value]
		elif value != None and value >= 10 and self.value <= 1000:
			return teens[value-10] + "Dollars"
		elif value != None and value >= 10 and base == 'Hundreds':
			return teens[value-10] + "Dollars"
		elif value != None and value >= 10:
			return teens[value-10] + base[:-1]
 
	def printHundreds(self,base):
		value = None
		if self.value != 0:
			try:
				value = None if len(self.getBase(base)) <= 2 else int(self.getBase(base)[-3])
			except:
				pass
		if value  and value < 10:
			return ones[value] + 'Hundred'
 
	def getBase(self,base):
		if base.lower() == 'hundreds':
			return self.hundreds
		elif base.lower() == 'thousands':
			return self.thousands
		elif base.lower() == 'millions':
			return self.millions
		elif base.lower() == 'billions':
			return self.billions
 
###########################
# PROG DECLARE
###########################
if __name__ == '__main__':
	main(sys.argv[1:])