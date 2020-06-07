x = int(input("Enter an integer: "))
root = 0

while root < abs(x):
    root += 1
    for pwr in range(1,6):
        if root ** pwr == abs(x):
            if x < 0:
                print(-root, "to the power of", pwr, "=", x)
            else:
                print(root, "to the power of", pwr, "=", x)