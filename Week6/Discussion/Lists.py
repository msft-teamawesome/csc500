# Creating a list
list = [1, 2, 3]

# Inserting elements
list.append(4)          # [1, 2, 3, 4]
list.insert(1, 1.5)     # [1, 1.5, 2, 3, 4]
list.extend([5, 6])     # [1, 1.5, 2, 3, 4, 5, 6]

# Updating elements
my_list[2] = 2.5           # [1, 1.5, 2.5, 3, 4, 5, 6]

# Removing elements
list.remove(1.5)        # [1, 2.5, 3, 4, 5, 6]
popped_element = list.pop(3)  # [1, 2.5, 3, 5, 6], popped_element = 4
del list[1]             # [1, 3, 5, 6]