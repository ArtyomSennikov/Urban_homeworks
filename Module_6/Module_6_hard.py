class Figure:
    sides_count = 0
    def __init__(self, color, sides):
        self.__color = color
        self.__sides = [sides] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if all(0 < i <= 255 and isinstance(i, int) for i in [r, g, b]):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        if all(0 < i  and isinstance(i, int) for i in sides):
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides() == True:
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides / (2 * 3.14)

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        for i in [self.get_sides()]:
            p = sum(i) / 2
            s = p * (p - i[0]) * (p - i[1]) * (p - i[2])
        return s


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
tr1 = Triangle((0, 0, 0), 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())