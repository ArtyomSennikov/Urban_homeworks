class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        data1 = open(self.__file_name, 'r')
        data2 = data1.read()
        data1.close()
        return data2

    def add(self, *products):
        warehouse = {}
        for i in products:
            if i.name and i.category not in self.get_products():
                warehouse.update({i.name: i.weight})
                data1 = open(self.__file_name, 'a')
                data1.write(f'{i}\n')
                data1.close()
                self.get_products()
            elif not warehouse:
                return
            else:
                weight = warehouse[i.name] + i.weight
                print(f'Продукт {i.name} уже был в магазине, его общий вес теперь равен {weight}')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
# Запись в файл
s1.add(p1, p2, p3)
# Получение списка продуктов
print(s1.get_products())
