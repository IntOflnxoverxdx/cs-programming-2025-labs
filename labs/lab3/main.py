# Задание 1
print("Задание 1")
ex1_name =  (input("Введите ваше имя: "))
ex1_age = int((input("Введите ваш возраст (целым числом): ")))
for i in range(10):
    print(f"{i+1}. Меня зовут {ex1_name}, мне {ex1_age} лет")

# Задание 2
print("\n\nЗадание 2")
ex2_num = -1
while not (ex2_num >= 1 and ex2_num <= 9):
    try:
        ex2_num = int(input("Введите число от 1 до 9 (таблица умножения): "))
    except ValueError:
        print("Вы ввели не число")
    if not (ex2_num >= 1 and ex2_num <= 9):
        print("Число от 1 до 9")
print(f"Таблица умножения для числа {ex2_num}")
for i in range(1,10):
    print(f"{ex2_num} * {i} = {ex2_num*i}")

# Задание 3
print("\n\nЗадание 3")
i = 0
while i <= 100:
    print (i)
    i+= 3

# Задание 4
print("\n\nЗадание 4")
ex4_num = int(input("Введите целое число (факториал): "))
ex4_result = 1 
i = 1
while i <= ex4_num:
    ex4_result *= i
    i += 1
print(ex4_result)

# Задание 5
print("\n\nЗадание 5")
i = 20
while i >= 0:
    print(i)
    i -= 1


# Задание 6
print("\n\nЗадание 6")
ex6_a = 0
ex6_b = 1
ex6_num = int(input("Введите число (для чисел фибоначчи): "))
print(ex6_a)
print(ex6_b)
while ex6_a+ex6_b <= ex6_num:
    print(ex6_a+ex6_b)
    ex6_a,ex6_b = ex6_b,ex6_a+ex6_b

# Задание 7
print("\n\nЗадание 7")
ex7_text = input("Введите строку (П1р2и3в4е5т6): ")
ex7s_res = ""
for i in range(len(ex7_text)):
    ex7s_res += ex7_text[i]+str(i+1)
print(ex7s_res)

# Задание 8
print("\n\nЗадание 8")

ex8_in = ""
while ex8_in != "q":
    try:
        ex8_in = input("Введите два числа через пробел: ")
        ex8_a,ex8_b = ex8_in.split(" ")
        print(f"Сумма равна: {float(ex8_a)+float(ex8_b)}")
    except Exception as e:
        print(f"Неправильный формат данных ({e})")
