import numpy as np
import math

v1 = np.array([1,0,0])
v2 = np.array([1,1,0])

def angle(vec1, vec2):
    dot = np.dot(v1, v2)
    # dot = |v1||v2|cosTheta
    # cosTheta = dot / |v1||v2|
    cosTheta = dot / (np.linalg.norm(v1)*np.linalg.norm(v2))
    angle = math.acos(cosTheta)
    angle = 180.0* angle / 3.141592
    return angle


print(angle(v1, v2))
