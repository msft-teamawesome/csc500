# Creating a dictionary
dict = {'a': 1, 'b': 2, 'c': 3}

# Inserting elements
dict['d'] = 4           # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Updating elements
dict['a'] = 10          # {'a': 10, 'b': 2, 'c': 3, 'd': 4}

# Removing elements
value = dict.pop('b')   # {'a': 10, 'c': 3, 'd': 4}, value = 2
del dict['c']           # {'a': 10, 'd': 4}
last_item = dict.popitem()  # {'a': 10}, last_item = ('d', 4)