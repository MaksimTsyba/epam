# replace double quote to single quote
def replace_dq(value):
    return value.replace('"', '\'')


print('Replace double quote to single quote:', replace_dq('"Hello, world"'))


# replace single quote to double quote
def replace_sq(value):
    return value.replace('\'', '"')


print('Replace single quote to double quote:', replace_sq('\'Hello, world\''))

