my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]  # initial list
print(my_list)
my_list_asc = my_list[::]  # copy of initial list
my_list_asc.sort()
print('Initial list unchanged: ')
print(my_list)
print('New list sorted asc: ')
print(my_list_asc)
my_list_desc = list(my_list_asc)  # copy of sorted list asc
my_list_desc.reverse()
print('Initial list unchanged: ')
print(my_list)
print('New list sorted asc unchanged: ')
print(my_list_asc)
print('New list sorted desc: ')
print(my_list_desc)
my_list_even = my_list_asc[1::2]
my_list_odd = my_list_asc[::2]
my_list_multiples3 = my_list_asc[2::3]
print('Even numbers list sorted: ')
print(my_list_even)
print('Odd numbers list sorted: ')
print(my_list_odd)
print('Multiple of 3 numbers list sorted: ')
print(my_list_multiples3)
# Intra python in depresie ? True la ambele de mai jos, 0=-0
print(my_list[-0] is my_list[0])
print(my_list[-0] == my_list[0])
