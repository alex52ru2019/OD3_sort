# сортировка вставками
# берем число и вставляем его туда, где левый от него меньше,а правый больше

a = [-3, 5, 0, -8, 1, 10]

def insert_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

print(insert_sort(a))