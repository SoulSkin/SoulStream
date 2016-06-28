#################################
# SoulSkinPythonUtils - Strings #
#	  Created by: SoulSkin		#
#################################

#------#
def joinStrList(inputList):
	returnStr = ""
	for string in inputList:
		returnStr += str(string);
	return returnStr

#------#
def getInput(string):
	#Get input from console regardless of python 2 or 3
	try:
		return raw_input(string)
	except:
		return input(string)

#------#
def intToPadded(num, inDigits):
	num = int(num)
	if abs(num)<1000000000000:
		digits = 12
	if abs(num)<100000000000:
		digits = 11
	if abs(num)<10000000000:
		digits = 10
	if abs(num)<1000000000:
		digits = 9
	if abs(num)<100000000:
		digits = 8
	if abs(num)<10000000:
		digits = 7
	if abs(num)<1000000:
		digits = 6
	if abs(num)<100000:
		digits = 5
	if abs(num)<10000:
		digits = 4
	if abs(num)<1000:
		digits = 3
	if abs(num)<100:
		digits = 2
	if abs(num)<10:
		digits = 1
	
	
	
	toPad = digits-inDigits
	if toPad<1:
		toPad = 0
	padding = str(num)
	for i in xrange(toPad+1):
		padding = "0"+padding
	return padding
