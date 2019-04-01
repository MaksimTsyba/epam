def split_by_index(s: str, indexing: list):
    data = []
    start = 0

    for item in indexing:
        data.append(s[start:item])
        start = item
    data.append(s[start:])
    return data


text = "pythoniscool,isn'tit?"

print(split_by_index(text, [6, 8, 12, 13, 18]))

