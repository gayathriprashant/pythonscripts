'''
#Dict to print numbers 1 to 5
num=eval(input("Enter your number between 1 to 5 : "))

num_val={1:'One',2:'Two',3:'Three',4:'Four',5:'Five'}

if num in [1,2,3,4,5]:
    print(num_val.get(num))
else:
    print("Enter the number within 1 to 5 r10ange")
'''

'''
#Platform modules 
import platform
print(dir(platform))
#print(help(platform))
print(f"This is {platform.system()} os")
print(f"This is python {platform.python_version()}")
print(f"This is python {platform.python_version_tuple()}")
print(f"This is {platform.machine()}")
print(f"This is {platform.release()}")
print(f"This is {platform.platform()}")
print(f"This is {platform.architecture()}")
print(f"This is {platform.processor()}")
print(f"This is {platform.node()}")
print(f"This is {platform.uname()}")
'''

#getpass module - getpass and getuser













