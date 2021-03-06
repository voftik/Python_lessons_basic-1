
__author__ = 'Новосёлов Владимир Евгеньевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

n = float(input("Введите любое целое число: "))

if n % 1 == 0:
    n = int(n)
    n = str(n)
    i = 0
    while  i < len(n):
        print(n[i])
        i += 1

else:
    print("Вы ввели не целое число")

# вариант решения с использованием арифметики

n = float(input("Введите любое целое число: "))

if n%1 == 0:
    n = int(n)
    while n != 0:
        digit = n % 10
        print(digit)
        n = n // 10

else:
    print("Вы ввели не целое число")


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input("Введите число А: ")
b = input("Введите число B " )
c = a
a = b
b = c
print('Знчениение числа А стало ', a)
print('Знчениение числа B стало ', b)

# Варинат через арифмитическое действие

a = input("Введите число А: ")
b = input("Введите число B " )
a = a + b
b = a - b
a = a - b
print('Знчениение числа А стало ', a)
print('Знчениение числа B стало ', b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

access = None
name = int(input('Введите ваш возраст:'))
if name >= 18:
    access = 1
    print('Доступ разрешен')
else:
    access = 0
print('Извините, пользование данным ресурсом только с 18 лет')
