#Name:			Kevin Blighe
#Email:			kevinblighe@outlook.com / kevin@clinicalbioinformatics.co.uk
#Date:			27th November 2019
#Function(s):		Increments POS field in VCF

import sys
import os

#Check the number of command line arguments
if not len(sys.argv)==3:
	print "\nError:\tincorrect number of command-line arguments"
	print "Syntax:\tIncrementPos.py [Input VCF] [Output VCF]\n"
	sys.exit()
if sys.argv[1]==sys.argv[2]:
	print "Error:\tInput file is the same as the output file - choose a different output file\n"
	sys.exit()

#File input
fileInput = open(sys.argv[1], "r")

#File output for split multi-alleles
fileOutput = open(sys.argv[2], "w")

#Loop through each line in the input file
print ("Parsing VCF and incrementing POS...")
for strLine in fileInput:
	#Strip the endline character from each input line
	strLine = strLine.rstrip("\n")

	#The '#' character in VCF format indicates that the line is a header. Ignore these and just output to the new file
	if strLine.startswith("#"):
		fileOutput.write(strLine + "\n")
	else:
		#Split the tab-delimited line into an array
		strArray = [splits for splits in strLine.split("\t") if splits is not ""]

		#increment the POS field
		strArray[1] = str(int(strArray[1]) + 1)

		# concatenate the array and write out the line
		fileOutput.write("\t".join(strArray) + "\n")
print ("Done.")

#Close the files
fileInput.close()
fileOutput.close()
