Accessing Items :
- You can access the items of a dictionary by referring to its key name, inside square brackets:
- Get the value of the "model" key:

> Eg-1:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]   # Mustang


or :

- There is also a method called get() that will give you the same result:

x = thisdict.get("model")  #Mustang

> Eg-2:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)  # dict_keys(['brand', 'model', 'year'])


> Eg-3: The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

- Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change     #dict_keys(['brand', 'model', 'year'])
                                dict_keys(['brand', 'model', 'year', 'color'])
                                
                                
Check if Key Exists : To determine if a specified key is present in a dictionary use the in keyword:

> Eg-4: Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 
  
  
  
