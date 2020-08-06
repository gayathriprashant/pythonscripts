#Files will be overwritten if already exists
#fo=open('newfile.txt','w')
'''
print(fo.mode)
print(fo.readable())
print(fo.writable())
'''
'''
fo.write("This is the testing of file\n This is the second line \n This is the third line\n")
content=["Testfile1\n Testfile2\n Testfile3"]
fo.writelines(content)
'''

my_content=['This is using loop-iteration-1','This is using loop-iteration-2','This is using loop-iteration-3']

fo=open("with_loop.txt",'a')

for each_line in my_content:
	fo.write(each_line+"\n")

fo=open("with_loop.txt","r")
data=fo.read()
fo.close()

print(data)
fo.close()
