import math
import numpy as np


v1 = np.array([1,2,3])
v2 = np.array([2,4,6])

print(v1 + v2)
print(v1 - v2)
print(5, v1, 5 * v1)

print("dot product of ", v1, "and", v2 , "is", np.dot(v1, v2))
print("cross product of ", v1, "and", v2 , "is", np.cross(v1, v2))

def area(p1, p2, p3):
    N = np.cross(p2-p1,p3-p1)
    return 0.5 * np.linalg.norm(N)


p1 = np.array([1,1,1])
p2 = np.array([5,7,-3])
p3 = np.array([3,6,2])

print("area of triangle ", p1, p2, p3, " = " , area(p1, p2, p3))
