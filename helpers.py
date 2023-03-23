def input_validate_int(prompt):
    out = 0
    try:
        res = int(input(prompt))
        out = res
    except:
        print('\033[93m', 'Input is invalid')
        out = 0
    return out

def input_validate_float(prompt):
    out = 0
    try:
        res = float(input(prompt))
        out = res
    except:
        print('\033[93m', 'Input is invalid')
        out = 0
    return out

