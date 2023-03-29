NumPy as np :
- NumPy is usually imported under the np alias.
- alias: In Python alias are an alternate name for referring to the same thing.

> Ex-1: Create an alias with the as keyword while importing:
import numpy as np
Now the NumPy package can be referred to as np instead of numpy.

> Ex-2: Example

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)  #[1 2 3 4 5]


> Ex-3: Checking NumPy Version :  The version string is stored under __version__ attribute.

import numpy as np
print(np.__version__)   #1.16.3
