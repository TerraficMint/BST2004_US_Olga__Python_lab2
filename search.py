import random

from sqlalchemy import false
random.seed(113)

# Инициализация и заполение массива рандомными числами
A = []
for i in range(10):
    A.append(random.randint(1, 50))
A.sort()
print("Исходный массив", A)


# метод поиска с помощью бинарной сортировки
# Отсортированный массив делится на две части равного размера, одна из которых исследуется далее

def binary_search(array, value):

    mid = len(array) // 2  # индекс среднего эл-та
    low = 0               # нижняя граница
    high = len(array) - 1  # верхняя граница

    # пока не найден нужный эл-т и границы не схлопнулись
    while array[mid] != value and low <= high:

        # число больше эл-та посередине -> нижняя граница смещается
        if value > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
        # новый поиск середины
        mid = (low + high) // 2

    if low > high:
        print("Искомого числа в массиве нет")
    else:
        print("ID =", mid)

# поиск Фибоначчи работает в отсортированном массиве,
# который сужает возможные местоположения с помощью чисел Фибоначчи.
# По сравнению с бинарным поиском, поиск Фибоначчи делит массив на две части,
# размеры которых являются последовательными числами Фибоначчи


def FibonacciSearch(array, value):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    # вычисление числа последовательности
    fibM = fibM_minus_1 + fibM_minus_2
    # пока не вышли за пределы массива
    while (fibM < len(array)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(array)-1))
        if (array[i] < value):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (array[i] > value):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i
    if(fibM_minus_1 and index < (len(array)-1) and array[index+1] == value):
        return index+1
    return -1

#  поиск происходит подобно двоичному поиску, но вместо деления области поиска на две части,
#  интерполирующий поиск производит оценку новой области поиска
#  по расстоянию между ключом и текущим значением элемента (примерно оценивает - элемент ближе к концу или началу)


def InterpolationSearch(array, value):
    low = 0
    high = (len(array) - 1)
    if low <= high and value >= array[low] and value <= array[high]:
        # вероятный индекс искомого элемента.
        # Он вычисляется как более высокое значение,
        # когда значение val ближе по значению к элементу в конце массива (array[high]),
        # и более низкое, когда значение val ближе по значению к элементу в начале массива (array[low]).
        index = low + \
            int(((float(high - low) /
                (array[high] - array[low])) * (value - array[low])))
        if array[index] == value:
            print("ID =", index)
        if array[index] < value:
            low = index + 1
        else:
            high = index - 1
    else:
        print("Искомого числа в массиве нет")


def insert(array, value):
    array.append(value)
    array.sort()
    print("Массив после вставки числа", value)
    print(array)


def remove(array, value):
    if value in array:
        array.remove(value)
        print("Массив после удаления числа", value)
        print(array)
    else:
        print("Введенного числа в массиве нет")


print("Провести поиск элемента? да/нет")
confirm = input()
answerYes = "да"
if (confirm == answerYes):
    print(" Бинарный поиск - 1\n Интерполяционный поиск - 2\n Поиск Фибоначчи - 3\n")
    search = input()
    if (search == "1"):
        print("Найти число: ", end=' ')
        search_elem = int(input())
        print("Бинарный поиск: ")
        binary_search(A, search_elem)
        print()
    elif (search == "2"):
        print("Найти число: ", end=' ')
        search_elem = int(input())
        result = InterpolationSearch(A, search_elem)
        print()
    elif (search == "3"):
        print("Найти число: ", end=' ')
        search_elem = int(input())
        print("ID = ", end=' ')
        print(FibonacciSearch(A, search_elem))
        print()
    else:
        print("Попробуйте еще раз.")

print("Вставить число в массив? да/нет")
confirm = input()
answerYes = "да"
if (confirm == answerYes):
    print("Нужно вставить число", end=' ')
    elemIn = int(input())
    insert(A, elemIn)


print("Удалить число из массива? да/нет")
confirm = input()
answerYes = "да"
if (confirm == answerYes):
    print("Нужно удалить число", end=' ')
    elemOut = int(input())
    remove(A, elemOut)
