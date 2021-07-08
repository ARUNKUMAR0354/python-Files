# Use the index() methond in list:
'''The index() method returns the index of the specified element in the list.
'''

vowels =['a','e','i','o','u']
index = vowels.index('i')
print("the index of i: ",index)

index = vowels.index('e')
print("the index of e: ",index)

# Use the append() method in list.
'''The append() method adds an item to the end of the list'''

Bikes = ['yamaha','honda','hero']
print("Before append the list:",Bikes)
Bikes.append('KTM')
print("Aftter append the list:",Bikes)

Bikes1 =['Ninja','Ducati']
Bikes.append(Bikes1)# append the wole list.
print("Aftter the append in one wole list:",Bikes)

# Use the extend() method in list
'''The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.

'''

Names = ['arun','kalai','selva']
print("Before extend in list:",Names)
Names1 = ['pari','thiru']
Names.extend(Names1)
print("After extend in list:",Names)

#use the extend() method in list, tuple, string .
Name_list =['ronica']
Name_set ={'dhansica'}
Name_tuble = ('krish','arun')
Name_list.extend(Name_set)
print("New list after the extend the set:",Name_list)
Name_list.extend(Name_tuble)
print("New list after extend the tuble:",Name_list)

# Use the insert() method in list.
'''The list insert() method inserts an element to the list at the specified index.'''

vowel = ['a', 'e', 'i', 'u']
vowel.insert(3, 'o')
print('Updated List:', vowel)

mixed_list = [{1, 2}, [5, 6, 7]]
number_tuple = (3, 4)
mixed_list.insert(1, number_tuple)# inserting a tuple to the list
print('Updated List:', mixed_list)

# Use the remove() method in list.
'''The remove() method removes the first matching element (which is passed as an argument) from the list.'''

# animals list
animals = ['cat','dog','cow','dog']
animals.remove('dog')
print('Updated animals list: ', animals)

# Use count() method in list.
'''The count() method returns the number of times the specified element appears in the list'''

Name =['a','r','u','n','k','u','m','a','r']
count = Name.count('a')
print("the count of 'a' is : ",count)
count = Name.count('k')
print("the count of 'k' is: ",count)

#Use  pop() method in list.
'''The pop() method removes the item at the given index from the list and returns the removed item.'''

languages = ['Python', 'Java', 'C++', 'French', 'C']
result = languages.pop(3)
print("Remove the 3rd index value using pop: ",result)
print('Updated List:', languages)

#use reverse() method in list.
'''The reverse() method reverses the elements of the list.'''

systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
systems.reverse()
print('Updated List:', systems)

#Reverse a List Using Slicing Operator
systems = ['aswin','vinoth','ruthra']
result = systems[::-1]
print(result)

#Use sort() method in list.
'''The sort() method sorts the elements of a given list in a specific ascending or descending order.'''


vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort()
print('Sorted list:', vowels)

# sort accepted in revrerse methode
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
print('Sorted list:', vowels)

#Use the copy() method in list list.
'''The copy() method returns a shallow copy of the list'''

old_list =[1,8,'g','f',7]
new_list = old_list.copy()
print(new_list)

#copy() method used to append value in list.
old_list = [1, 2, 3]
new_list = old_list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)

# shallow copy using the slicing syntax
list = ['cat', 0, 6.7]
new_list = list[:]# copying a list using slicing
new_list.append('dog')
print('Old List:', list)
print('New List:', new_list)

#Python List clear()
'''The clear() method removes all items from the list'''

list = [{1, 2}, ('a'), ['1.1', '2.2']]
list.clear()
print("list:",list)

# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]
del list[:]
print("list:",list)
