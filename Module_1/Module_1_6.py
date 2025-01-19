my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict: ', my_dict)
print('Existing value: ', my_dict.get('Masha'))
print('Not existing value: ', my_dict.get('Alexey'))
print('Deleted value: ', my_dict.pop('Egor'))
my_dict.update({'Kamila': 1981, 'Artem': 1915})
print('Modified dictionary: ', my_dict)

my_set = {1, 'Яблоко', 42.314}
print(my_set)
my_set.add(13)
my_set.add ((5, 6, 1.6))
my_set.discard(1)
print('Modified set: ', my_set)