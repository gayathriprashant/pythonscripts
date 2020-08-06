#sfile="/Users/gayathri/Downloads/pythonscripts/code/newfile.txt"
#dfile="/Users/gayathri/Downloads/pythonscripts/code/destfile.txt"

sfile=input("Enter your source file location : ")
dfile=input("Enter your destination file location : ")
sfo=open(sfile,'r') # by default it is read mode if you don't specify
content=sfo.read()
sfo.close()

dfo=open(dfile,'w')
dfo.write(content)
dfo.close()