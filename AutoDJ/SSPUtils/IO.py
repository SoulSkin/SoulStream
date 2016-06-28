#################################
#	SoulSkinPythonUtils - IO	#
#	  Created by: SoulSkin		#
#################################

import os
import os.path
import shutil

#---PRIVATE---#
def findFilenameAndDir(input):
	if not isinstance(input[0], str):
		input = input[0]
	filename = str(input[0])
	if len(input) > 1:
		filename = filename + str(input[1])
	return filename

#---PRIVATE---#
def reverseHelper(inputFile, lineModifier, nameModifier):
	file = fileRead(inputFile)
	file2= []

	for num in range(len(file)-1,-1,-1):
		file2.append(file[num][::lineModifier])
	fileWriteList(file2, str(inputFile) + nameModifier)
	print ("Created file: " + str(inputFile) + nameModifier)

#------#
def ping(*null):
	return True

#------#
def fileWrite(payload, *filenameAndDir):
	filename = findFilenameAndDir(filenameAndDir)

	f = open(filename, 'a')
	f.write(str(payload) + "\n")
	return payload

#------#
def fileWriteClear(payload, *filenameAndDir):
	filename = findFilenameAndDir(filenameAndDir)

	f = open(filename, 'w')
	f.write(str(payload) + "\n")
	return payload

#------#
def printAndWrite(payload, *filenameAndDir):
	print (fileWrite(payload, filenameAndDir))

#------#
def fileWriteList(payload, *filenameAndDir):
	filename = findFilenameAndDir(filenameAndDir)

	f = open(filename, 'a')
	for i in payload:
		f.write(str(i) + "\n")
	return payload

#------#
def fileRead(*filenameAndDir):
	lines = [];
	filename = findFilenameAndDir(filenameAndDir)
	
	f = open(filename, 'r')
	for line in f:
		lines.append(line.strip("\n").strip("\r"))
	return lines

#------#
def lineRead (lineNum, *filenameAndDir):
	return fileRead(filenameAndDir)[lineNum +1]

#------#
def fileReverse(inputFile):
	reverseHelper(inputFile, -1, ".reversed")

#------#
def fileMirror(inputFile):
	reverseHelper(inputFile, 1, ".mirrored")

#------#
def fileReverseAndMirror(inputFile):
	reverseHelper(inputFile, 1, ".mirrored")
	reverseHelper(inputFile, -1, ".reversed")

#------#
def createFile(*filenameAndDir):
	filename = findFilenameAndDir(filenameAndDir)
	if not os.path.isfile(filename):
		open(filename, 'w').write("")

#------#
def createFolder(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

#------#
def folder(directory):
	createFolder(directory)

#------#
def folderCopy(fromFolder, toFolder, fileExtension):
	dlFiles = fileFind(os.path.abspath(fromFolder), fileExtension)
		
	for file in dlFiles:
		filesCopyToDir(toFolder, file)
	return dlFiles

#------#
def folderDelete(fromFolder, fileExtension):
	dlFiles = fileFind(os.path.abspath(fromFolder), fileExtension)
		
	for file in dlFiles:
		fileDelete(file)
	return dlFiles

#------#
def fileSplitPart(parts, *filenameAndDir):
	fileParts = []
	file = fileRead(filenameAndDir)
	for part in range(1,parts):
		for lineNum in range(1,len(file)):
			fileParts[part].append(file[lineNum])
		
	return fileParts

#------#
def filesCopyToDir(copyDir, *files):
	createFolder(copyDir)
	for file in files:
		shutil.copy(file,copyDir)

#------#
def fileCopy(fromFile, toFile):
		shutil.copyfile(fromFile,toFile)
#------#
def fileExists(*filenameAndDir):
	filename = findFilenameAndDir(filenameAndDir);
	return os.path.exists(filename)

#------#
def fileFind(dir, fileExtension):
	foundFiles = [];
	folder(dir)
	for dirpath, dirnames, filenames in os.walk(dir):
		for filename in [f for f in filenames if f.lower().endswith(fileExtension.lower())]:
			foundFiles.append(os.path.join(dirpath, filename))
	return foundFiles

#------#
def fileDelete(*filenameAndDir):
	filename = findFilenameAndDir(filenameAndDir)
	os.remove(filename)

#------#
def getConfig():
	#Create a config parser for reading INI files
	try:
		import ConfigParser
		return ConfigParser.ConfigParser()
	except:
		import configparser
		return configparser.ConfigParser()