'''
import os

col_size=os.get_terminal_size().columns
print(col_size)
x="I am learning python scripting. It is easy scripting"
print(x.index('I',14))
print(x.count('learning'))
print(x.find('scripting '))
y="Welcome to python!!!"
print(y.center(col_size))
print(y.ljust(col_size))
print(y.rjust(col_size))
print(y.center(80))
'''
#examples of list
'''
data1=[40,10, 'test', 80.9, 'shell', 'python scripting']
print(data1[0])
print(data1[3])
print(data1[4][2])
print(data1[-1])
print(data1[-2])
print(data1[0:3])
print(data1[3:])
data1[1]=79
print(data1.index(40))
#data1.clear()
#data1.count(1)
data2=data1 # will allocate same address location pointed to data2
data3=data1.copy() # will have a different id location for .copy()
'''
'''
data1=[40,10, 'test', 80.9, 'shell', 'python scripting']
data1.append(9000)
print(data1)
data1.insert(3,2000)
print(data1)
'''
# examples of tuples
'''
test_tuple1=()
test_tuple2=(1,2,4,50,'shell','python')
print(test_tuple1)
print(test_tuple2[3])
test_tuple3=(40,20,[5,4,6])
print(test_tuple3[2][1])
test_tuple4=test_tuple2+test_tuple3
print(test_tuple4)
print(test_tuple4.count('shell'))
print(test_tuple4.index(50))
print(len(test_tuple4))
print(test_tuple2[:])
print(type(test_tuple4))
'''

'''
#Examples of dictionary - key value pair in {}
dict1={'Name':'Tom', 'Age':20, 'Gender':'Male'}
print(dict1)
print(dict1['Name'])
print(dict1.get('Age'))
#to create a new key pair
dict1['Hobby']='read books'
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict2=dict1.copy()
print(dict2)
print(id(dict1))
print(id(dict2))
dict2['cc']='xyz'
dict1.update(dict2)
print(dict1)
keys=['a','b','c']
dict5=dict.fromkeys(keys) #create a dictionary with keys
print(dict5)
dict5['a']="testing"
print(dict5)
#setdefault() - will not override the value
'''
'''
#Examples of Set - unordered collection of data
set1={3,4,5,6,5,4,6} #will remove repetition of data
set2={4.5,6,10,20}
print(set1)
print(set1.union(set2))
print(set1.intersection(set2))
'''













