'''
   Assumes l is a list of integars
   returns the first even number in list
   raises an exception if no even number in list
   '''

def isEven(l):

   for i in l:
       if i % 2 == 0:
           return i
   raise ValueError("No even numbers in list!")

#isEven([1,3,5,7])
print(isEven([5, 8, 3, 2]))
print(isEven([1,3,5,7]))