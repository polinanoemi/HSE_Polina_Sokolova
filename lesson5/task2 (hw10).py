import random

# Генерация первого массива из 100 000 случайных чисел
random_numbers_array = [random.randint(1, 1000000) for _ in range(100000)]

# Генерация второго массива из 100 000 словарей
dict_array = [{"num_1": random.randint(1, 1000000), "num_2": random.randint(1, 1000000)} for _ in range(100000)]

# Функция сортировки пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = [arr[j + 1], arr[j]]

# Сортировка первого массива с помощью сортировки пузырьком
bubble_sort(random_numbers_array)

# Сортировка второго массива по ключам "num_1" и "num_2"
dict_array.sort(key=lambda x: (x["num_1"], x["num_2"]))

# Вывод результатов
print("Первый массив после сортировки пузырьком:", random_numbers_array[:10])
print("Второй массив после сортировки по ключам 'num_1' и 'num_2':", dict_array[:10])
