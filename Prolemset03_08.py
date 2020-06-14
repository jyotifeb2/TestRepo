def is_abecdarian(s):
    index = 0
    while index < len(s)-1:
        if s[index + 1] < s[index]:
            return False
        index += 1
    return True

print(is_abecdarian('babcd'))
print(is_abecdarian('abcz'))