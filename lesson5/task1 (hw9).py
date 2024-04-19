import random
import time

# Генерация массива с использованием случайного шага от 3 до 5
start = 10
end = 250000000
step = random.randint(3, 5)
array = list(range(start, end, step))

# Функция для генерации 10 случайных чисел
random_numbers = [random.randint(start, end) for _ in range(10)]

# Функция линейного поиска
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

# Функция бинарного поиска
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Проверка наличия чисел в массиве с помощью линейного поиска
start_time = time.time()
for num in random_numbers:
    linear_search(array, num)
linear_search_time = time.time() - start_time

# Проверка наличия чисел в массиве с помощью бинарного поиска
start_time = time.time()
for num in random_numbers:
    binary_search(array, num)
binary_search_time = time.time() - start_time

print("Время линейного поиска:", linear_search_time)
print("Время бинарного поиска:", binary_search_time)
