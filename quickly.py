# быстрая сорртировка
# делим массив на 3 части,
# больше опорного элемента, меньше опорного элемента, равные опорного элемента
# аналогично делим каждую часть, со своим опорным элементом
# и так до тех пор, пока не останется одна часть
# потом собираем части в один массив


def quick_sort(array):
    if len(array) <= 1:
        return array
    elemet = array[0]
    left = list(filter(lambda x: x < elemet, array))
    right = list(filter(lambda x: x > elemet, array))
    center = [i for i in array if i == elemet]
    return quick_sort(left) + center + quick_sort(right)

print(quick_sort([5, 2, 9, 0, 1, 5, 3]))