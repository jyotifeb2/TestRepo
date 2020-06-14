word=input('Enter the String ')

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

#fin = open('words.txt')
count = 0
num_of_words = 4

for line in word:
    word = line.strip()
    if has_no_e(word) == True:
        count += 1
        print(word)

print(count / num_of_words * 100, '%')