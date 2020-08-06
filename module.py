'''
#Working with getpass modules
import getpass
db_pass=getpass.getpass(prompt="Enter your password") #this will not show the entered password
print(db_pass)
db_user=getpass.getuser()
'''
'''
#working with sys module
#sys - helps to get the python runtime environment on your system
import sys
#print(dir(sys))
print(sys.platform)
print(f"The platform is {sys.platform}")
print(f"The version is {sys.version_info}")
print(f"The modules imported {sys.modules}")
print(sys.path) # It is an environment variable for python
#sys.exit() # This will stop the running python script
#sys.argv - returns a list of cli arguments passed to the a python script
'''
'''
import sys
print(sys.argv)
usr_string=sys.argv[1]
usr_action=sys.argv[2]
if usr_action=="lower":
    print(usr_string.lower())
elif usr_action=="upper":
    print(usr_string.upper())
elif usr_action=="title":
    print(usr_string.title())
else:
    print("Please select upper/lower/title option")
'''

#OS modules - work or interact with operating system
#changing, making, deleting directories
import os
print(os.sep)
print(os.getcwd())
#print(os.chdir("/home/user")) will help to move the directory
print(os.listdir())
#os.environ #will get the environment variables
print(os.path)


