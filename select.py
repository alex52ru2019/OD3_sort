# сортировка выбором
# берем первый элемент и минимальное значение в массиве
# меняем их местами
# берем второй элемент и минимальное значение в массиве
# меняем их местами и т.д.

a = [-3, 5, 0, -8, 1, 10]
n = len(a)
for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if a[j] < a[min]:
            min = j
    a[i], a[min] = a[min], a[i]
    print(a)