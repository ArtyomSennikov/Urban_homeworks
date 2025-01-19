# Первый вариант
n = (int(input('Введите число от 3 до 20: ')))
parole = []

for i in range(1, 21):
    for j in range(i, n):
        if i == j:
            continue
        elif n % (i + j) == 0:
            parole.append(i)
            parole.append(j)
result = str(parole)
result = result.replace(", ", "")
print(result)

# Вариант, который выводит сразу все возможные пароли.
n = list(range(3, 21))
parole = []

# def result():
#    res = str(parole)
#    res = res.replace(", ", "")
#    parole.clear()
#    return res
# for i in n:
#    for j in range(1, 21):
#        for k in range(j, i):
#            if j == k:
#                continue
#            elif i % int(j + k) == 0:
#                parole.append(j)
#                parole.append(k)
#    print(i, " - ", result())