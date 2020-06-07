
x=input('Enter string #1: ')
y=input('Enter string #2: ')

def isIn(x,y):
    if x in y:
       return True
    elif y in x:
        return True
    else:
        return 'False'

print(isIn(x,y))