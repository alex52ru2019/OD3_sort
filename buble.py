# пузырьковая сорртировка
# с каждым проходом перестановка максимального элемента в конце массива
mas = [5, 7, 4, 3, 8, 2]
n = len(mas)
for k in range(n-1):
    for i in range(n-1-k):
        if mas[i] > mas[i+1]:
            mas[i], mas[i+1] = mas[i+1], mas[i]
    print(mas)