def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('kajak'))
print(is_palindrome('dupek'))
print(is_palindrome(''))
print(is_palindrome('a'))