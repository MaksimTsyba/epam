def get_pare(l: list):
    data = []
    count = 0
    for item in l:
        if count + 1 <= len(l) - 1:
            data.append((l[count], l[count + 1]))
        count += 1
    if len(data) == 0:
        data = None
    return data


print(get_pare(["test", "hello", "python", "city"]))
