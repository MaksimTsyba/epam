import math
import re
import builtins


def calc_math(value):
    return getattr(math, value[0])(float(value[1]))


def cal_additional_parameters(value):
    return getattr(builtins, value[0])(float(value[1]))


math_param = dir(math)
additional_param = ['abs', 'round']
all_parameters = math_param + additional_param


def pcalc(value):
    left_bracket = re.findall(r'\(', value)
    right_bracket = re.findall(r'\)', value)
    if len(left_bracket) != len(right_bracket):
        return 'error: missing bracket'

    math_parameters = re.findall(r'(\w+)\s*\((.+?)\)', value)

    value = value.replace(' (', '(')
    for items in math_parameters:
        if items[0] not in all_parameters:
            return 'Error: parameter "' + items[0] + '" not found'
        if items[0] in additional_param:
            value = value.replace(items[0] + '(' + items[1] + ')', str(cal_additional_parameters(items)))
        else:
            value = value.replace(items[0] + '(' + items[1] + ')', str(calc_math(items)))

    print(value)
    print(eval(value))

    counter = 0
    x = []
    z = ""
    bracket = False
    test = 0
    for item in value:
        if item == '(' and not bracket:
            if test == 0:
                x.append(z)
                z = ""
            else:
                x[-1] = z
                z = ""
            # counter = 0

        if item == '(' and len(z) > 0:
            bracket = True

        z += item

        if item == ')' and not bracket:

            if z.find('(') != -1 and z.find(')') != -1:

                if counter == -1:
                    z = str(eval(z))
                    counter = 0
                else:
                    z = x[-1] + str(eval(z))
                    counter = -1
                x[-1] = z
                test = 1
            else:
                x.append(z)
                z = ""
                counter = 0
                test = 0

        elif item == ')' and bracket:
            bracket = False

    print(x)
    result = value

    return result


pcalc('(13 + 4) - (log10(5) + ( 3 + round(7.5) + 5)) + (log10(4) + 4)')
# pcalc('10 + (log10(5) + ( 3 + round(7.5) + 5) + 10)')
# print(math.log(5)+ 7)
