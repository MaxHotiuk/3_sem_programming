import re

def numeric_validation(number):
    if number.isnumeric():
        if int(number) > 0:
            return True
    else: return False

def range_validation(a, b, n):
    return n>=a and n<=b

def integer_validation(number):
    if len(number) == 0:
        return False
    if number[0] in ('-'):
        return number[1:].isdigit()
    return number.isdigit()

def validate_name(name):
    pattern = r'^[A-Z][a-z]+$'

    if re.match(pattern, name):
        return True
    else:
        return False