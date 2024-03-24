"""
1. Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные,
а затем выведите на экран. Используйте функции для консольного ввода input()
и консольного вывода print().
Попробуйте также через встроенную функцию id() понаблюдать, какие типы объектов
могут изменяться и сохранять за собой адрес в оперативной памяти.
"""
# Создаем переменные
integer_variable = 42
float_variable = 3.14
string_variable = "Привет, мир!"

# Выводим переменные на экран
print("integer_variable:", integer_variable)
print("float_variable:", float_variable)
print("string_variable:", string_variable)

# Запрашиваем данные у пользователя
user_integer = int(input("Введите целое число: "))
user_float = float(input("Введите дробное число: "))
user_string = input("Введите строку: ")

# Выводим введенные пользователем данные
print("user_integer:", user_integer)
print("user_float:", user_float)
print("user_string:", user_string)

# Проверяем типы переменных и их адреса в памяти с использованием функции id()
print("Тип integer_variable:", type(integer_variable), "Адрес:", id(integer_variable))
print("Тип float_variable:", type(float_variable), "Адрес:", id(float_variable))
print("Тип string_variable:", type(string_variable), "Адрес:", id(string_variable))
print("Тип user_integer:", type(user_integer), "Адрес:", id(user_integer))
print("Тип user_float:", type(user_float), "Адрес:", id(user_float))
print("Тип user_string:", type(user_string), "Адрес:", id(user_string))

print('stop')

