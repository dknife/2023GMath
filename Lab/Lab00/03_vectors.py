import math

print("Vectors")

v1 = [1, 2, 3]
v2 = [1, 1, 1]

def addVec(vec1, vec2) :
    sum = []
    for i in range(len(vec1)) :
        sum.append(vec1[i] + vec2[i])
    return sum

def subVec(vec1, vec2) :
    res = []
    for i in range(len(vec1)) :
        res.append(vec1[i] - vec2[i])
    return res

def multSVec(s, vec) :
    res = []
    for i in range(len(vec)) :
        res.append(s * vec[i])
    return res

def dot(vec1, vec2) :
    sum = 0
    for i in range(len(vec1)):
        sum += vec1[i]*vec2[i]
    return sum

def cross(vec1, vec2):
    res = []
    for i in range(len(vec1)):
        i1 = (i+1)%3
        i2 = (i+2)%3
        res.append(vec1[i1]*vec2[i2] - vec1[i2]*vec2[i1])
    return res

def norm(vec) :
    sumSquares = 0
    for i in range(len(vec)):
        sumSquares += vec[i]*vec[i]
    return math.sqrt(sumSquares)

def area(p1, p2, p3):
    return 0.5* norm(cross(subVec(p2, p1), subVec(p3, p1)))
