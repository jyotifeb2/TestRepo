#Iterative Approach

n=int(input('Enter Number '))


def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

print(iterative_factorial(n))

#Recursive Approach

m=int(input('Enter Number '))
def recursive_factorial(m):
    if m == 1:
        return 1
    else:
        return m * recursive_factorial(m-1)

print(recursive_factorial(m))