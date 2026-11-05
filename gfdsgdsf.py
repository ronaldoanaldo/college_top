import random

# Исходный список, заполненный случайными числами от -50 до 50
numbers = [random.randint(-50, 50) for _ in range(20)]
print(f"Исходный список: {numbers}\n")

# ==========================================
# ЗАДАНИЕ 1
# ==========================================
print("--- Задание 1 ---")

# 1. Сумма отрицательных чисел
sum_negative = sum(x for x in numbers if x < 0)
print(f"Сумма отрицательных чисел: {sum_negative}")

# 2. Сумма четных чисел
sum_even = sum(x for x in numbers if x % 2 == 0)
print(f"Сумма четных чисел: {sum_even}")

# 3. Сумма нечетных чисел
sum_odd = sum(x for x in numbers if x % 2 != 0)
print(f"Сумма нечетных чисел: {sum_odd}")

# 4. Произведение элементов с индексами, кратными 3
prod_idx_3 = 1
for i in range(0, len(numbers), 3):
    prod_idx_3 *= numbers[i]
print(f"Произведение элементов с индексами кратыми 3: {prod_idx_3}")

# 5. Произведение элементов между минимальным и максимальным элементом
min_idx = numbers.index(min(numbers))
max_idx = numbers.index(max(numbers))

start_idx = min(min_idx, max_idx) + 1
end_idx = max(min_idx, max_idx)

prod_between_min_max = 1
if start_idx < end_idx:
    for i in range(start_idx, end_idx):
        prod_between_min_max *= numbers[i]
else:
    prod_between_min_max = 0 # Элементов между ними нет
print(f"Произведение элементов между min и max (индексы {min_idx} и {max_idx}): {prod_between_min_max}")

# 6. Сумма элементов между первым и последним положительными элементами
pos_indices = [i for i, x in enumerate(numbers) if x > 0]
sum_between_pos = 0

if len(pos_indices) >= 2:
    first_pos = pos_indices[0]
    last_pos = pos_indices[-1]
    sum_between_pos = sum(numbers[first_pos + 1 : last_pos])
    print(f"Сумма элементов между первым и последним положительными: {sum_between_pos}")
else:
    print("Сумма элементов между положительными: Недостаточно положительных элементов")


# ==========================================
# ЗАДАНИЕ 2
# ==========================================
print("\n--- Задание 2 ---")

# 1. Список, содержащий только четные числа
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Четные числа: {even_numbers}")

# 2. Список, содержащий только нечетные числа
odd_numbers = [x for x in numbers if x % 2 != 0]
print(f"Нечетные числа: {odd_numbers}")

# 3. Список, содержащий только отрицательные числа
negative_numbers = [x for x in numbers if x < 0]
print(f"Отрицательные числа: {negative_numbers}")

# 4. Список, содержащий только положительные числа
positive_numbers = [x for x in numbers if x > 0]
print(f"Положительные числа: {positive_numbers}")
