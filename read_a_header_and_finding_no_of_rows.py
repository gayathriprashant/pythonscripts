import csv 
req_file="/Users/gayathri/Downloads/pythonscripts/code/testfile.csv"

fo=open(req_file,"r")
content=csv.reader(fo,delimiter=",")
#print(list(content))
#print(f'The header is:\n {list(content)[0]}')
header=next(content)
print("The header is: ",header)
print("The no of rows are: ",len(list(content))-1)
'''
for each in content:
	print(each)
'''
fo.close()

