Copy a List:
- You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
- There are ways to make a copy, one way is to use the built-in List method copy().

> Eg-1:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)   #['apple', 'banana', 'cherry']

- Another way to make a copy is to use the built-in method list():

> Eg-2: Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


