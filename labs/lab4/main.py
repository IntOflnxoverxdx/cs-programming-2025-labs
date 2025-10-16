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
    
# print(f"Это {ex2_months[int(ex2_month/4)]}")