#Задание 1
print("Задание 1")

ex1_temperature = int(input("Введите температуру: "))
if ex1_temperature >= 20:
    print("Кондиционер выключен")
else:
    print("Кондиционер включен")


#Задание 2
print("Задание 2")
ex2_month = int(input("Введите номер месяца: "))
if ex2_month <= 2 or ex2_month == 12:
    print("Это зима")
if ex2_month >= 3 and ex2_month <= 5:
    print("Это весна")
if ex2_month >= 6 and ex2_month <= 8:
    print("Это лето")
if ex2_month >= 9 and ex2_month <= 11:
    print("Это осень")

    
#Задание 3
print("Задание 3")
ex3_res = 0
try:
    ex3_age = float(input("Введите возраст собаки (в годах): "))
except ValueError:
    print("вы ввели не число")
if ex3_age >= 1:
    if ex3_age >= 2:
        ex3_res = 2*10.5+(ex3_age-2)*4
    else:
        ex3_res = 10.5
    print(f"Возраст собаки в человеческих годах: {ex3_res}")
    
else:
    print("Ошибка: возраст должен быть не меньше 1")

#Задание 4
print("Задание 4")
ex4_num = input("Введите число: ")
ex4_res = "не "
if int(ex4_num[-1]) % 2 == 0:
    ex4_sum = 0
    for n in ex4_num:
        ex4_sum += int(n)
    if ex4_sum % 3 == 0:
        ex4_res = ""
print(f"Число {ex4_num} {ex4_res}делится на 6")

#Задание 5
print("Задание 5")
ex5_const = [
    [" строчные буквы,",'abcdefghijklmnopqrstuvwxyz'],
    [" заглавные буквы,",'ABCDEFGHIJKLMNOPQRSTUVWXYZ'],
    [" цифры,",'1234567890'],
    [" спецсимволы",'!@#$%^&*()./,~`']
]
ex5_password = input("Введите пароль: ")
if len(ex5_password) >= 8:
    ex5_res = "Пароль ненадежный: отсутствуют"
    for arr in ex5_const:
        ex5_sat = 0
        for l in arr[1]:
            if l in ex5_password:
                ex5_sat += 1
        if ex5_sat == 0:
            ex5_res += arr[0]
    if ex5_res == "Пароль ненадежный: отсутствуют":
        ex5_res = "Пароль надежный"
    print(ex5_res)
else:
    print("Длина пароля должна быть более 8 символов")

#Задание 6
print("Задание 6")

ex6_year = int(input("Введите год: "))
if ex6_year % 4 == 0 and ex6_year % 100 != 0 or ex6_year % 400 = 0:
    print(f"{ex6_year} - високосный год")
else:
    print(f"{ex6_year} - не високосный год")


#Задание 7
print("Задание 7")

ex7_nums = input("Введите три числа через пробел: ").split()
ex7_min = ex7_nums[0]
for n in ex7_nums:
    if float(n) < float(ex7_min):
        ex7_min = n
print(f"Минимальное число из трех - {ex7_min}")

#Задание 8
print("Задание 8")
ex8_percent = 0
ex8_summ = float(input("Введите сумму покупки: "))
if ex8_summ >= 1000:
    ex8_percent = 5
if ex8_summ >= 5000:
    ex8_percent = 10
if ex8_summ >= 10000:
    ex8_percent = 15
print(f"Ваша скидка {ex8_percent}%")
print(f"К оплате {ex8_summ - ex8_summ*ex8_percent/100}")


#Задание 9
print("Задание 9")

ex9_hour = int(input("Введите час (0–23): "))
ex9_res = "ночь"
if ex9_hour >= 6:
    ex9_res = "утро"
if ex9_hour >= 12:
    ex9_res = "день"
if ex9_hour >= 18:
    ex9_res = "вечер"
if ex9_hour >= 23:
    ex9_res = "обижусь и вообще ничего делать не буду, нормально же попросил 0-23 ввести" 
print(f"Сейчас {ex9_res}")

#Задание 10
print("Задание 10")

ex10_num = int(input("Введите число: "))
ex10_res = f"Число {ex10_num} - простое"
for n in range(2,int(ex10_num**0.5)):
    if ex10_num % n == 0:
        ex10_res = f"Число {ex10_num} - составное"
        break
print(ex10_res)
