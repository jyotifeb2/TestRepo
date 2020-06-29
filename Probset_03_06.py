string = [input("Enter a string") for i in range(0, 5)]
forbidden_string = input("Enter a forbidden_string ")
lst = []
for i in string:
    for j in forbidden_string:
        if j in i:
            lst.append(i)
            print(i,"the word use one of the forbidden letters")
            break
    else:
        print(i,"the word doesn’t use any of the forbidden letters")
lst2 = [k for k in lst if forbidden_string in k]
dict1 = {l: len(l) for l in lst2}
maxi = 0
char = ''
for i, j in dict1.items():
    if j >= maxi:
        maxi = j
        char = i
print(char)
