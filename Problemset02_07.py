
import palindrome

def is_palindrome(word):
    """Checks if word is a palindrome."""
    if len(word) <= 1:
        return True
    elif palindrome.first(word) == palindrome.last(word):

        if len(palindrome.middle(word)) == 1:
            return True
        #print('true')
        else:
            return is_palindrome(palindrome.middle(word))

    else:
        return False

#print('false')
print(is_palindrome(''))
print(is_palindrome('noon'))
print(is_palindrome('lol'))
