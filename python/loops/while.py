number = int(input("Введіть число: "))
temp_number = abs(number)  # Для коректної роботи з від'ємними числами
sum_digits = 0

while temp_number > 0:
    digit = temp_number % 10   # Отримуємо останню цифру
    sum_digits += digit        # Додаємо її до суми
    temp_number //= 10         # Видаляємо останню цифру

print("Сума цифр числа =", sum_digits)
