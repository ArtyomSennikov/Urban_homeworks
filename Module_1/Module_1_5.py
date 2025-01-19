# Создание кортежа данных.
immutable_var = (1, 2, 'a', 'b')
print('Immutable tuple: ', immutable_var)

# Выполнение этой строки кода приведёт к ошибке программы.
#immutable_var[0] = 2

# Создание изменяемого списка данных.
mutable_list = [1, 2, 'a', 'b']

# Изменение списка.
mutable_list.append('Modified')
print('Mutable list: ', mutable_list)