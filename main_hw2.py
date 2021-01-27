def my_sum_function(*args, **kwargs):
    r_s = 0
    print(args)
    print(kwargs)
    for index, element in enumerate(args):  # print as tuple ; de obicei se foloseste index, element
        # print(index, element)
        type_element = type(element).__name__
        if type_element == 'float' or type_element == 'int':
            r_s += element
    for value in kwargs.values():
        # print(value)
        type_value = type(value).__name__
        if type_value == 'float' or type_value == 'int':
            r_s += value

    return r_s


def sum_rec(n):
    if n == 0:
        return 0
    else:
        return n + sum_rec(n - 1)


def sum_rec_even(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n % 2 == 0 and n > 2:
        return n + sum_rec_even(n - 2)
    elif n % 2 == 1 and n > 1:
        return sum_rec_even(n - 1)


def sum_rec_odd(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 0
    elif n % 2 == 0 and n > 2:
        return sum_rec_odd(n - 1)
    elif n % 2 == 1 and n > 1:
        return n + sum_rec_odd(n - 2)


def sum_rec_refact(n):
    # mind bending at my age :)
    """Mind bending at my age"""
    final_oddd_tuple = (1, 1)
    final_even_tuple = (0, 0)
    calc_tuple = final_even_tuple  # just to avoid warning
    if n == 0:
        return final_even_tuple
    elif n == 1:
        return final_oddd_tuple
    elif n % 2 == 0 and n > 0:
        list_to_calc = [n + sum_rec_refact(n - 1)[0], n + sum_rec_refact(n - 2)[1]]
        calc_tuple = tuple(list_to_calc)
    elif n % 2 == 1 and n > 1:
        list_to_calc = [n + sum_rec_refact(n - 1)[0], sum_rec_refact(n - 1)[1]]
        calc_tuple = tuple(list_to_calc)
    return calc_tuple


chiffres = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}  # set


def read_keyboard():
    is_int = True
    print("Please enter an int:\n")
    value = input()
    if len(value) == 0:
        is_int = False
    else:
        # Avoid catch exception, check if all chars are digits
        if value[0] not in chiffres and value[0] not in {'-'}:  # First char can be (-) as well
            # print(value[0], 'not in range')
            is_int = False
        for c in value[1:]:
            # print(value[i])
            if c not in chiffres:
                # print(value[i], 'not in range')
                is_int = False
                break
    if not is_int:
        return 0
    return int(value)


print('1: ', my_sum_function())
print('2: ', my_sum_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print('3: ', my_sum_function(2, 4, 'abc', param_1=2))

n = 15
sr = sum_rec(n)
sre = sum_rec_even(n)
sro = sum_rec_odd(n)
print(f'Sum to {n} is {sr}')
print(f'Sum even numbers to {n} is {sre}')
print(f'Sum  odd numbers to {n} is {sro}')
print(f'Check sro+sre==sr {sro}+{sre}=={sr} {sro + sre == sr}')

n = 20
sr = sum_rec(n)
sre = sum_rec_even(n)
sro = sum_rec_odd(n)
print(f'Sum to {n} is {sr}')
print(f'Sum even numbers to {n} is {sre}')
print(f'Sum  odd numbers to {n} is {sro}')
print(f'Check sro+sre==sr {sro}+{sre}=={sr} {sro + sre == sr}')

print('---Revisiting sum to calculate all in one function---\n')
n = 15
sr = sum_rec_refact(n)[0]
sre = sum_rec_refact(n)[1]
sro = sum_rec_refact(n)[0] - sum_rec_refact(n)[1]
print(f'Sum to {n} is {sr}')
print(f'Sum even numbers to {n} is {sre}')
print(f'Sum  odd numbers to {n} is {sro}')

n = 20
sr = sum_rec_refact(n)[0]
sre = sum_rec_refact(n)[1]
sro = sum_rec_refact(n)[0] - sum_rec_refact(n)[1]
print(f'Sum to {n} is {sr}')
print(f'Sum even numbers to {n} is {sre}')
print(f'Sum  odd numbers to {n} is {sro}')

print(read_keyboard())
