def calculate_structure_sum(data):
    res = 0
    for i in data:
        if isinstance(i, dict):  # Преобразование словарей в списки.
            i = list(i.items())
        if type(i) == str:       # Суммирование длин строк.
            res += len(i)
        if type(i) == int:       # Суммирование чисел.
            res += i
        if isinstance(i, (tuple, set, list)): # Рекурсия суммирующей функции, если ей попадается список, множество или кортеж.
            res += calculate_structure_sum(i)
    return res

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)