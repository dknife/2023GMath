import math

vec1 = [1,2,3]
vec2 = [2,1,1]

def norm(v) :
    dim = len(v)
    value = 0.0
    for i in range(0, dim) :
        value += v[i]**2.0
    return math.sqrt(value)


def main() :
    n1 = norm(vec1)
    n2 = norm(vec2)
    print(n1, n2)


main()
