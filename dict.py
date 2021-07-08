# Creating a Dictionary  with Integer Key

Dict1 = {1:'arun',2:'dhansika',3:'ronica'}
print("Dictionary  with Integer Key: ")
print(Dict1)
print(Dict1[2])

# Creating a Dictionary with Mixed keys

dict1 = {'name':'arun',1:[1,2,3,4],'rollnum':(12344)}
print("Creating a Dictionary with Mixed keys: ")
print(dict1)

# Dictionary use with deletion key word.
Dict = {5: 'Welcome', 6: 'To', 7: 'Motogb',
        'A': {1: 'CRA', 2: 'motor', 3: 'sport'},
        'B': {1: 'Racing', 2: 'Life'}}
print("Initial Dictionary: ")
print(Dict)

# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# Deleting a Key from Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)
