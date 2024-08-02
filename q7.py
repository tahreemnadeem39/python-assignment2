#Q7-Creating a list

list1: list[int] = [1, 2, 3]
list2: list[int] = [4, 5, 6]

# Use the extend() method to add the elements of list2 to list1
list1.extend(list2)

print(list1)
