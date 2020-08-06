import csv 
req_file="/Users/gayathri/Downloads/pythonscripts/code/testfile.csv"

fo=open(req_file,"r")
content=csv.reader(fo,delimiter=",")
for each in content:
	print(each)

fo.close()

