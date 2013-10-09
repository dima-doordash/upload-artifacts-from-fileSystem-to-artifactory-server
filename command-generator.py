import os
# this file assumes settings.xml is from where you will run the file generated from this code.
files=[]

#Begin  User need to fill in following properties

directory = '' # your local directory in m2 format 
repId="" # repid used in setting.xml for maven to upload
url="" # url for the repository where you need to upload it to

#End  User need to fill in following properties


slashesInDirectory=directory.count('/')


for dirname, dirnames, filenames in os.walk(directory):
    for filename in filenames:
    	files.append(os.path.join(dirname, filename))


for file in files:
	artifact= file.split('/', slashesInDirectory+4 );
	if (len(artifact)) == slashesInDirectory+5: 
		
		orgDir = artifact[slashesInDirectory+1]
		
		module=  artifact[slashesInDirectory+2]
		
		verDir = artifact[slashesInDirectory+3]
		
		ext =  artifact[slashesInDirectory+4]
		fullPathToFile=directory+"/"+orgDir+"/"+module+"/"+verDir+"/"+ext

		# add/delete formats according to your need
		if ".jar" in ext:
			print("mvn -X -s settings.xml -e deploy:deploy-file -DgroupId="+orgDir+" -DartifactId="+module+" -Dfile="+fullPathToFile+"  -Dversion="+verDir+" -Dpackaging=jar  -DrepositoryId="+repId+" -Durl="+url+"")
		elif ".war" in ext:
			print("mvn  -X -s settings.xml -e deploy:deploy-file -DgroupId="+orgDir+" -DartifactId="+module+" -Dfile="+fullPathToFile+"  -Dversion="+verDir+" -Dpackaging=war  -DrepositoryId="+repId+" -Durl="+url+"")
		elif ".libd" in ext:
 			print("mvn  -X -s settings.xml -e deploy:deploy-file -DgroupId="+orgDir+" -DartifactId="+module+" -Dfile="+fullPathToFile+"  -Dversion="+verDir+" -Dpackaging=libd  -DrepositoryId="+repId+" -Durl="+url+"")
 		elif ".zip" in ext:
 			print("mvn  -X -s settings.xml -e deploy:deploy-file -DgroupId="+orgDir+" -DartifactId="+module+" -Dfile="+fullPathToFile+"  -Dversion="+verDir+" -Dpackaging=zip  -DrepositoryId="+repId+" -Durl="+url+"")	
		else:
			print "# not a recognised format => "+ ext
