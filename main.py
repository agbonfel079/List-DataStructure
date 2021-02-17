# List items are enclosed in square brackets
# Lists are ordered
# Lists are mutable
# List elements do not  need to be unique 
# List can be of different data types 

# list = []
# list = [1,2,3]
# list = ['orange','apple', 'pear', 'apple', 'banana']
# list = [1, 'Hello', 5.0]

# print(list)

'''
List  Indexing
'''

# fruits = ['orange','apple', 'pear', 'apple', 'banana']
# print(fruits[-3])

# fruits = ['orange','apple', ['pear', 'apple', 'banana']]
# print(fruits[2][2])

'''
How to Slice Lists in Python
'''

# fruits = ['orange','apple', 'pear', 'apple', 'banana']

# print(fruits[:])
#print(fruits[2:5])
# print(fruits[:3])
# print(fruits[2:])
#print(fruits[::2])
# print(fruits[::-1])

'''
Add Elements To a List
'''
# fruits = ['orange','apple', 'pear', 'apple', 'banana']

# fruits[0] = 'Berries'
# print(fruits)

# fruits[1:4] = ['Mandarins','Peaches','Plums']
# print(fruits)

# fruits.append('Limes')
# print(fruits)

'''
Remove or Delete List Item
'''
# fruits = ['orange','apple', 'pear', 'apple', 'banana']

# del fruits[0]
# print(fruits)
# del fruits[1:5]
# print(fruits)
# del fruits
# print(fruits)

'''
Python List Methods
'''

# print(dir(list))
# print(help(list.index))
# print(help(list.append))
# print(help(list.insert))
# print(help(list.clear))

# fruits = ['orange','apple', 'pear', 'apple', 'banana']
# fruits.append('cashew')
# print(fruits)


#=======================

# fruits = ['orange','apple', 'pear', 'apple', 'banana']
# fruits.insert(0, 'guava')
# print(fruits)

#=======================

# fruits = ['orange','apple', 'pear', 'apple', 'banana']
# fruits.clear()
# print(fruits)


# #=======================
# fruits = ['orange','apple', 'pear', 'apple', 'banana']
# # fruits.pop (-1)
# # print(fruits)

# print(fruits.index('banana'))

# pos =fruits.index('apple')
# fruits.pop(pos)
# print(fruits)

#=======================

fruits = ['orange','apple', 'pear', 'apple', 'banana','banana','banana']
# print(fruits.count('banana'))

# result =  {}
# for x in fruits:
#   result[x] = fruits.count(x)

#   print(result)

# from  collections import Counter 

# print(Counter(fruits))

'''
List Membership  Test
'''

fruits = ['orange','apple', 'pear', 'apple', 'banana']

print("orange" not in fruits) 