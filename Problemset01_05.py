#from this import s
s=input('enter number ')
numbers = s.split(',')
sum = 0

for e in numbers:
    sum += float(e)

print (sum)