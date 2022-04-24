import math

def add (a,b):
    return a + b

def sub (a,b):
    return a-b

def mul (a,b):
    return a*b

def div (a,b):
    if b == 0:
        print("Błąd dzielenia przez 0")
    else:
        return a/b

def add_matrices (a,b):
    result = a
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    return result


def rown_kwadratowe (a,b,c):
    delta = b*b - 4*a*c
    results = []
    if delta < 0:
        print("Brak pierwiastków")
    elif delta == 0:
        x = -b/a/2
        results.append(x)
        return results
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        results.append(x1)
        results.append(x2)
        return results

# print (add(2,2))
# print (sub(5,3))
# print (mul(4,5))
# print (div(6,2))
# div(1,0)
#
# X = [[1,2],[3,4]]
# Y = [[6,7],[8,9]]
# print(add_matrices(X,Y))
# print(rown_kwadratowe(1,5,6))
# print(rown_kwadratowe(1,4,4))
# rown_kwadratowe(3,1,3)