The Difference Between Copy and View:
- The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
- The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
- The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

COPY:
Example: Make a copy, change the original array, and display both arrays:

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)    # [42  2  3  4  5]
            # [1 2 3 4 5]
  
  
VIEW:
Example: Make a view, change the original array, and display both arrays:

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)  #[42  2  3  4  5]
          #[42  2  3  4  5]
  
  
  
Make Changes in the VIEW:
Example: Make a view, change the view, and display both arrays:

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)    #[31  2  3  4  5]
            #[31  2  3  4  5]


  
Check if Array Owns its Data:
- As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
- Every NumPy array has the attribute base that returns None if the array owns the data.
- Otherwise, the base  attribute refers to the original object.

Example:  Print the value of the base attribute to check if an array owns it's data or not:

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)   # None - copy owns the data
                # [1 2 3 4 5]- view doesnt own the data
