# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint


# len_array = int(input("Введите количество чисел в списке: "))
# numbers = []
# sum_elements = 0

# for i in range(len_array):
#     numbers.append(randint(1, 10))
# for val in numbers[1::2]:
#     sum_elements += val

# print(f"Список - {numbers}\nСумма элементов -> {sum_elements}")




# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint


# array_size = int(input("Введите количество чисел в списке: "))
# numbers = []
# multiplied = []

# for i in range(array_size):
#     numbers.append(randint(1, 10))
# print(f"Список - {numbers}")

# if array_size % 2 == 0:
#     for i in range(int(array_size / 2)):
#         multiplied.append(numbers[i] * numbers[-i - 1])
# else:
#     for i in range(int(array_size / 2 + 1)):
#         multiplied.append(numbers[i] * numbers[-i - 1])

# print(f"Пары чисел - {multiplied}")



# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import uniform

# array_size = int(input("Введите количество чисел в списке: "))
# float_numbers = []

# for i in range(array_size):
#     float_numbers.append(round(uniform(1, 10), 2))
# print("Список вещественных чисел", float_numbers)

# for i in range(array_size):
#     float_numbers[i] = float_numbers[i] - int(float_numbers[i])
# float_numbers.sort()
# dif_numbers = float_numbers[-1] - float_numbers[0]
# print(f"Разница : {round(dif_numbers, 2)}")








