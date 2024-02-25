"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda x: x**2, num))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_simple(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_odd(num):
    if num % 2 == 0:
        return True
    return False


def filter_numbers(numbers, selector):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if selector == PRIME:
        return list(filter(lambda num: is_simple(num), list(numbers)))
    elif selector == ODD:
        return list(filter(lambda num: not is_odd(num), list(numbers)))
    elif selector == EVEN:
        return list(filter(lambda num: is_odd(num), list(numbers)))
