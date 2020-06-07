
a = int(input('Enter Number  '))
b= int(input('Enter Number  '))
c= int(input('Enter Number '))
def largest_odd(a, b, c):
    L = [i for i in (a, b, c) if i % 2 != 0]
    return max(L) if L else 'No Odd Number'

Number = largest_odd(a, b, c)
print('Largest odd Number', Number)
