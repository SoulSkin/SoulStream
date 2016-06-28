import ftplib

#################################
#	SoulSkinPythonUtils - FTP	#
#	  Created by: SoulSkin		#
#################################

server = "localhost"
username = "User"
password = "password"


#Gets a connection from getConnection and uploads "localFile" to "remoteFile". Optional "dir" argument for remote
def Upload(localFile, remoteFile, dir="\\"):
	ftp = getConnection()
	ChangeOrCreateDir(ftp, dir)
	file = open(localFile, "rb");
	ftp.storbinary("STOR "+str(remoteFile), file);
	file.close()

##DEPRICATED-Gets a connection from getConnection and uploads the File object in "varFile" to "remoteFile". Optional "dir" argument for remote
def UploadFileVar(varFile, remoteFile, dir="\\"):
	ftp = getConnection()
	ChangeOrCreateDir(ftp, dir)
	ftp.storbinary("STOR "+str(remoteFile), file);

#Gets a connection from getConnection and downloads "remoteFile" to "localFile". Optional "dir" argument for remote
def Download(localFile, remoteFile, dir="\\"):
	ftp = getConnection()
	ChangeOrCreateDir(ftp, dir)
	file = open(localFile, "wb");
	ftp.retrbinary("RETR "+str(remoteFile), file.write);
	file.close()

#Creates root\"dirIn" if nesassary and moves into it
def ChangeOrCreateDir(workingConnection, dirIn):
	try:
		workingConnection.pwd()
		workingConnection.cwd(dirIn)
	except ftplib.error_perm:
		workingConnection.mkd(dirIn)
		workingConnection.cwd(dirIn)
	
#Sets a new server, username, and password for the FTP connection (global)
def setFullConnection(serv,user,Pass):
	setServer(serv);
	setUser(user);
	setPassword(Pass);

#Sets a new server for the FTP connection (global)
def setServer(serv):
	global server;
	server =  serv;

#Sets a new username for the FTP connection (global)
def setUser(user):
	global username;
	username =  user;

#Sets a new password for the FTP connection (global)
def setPassword(Pass):
	global password;
	password = Pass;

#Returns a FTP object with credentials from server, username, and password (all global)
def getConnection():
	global password, username, server
	return ftplib.FTP(server,username,password)

def test():
	getConnection().dir()