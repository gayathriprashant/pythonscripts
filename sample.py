'''
print ("Hello")
a=10
b=20
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is greater than {a}")
'''

#testing data types and intro of print (f {}) command works only in python 3
'''
print("Hello  \t\b world ")
x=4
y=7.5
z=100.00
print(x)
#memory location of the variable used by 'id'
x=20
print(id(x))
print(type(y))
print(f"{x}\n{y}\n{z}")
print("{} {} {}".format(x,y,z))
print(id(x))
print(f"The value of x is: {x} and value of y is: {y}")
'''

#addition of two numbers
'''
a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
c=a+b
print(f"the addition of {a} and {b} is {c}")
'''
'''
a=eval(input("Enter number 1 : "))
b=eval(input("Enter number 2 : "))
c=a+b
print(f"the addition of {a} and {b} is {c}")
'''
'''
str1="Python Scripting"
print(str1[0:3])
print(len(str1))
print(str1.upper())
print(str1.casefold())
'''
'''
name="Henry Roosevelt"
print(name.endswith('t'))
print(name.startswith('Hen'))
print(name.islower())
print(name.isupper())
name1="\t".join(name)
name1="*".join(name)
print(name1)
print(name.center(70))
print(name.zfill(30))
text="python test script python"
print(text.rstrip('python'))
'''




























