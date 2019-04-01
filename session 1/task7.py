def foo(l: list):
    sum_l = 1
    for item in l:
        if isinstance(item, int):
            sum_l *= item
    new_list = []
    for result in l:
        if isinstance(result, int):
            new_list.append(int(sum_l / result))

    return new_list


print(foo([1, 2, 3, 4]))
