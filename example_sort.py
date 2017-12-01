def gen_random_lst(length, min_val=1, max_val=10000):
    """
        Возвращает список случайных чисел.

        Возвращает список случайных чисел от 1 до 10000, 
        но позволяет пользователю определять свой диапазон
    """
    import random

    rand_lst = [random.randint(min_val, max_val) for i in range(length+1)]

    return rand_lst


def bubble_sort(lst):
    """
    Функция-заглушка для сортировки методом пузырька

    Как бы сортирует, но на самом деле нет список,
    который был ей передан в качестве входного параметра
    Эта функция должна быть переписана
    """
    sorted_list = [i for i in lst]

    return sorted_list


def default_py_sort(lst):
    """
    Сортировка стандартным методом sorted, встроенным в Python
    """

    return sorted(lst)


lst = gen_random_lst(10000)

# print(bubble_sort(lst))

if __name__ == '__main__':

    import timeit

    print(timeit.timeit("default_py_sort(lst)",
                        setup="from __main__ import default_py_sort, lst", number=10))
    print(timeit.timeit("bubble_sort(lst)",
                        setup="from __main__ import bubble_sort, lst", number=10))
