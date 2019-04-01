def get_longest_word(s: str):
    longest = ""
    word_len = 0
    for item in s.split(' '):
        if len(item) > word_len:
            longest = item
            word_len = len(item)
    return longest


print(get_longest_word('Python is simple\n and effective!'))

