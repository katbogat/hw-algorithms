'''Условие задачи "Лишняя буква":
Васе очень нравятся задачи про строки, поэтому он придумал свою.
Есть 2 строки s и t, состоящие только из строчных букв.
Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию.
Нужно найти добавленную букву.
'''

'''Формат ввода:
На вход подается кортеж, содержащий строки s и t.
'''

'''Формат вывода:
Выведите лишнюю букву.
'''

# Пример ввода -> вывода:
inputs = [
    ('abcd', 'abcde'),   # -> e
    ('go', 'ogg'),       # -> g
    ('xtkpx', 'xkctpx')  # -> c
]


# тут ваше решение:
def k_calcultion(first_string, second_string):
    for first_letter, second_letter in zip(first_string, second_string):
        if first_letter != second_letter:
            return second_letter
    return second_string[-1]


for input in inputs:
    first_string = list(input[0])
    second_string = list(input[1])
    first_string.sort()
    second_string.sort()
    print(k_calcultion(first_string, second_string))
