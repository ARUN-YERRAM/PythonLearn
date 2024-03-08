import numpy as np
A = np.ndarray([[1,2,3],[4,6,3]])
print(A.ndim)

print(A.shape)
print(A.size)
print(A.itemsize)

f = open("6py.py","r")
print(f.read())
f.close()

f = open("6py.py","w")
print(f.write("egege"))
f.close()


import os
if (os.path.exists("fjs.py")):
    os.remove("fjs.py")
else:
    print("File does not exist")

# import antigravity
# import this

import numpy
print("vegh")