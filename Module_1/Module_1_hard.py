dict_of_average_grades = {}

list_of_grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
set_of_students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = (sorted(tuple(set_of_students)))
b = [sum(list_of_grades[0])/len(list_of_grades[0]), sum(list_of_grades[1])/len(list_of_grades[1]),
     sum(list_of_grades[2])/len(list_of_grades[2]), sum(list_of_grades[3])/len(list_of_grades[3]),
     sum(list_of_grades[4])/len(list_of_grades[4])]
dict_of_average_grades.update({a[0]:b[0], a[1]:b[1], a[2]:b[2], a[3]:b[3], a[4]:b[4]})

print(dict_of_average_grades)