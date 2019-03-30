def my_split(value="", separate="", max = -1):
    data = []

    # recursive function for check separate in enter text
    def check_str(text, max_it):
        if max is not -1:
            if len(data) is max:
                data.append(text)
                return False
        if text.find(separate) is not -1:
            data.append(text[0:text.find(separate)])
            check_str(text[text.find(separate)+len(separate):], max_it)
        else:
            data.append(text)
            return False

    check_str(value, max)

    return data


x = 'hello, world, world'

print(my_split(x, ', '))

