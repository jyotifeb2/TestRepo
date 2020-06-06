'''
 Assumes s is a string
 Returns the sum of the decimal digits in s
 For example, if s is 'a1b3c' it returns 5
 '''

#s=input('Enter String ')
def sumDigits(s):
  '''
  Assumes s is a string
  Returns the sum of the decimal digits in s
  For example, if s is 'a1b3c' it returns 5
  '''
  result = 0
  try:
    for i in range(len(s)):
      if s[i].isdigit():
        result += int(s[i])
    return result

  except TypeError:
    print('Input is not a string !')

print(sumDigits('a2b3c'))
print(sumDigits(1234))

   #res = sumDigits('123ab')
    #print('Vlaue ',res)
