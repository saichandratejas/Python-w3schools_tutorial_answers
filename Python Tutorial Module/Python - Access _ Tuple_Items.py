Access Tuple Items :
- You can access tuple items by referring to the index number, inside square brackets

> Eg-1:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #"apple"
print(thistuple[2]) #"cherry

Negative Indexing :
- Negative indexing means start from the end.
- -1 refers to the last item, -2 refers to the second last item etc.

> Eg-2 :

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])   #"cherry"

Range of Indexes :
- You can specify a range of indexes by specifying where to start and where to end the range.
- When specifying a range, the return value will be a new tuple with the specified items.


> Eg-3 :

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  #('cherry', 'orange', 'kiwi')


> Eg-4 :

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])    #('apple', 'banana', 'cherry', 'orange')


> Eg-5 :

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])   #"cherry", "orange", "kiwi", "melon", "mango"


Range of Negative Indexes :
- Specify negative indexes if you want to start the search from the end of the tuple:
- This example returns the items from index -4 (included) to index -1 (excluded)


> Eg-6 :

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])   #"kiwi", "melon", "mango"


> Eg-7 :

Check if Item Exists
- To determine if a specified item is present in a tuple use the in keyword:
- Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")   # Yes, 'apple' is in the fruits tuple
  
  
  
  
