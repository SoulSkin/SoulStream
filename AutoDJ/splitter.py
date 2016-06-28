'''
	Nightbot AutoDJ file Splitter
		Created by: SoulSkin
		soulskinmc@gmail.com
	
	Description:
		This program takes the file output of the Nightbot Beta App for AutoDJ and splits it.
'''
import time
import SSPUtils.IO as IO

#always in %USER%/Documents/Nightbot
inputFile = "C:/Users/John/Documents/Nightbot/current_song.txt"

#anywhere you want it
folder = "C:/Users/John/Documents/Stream Assets/OBS_dynamic/AutoDJ"
titleFile = folder+"song_title.txt"
artistFile = folder+"song_artist.txt"
requesterFile = folder+"song_requester.txt"
combinedFile = folder+"song_title_artist.txt"


#Guts of the program
#------#
def MAIN():
	print("Splitting Nightbot AutoDJ file")
	#this var makes it so the console is not spammed with redundant messages.
	last = ""
	while True:
		file = IO.fileRead(inputFile)[0]
		list = file.split(" - ")
		IO.fileWriteClear(list[0],artistFile)
		IO.fileWriteClear(list[1],titleFile)
		IO.fileWriteClear(list[2][14:],requesterFile)
		IO.fileWriteClear("\""+list[1]+"\" by "+list[0],combinedFile)
		if not last == file:
			print ("new song: "+file)
		last = file
		time.sleep(10)

MAIN()
import os
os.system("pause")