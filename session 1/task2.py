x = input('Enter word to check it is palindrome:')

if x == x[::-1]:
    print('This word is palindrome')
else:
    print('This word is not palindrome')

