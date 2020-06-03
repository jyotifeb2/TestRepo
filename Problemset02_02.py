#a = input('Enter Number ')
#b = input('Enter Number ')

#A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b.
#Note: you will have to think about the base case.
def is_power(a, b):
    """Checks if a is power of b."""
    if a == b:
        return True
    elif a % b == 0:
        return is_power(a / b, b)
    else:
        return False
print(is_power(8, 2))
print(is_power(128,2))
