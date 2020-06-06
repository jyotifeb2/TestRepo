#Write a program that computes the decimal equivalent of the binary number 10011?

binary = input('enter a number: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print (decimal)