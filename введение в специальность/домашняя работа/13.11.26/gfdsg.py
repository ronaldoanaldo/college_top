# Домашнее задание: Модуль 3. Циклы. Часть 2 (Начальный уровень)

# ==========================================
# Задание 1
# Посчитать отдельно сумму четных, нечетных и чисел, кратных 9 в указанном диапазоне,
# а также среднеарифметическое каждой группы.
# ==========================================
print("--- Задание 1 ---")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

sum_even = 0
sum_odd = 0
sum_9 = 0

count_even = 0
count_odd = 0
count_9 = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        sum_even = sum_even + i
        count_even = count_even + 1
    else:
        sum_odd = sum_odd + i
        count_odd = count_odd + 1

    if i % 9 == 0:
        sum_9 = sum_9 + i
        count_9 = count_9 + 1

print("Сумма четных:", sum_even)
if count_even > 0:
    print("Среднее четных:", sum_even / count_even)
else:
    print("Среднее четных: 0")

print("Сумма нечетных:", sum_odd)
if count_odd > 0:
    print("Среднее нечетных:", sum_odd / count_odd)
else:
    print("Среднее нечетных: 0")

print("Сумма кратных 9:", sum_9)
if count_9 > 0:
    print("Среднее кратных 9:", sum_9 / count_9)
else:
    print("Среднее кратных 9: 0")


# ==========================================
# Задание 2
# Отобразить на экране вертикальную линию из введенного символа указанной длины.
# ==========================================
print("\n--- Задание 2 ---")
length = int(input("Введите длину линии: "))
symbol = input("Введите символ: ")

i = 0
while i < length:
    print(symbol)
    i = i + 1


# ==========================================
# Задание 3
# Определить знак вводимых чисел. При вводе 7 завершить работу и вывести "Good bye!".
# ==========================================
print("\n--- Задание 3 ---")
num = int(input("Введите число: "))

while num != 7:
    if num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")

    num = int(input("Введите число: "))

print("Good bye!")


# ==========================================
# Задание 4
# Подсчитывать сумму, максимум и минимум введенных чисел.
# При вводе 7 завершить работу и вывести "Good bye!".
# ==========================================
print("\n--- Задание 4 ---")
num = int(input("Введите число: "))

if num == 7:
    print("Good bye!")
else:
    total_sum = num
    max_num = num
    min_num = num

    while True:
        num = int(input("Введите число: "))

        if num == 7:
            print("Good bye!")
            break

        total_sum = total_sum + num

        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    print("Сумма:", total_sum)
    print("Максимум:", max_num)
    print("Минимум:", min_num)
