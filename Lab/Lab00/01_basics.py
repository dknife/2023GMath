print("hello world")

# variables
a = 10
b = 2.5
c = a+b
print(c)

# if: 조건문
if c > 10 :
    print("c가 10보다 크다.")
elif c > 8 :
    print("c는 8에서 10 사이이다.")
else :
    print("c는 8이하이다.")

# array: 배열
iArray = [1,2,3,4]
print("iArray의 크기 = ", len(iArray))
print(iArray)
iArray[2] = 1000
print(iArray)

# 반복문
sum = 0
for i in range(0,len(iArray), 1) :
    sum += iArray[i]

print(sum)


def add(a, b) :
    return a+b

print(add(10,10))
print(add(100,100))
print(add(120,120))

###############################


a, b, c, d = 1,2,3,4

print(a,b,c,d)

### 다중 리턴

def fourOperations(a, b) :
    return a+b, a-b, a*b, a/b

param1 = 5
param2 = 6
iArray = 7


a, b, c, d = fourOperations(param1, iArray)

print(a,b,c,d)
