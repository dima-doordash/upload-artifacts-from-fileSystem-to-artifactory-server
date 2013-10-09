upload-artifacts-from-fileSystem-to-artifactory-server
======================================================

Generates a shell script that you can use to upload artifacts from your local file system to Artifactory/Nexus artifact server


Steps:
1. Fill in the values in python file command-generator.py under section "Begin  User need to fill in following properties" and "End  User need to fill in following properties"

2. Populate the setting file with correct values

3. From within this directory type in following command " python command-generator.py > upload.sh "
4. ./upload.sh




Contents:
1) A Python file : for getting all the jars/wars from a user configured directory and then generating mvn deploy command for each one to be uploaded to artifact server
2) settings.xml : For letting maven know which server and which repo to  upload to 
3) settings-secuirity.xml  : For maven to read username and encrypted passwords
4) upload.sh: Auto generated file which has mvn deploy command for each artifact
