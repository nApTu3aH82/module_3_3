def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params() # вызов функции без аргументов работает
print_params(12)
print_params('Keys', [1, 7, 10])
print_params('Football', False, 17)
# Вызов функции работает при передаче количества аргументов не более трех!
print_params(b=25) # работает
print_params(c = [1,2,3]) # работает

values_list = [False, 'Immortal', 0]
values_dict = {'a': 10, 'b': 'Source', 'c': 3}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32,'Строка']
print_params(*values_list_2, 42)