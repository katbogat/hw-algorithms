'''Условие задачи "Большое число":
Даны числа. Нужно определить, какое самое большое число можно из них составить.
'''

'''Формат ввода:
В строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.
'''

'''Формат вывода:
Нужно вывести самое большое число, которое можно составить из данных чисел.
'''

# Пример ввода -> вывода:
inputs = [
    '15 56 2',    # -> 56215
    '1 783 2',   # -> 78321
    '2 4 5 2 10',  # -> 542210
]


# тут ваше решение:
def list_comparator(num_list1, num_list2):
    if (num_list1 + num_list2) > (num_list2 + num_list1):
        return True
    return False


def insertion_sort_by_comparator(array, more):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and more(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
    return array


for numbers in inputs:
    numbers_list = list(map(list, numbers.split()))
    n = len(numbers_list)

    sort_num_listlist = insertion_sort_by_comparator(numbers_list, list_comparator)
    sort_num_list = list(map(('').join, sort_num_listlist))
    print(('').join(sort_num_list))
