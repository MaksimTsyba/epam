import math
import re
import builtins


def calc_math(value):
    if value[0] == 'pi' or value[0] == 'e':
        result = getattr(math, value[0])
    else:
        result = getattr(math, value[0])(float(value[1]))
    return result


def cal_additional_parameters(value):
    return getattr(builtins, value[0])(float(value[1]))


math_param = dir(math)
additional_param = ['abs', 'round']
all_parameters = math_param + additional_param


# def pcalc(value):
#     left_bracket = re.findall(r'\(', value)
#     right_bracket = re.findall(r'\)', value)
#     if len(left_bracket) != len(right_bracket):
#         return 'error: missing bracket'
#
#     math_parameters = re.findall(r'(\w+)\s*\((.+?)\)', value)
#     print(math_parameters)
#     value = value.replace('pi', str(math.pi)).replace('e', str(math.e))
#
#     value = value.replace(' (', '(')
#     for items in math_parameters:
#         if items[0] not in all_parameters:
#             return 'Error: parameter "' + items[0] + '" not found'
#         if items[0] in additional_param:
#             value = value.replace(items[0] + '(' + items[1] + ')', str(cal_additional_parameters(items)))
#         else:
#             value = value.replace(items[0] + '(' + items[1] + ')', str(calc_math(items)))
#
#     print(value)
#
#     print(len(left_bracket))
#     if len(left_bracket) or len(right_bracket):
#         x = []
#         z = ""
#         counter = False
#         for item in value:
#
#             if item == '(' or item == ')':
#                 if item == ')':
#                     z += item
#                 if len(z) > 0:
#                     if z.find('(') != -1 and z.find(')') != -1:
#                         z.replace('(', '').replace(')', '')
#                         if len(x) > 0:
#                             if x[-1].find('(') != -1:
#                                 z = x[-1] + str(eval(z))
#                                 del x[-1]
#                             else:
#                                 z = str(eval(z))
#                                 x.append(z)
#                                 z = ""
#                             counter = True
#                         else:
#                             z = str(eval(z))
#                             x.append(z)
#                     else:
#                         x.append(z)
#                         z = ""
#             z += item
#             if item == ')' and not counter:
#                 z = ""
#             elif counter:
#                 z = z[:-1]
#                 counter = False
#         print(x)
#         result = eval(''.join(x))
#
#     else:
#         result = eval(value)
#     print('eval_result:', eval(value))
#     print('my_result:', result)
#     return result


def calculate_math_parameters(value):
    math_parameters = re.findall(r'(\w+)\s*\((.+?)\)', value)
    print(math_parameters)
    value = value.replace('pi', str(math.pi)).replace('e', str(math.e))

    value = value.replace(' (', '(')
    for items in math_parameters:
        if items[0] not in all_parameters:
            return 'Error: parameter "' + items[0] + '" not found'
        if items[0] in additional_param:
            value = value.replace(items[0] + '(' + items[1] + ')', str(cal_additional_parameters(items)))
        else:
            value = value.replace(items[0] + '(' + items[1] + ')', str(calc_math(items)))

    return value


def parse_brackets(value):
    x = []
    z = ""
    counter = False
    count_value = 1

    for item in value:
        if item == '(' or item == ')':
            if item == ')':
                z += item
            if len(z) > 0:
                if z.find('(') != -1 and z.find(')') != -1:
                    z.replace('(', '').replace(')', '')
                    if len(x) > 0:
                        if x[-1].find('(') != -1:
                            z = x[-1] + str(eval(z))
                            del x[-1]
                        else:
                            z = str(eval(z))
                            x.append(z)
                            z = ""
                        counter = True
                    else:
                        z = str(eval(z))
                        x.append(z)
                else:
                    x.append(z)
                    z = ""
        else:
            if len(value) == count_value:
                z += item
                x.append(z)
        z += item
        if item == ')' and not counter:
            z = ""
        elif counter:
            z = z[:-1]
            counter = False
        count_value += 1
    result = eval(''.join(x))
    return result


def pcalc2(value):
    left_bracket = re.findall(r'\(', value)
    right_bracket = re.findall(r'\)', value)
    if len(left_bracket) != len(right_bracket):
        return 'error: missing bracket'

    result_calculate = calculate_math_parameters(value)

    print(result_calculate)
    if len(left_bracket) or len(right_bracket):
        result = parse_brackets(result_calculate)
    else:
        result = eval(value)
    print('eval_result:', eval(value))
    print('my_result:', result)
    return result


# pcalc('(10+4)-(log10(5) + ( 3 + round(7.5) + 5) + 10) + (log10(4) + 4)')
# pcalc('10 + (log10(5) + ( 3 + abs(7.5) + 5) + 10)')
# pcalc('(10 + 1) + (9 + (log(3) + pi) + 10)+(11+4)')
# pcalc('sin(e**log(e**e**sin(23.0),45.0) + cos(3.0+log10(e**-e)))')
# pcalc('sin(e**log(e**e**sin(23.0),45.0) + cos(3.0+log10(e**-e)))')
# print(4 >= 3)
# print(eval('sin(e**log(e**e**sin(23.0),45.0) + cos(3.0+log10(e**-e)))'))


print(pcalc2('(3+4) * 44'))
# print()
