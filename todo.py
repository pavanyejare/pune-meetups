import sys
import os 
import pdb




if len(sys.argv) == 1 :
	print ("Provide argumanet")
	sys.exit(1)

if len(sys.argv) >= 2:
	first = sys.argv[1]
	if (first == "-a"):
		string = sys.argv[2]
		file1=open("test.txt",'a') 
		file1.write(string + "\n")
		file1.close()
		print ("Done")

	if (first == "-v"):
		f2=open("test.txt",'r')
		for i in f2:
		 print (i) 
