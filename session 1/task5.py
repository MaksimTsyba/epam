def get_digits(num: int):
    data = []

    for item in str(num):
        data.append(int(item))
    return tuple(data)


print(get_digits(1234638276352))

