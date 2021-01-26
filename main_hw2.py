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


chiffres = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}  # set


def read_keyboard():
    is_int = True
    print("Please enter an int:\n")
    value = input()
    # Avoid catch exception, check if all chars are digits ; LE: could have been done with isdigit ? :)
    if value[0] not in chiffres and value[0] not in {'-'}:  # First char can be (-) as well
        # print(value[0], 'not in range')
        is_int = False
    for i in range(1, len(value)):
        # print(value[i])
        if value[i] not in chiffres:
            # print(value[i], 'not in range')
            is_int = False
    if not is_int:
        return 0
    else:
        return int(value)


print('1: ', my_sum_function())
print('2: ', my_sum_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print('3: ', my_sum_function(2, 4, 'abc', param_1=2))

n = 9
sr = sum_rec(n)
sre = sum_rec_even(n)
sro = sum_rec_odd(n)
print(f'Sum to {n} is {sr}')
print(f'Sum even numbers to {n} is {sre}')
print(f'Sum  odd numbers to {n} is {sro}')
print(f'Check sro+sre==sr {sro}+{sre}=={sr} {sro + sre == sr}')

n = 10
sr = sum_rec(n)
sre = sum_rec_even(n)
sro = sum_rec_odd(n)
print(f'Sum to {n} is {sr}')
print(f'Sum even numbers to {n} is {sre}')
print(f'Sum  odd numbers to {n} is {sro}')
print(f'Check sro+sre==sr {sro}+{sre}=={sr} {sro + sre == sr}')

print(read_keyboard())
