# Задание 1
print("Задание 1")
ex1_var_int = 2
ex1_var_float = 2.4
ex1_var_str = "string"
ex1_var_bool = True
print(ex1_var_int)
print(ex1_var_float)
print(ex1_var_str)
print(ex1_var_bool)





# Задание 2
print("\n\nЗадание 2")
ex2_name = "Кирилл"
ex2_age = 19
print(ex2_name,ex2_age)

# Задание 3
print("\n\nЗадание 3")
ex3_1 = 342
ex3_2 = 56.2
ex3_3 = '43'
ex3_sum = ex3_1 + ex3_2 + int(ex3_3) #Хотел написать float на всякий случай, но пока оставлю так
print(ex3_sum)


# Задание 4
print("\n\nЗадание 4")
ex4_a = 3
ex4_b = 8
ex4_res = (ex4_a + 4*ex4_b)*(ex4_a - 3*ex4_b) + ex4_a**2
print(ex4_res)

# Задание 5
print("\n\nЗадание 5")
def ex5_calculate_square():
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))
    square = a*b
    print(square)
    return square
ex5_calculate_square()

# Задание 6
print("\n\nЗадание 6")
print("""*   *   *
 * * * *
  *   *""")

# Задание 7
print("\n\nЗадание 7")
ex7_a = 43
ex7_b = 2.4
# операции арифметические
print(ex7_a+ex7_b)
print(ex7_a-ex7_b)
print(ex7_a*ex7_b)
print(ex7_a/ex7_b)
print(ex7_a//ex7_b)
print(ex7_a%ex7_b)
print(ex7_a**ex7_b)

# операции сравнения
print(ex7_a==ex7_b)
print(ex7_a!=ex7_b)
print(ex7_a>=ex7_b)
print(ex7_a<=ex7_b)
print(ex7_a<ex7_b)
print(ex7_a>ex7_b)

# Задание 8
print("\n\nЗадание 8")
ex8_name = "Кирилл"
ex8_age = 19
print(f"Меня зовут {ex8_name}, мне {ex8_age} лет.")

# Задание 9
print("\n\nЗадание 9")
ex9_string = "Съешь еще этих мягких французских булок, да выпей чаю"
ex9_parts = ex9_string.split(" ")
ex9_res = ""
for word in ex9_parts:
    ex9_res += f"{word} "
ex9_res = word.strip()
print(ex9_res)

# Задание 10
print("\n\nЗадание 10")
print("Нет! Да!"*4)

# Задание 11
print("\n\nЗадание 11")
ex11_x,ex11_y,ex11_z = input("Введите три числа в формате x,y,z: ").split(",")
ex11_res = (float(ex11_x)+float(ex11_z))//float(ex11_y)
print(f"Результат вычисления:\n{ex11_res}")

# Задание 12
print("\n\nЗадание 12") 
ex12_word = ""
while len(ex12_word) < 10:
    ex12_word = input("Введите слово от 10 символов: ")

print(ex12_word[0:4])
print(ex12_word[::-1][0:2][::-1])
print(ex12_word[3:8])
print(ex12_word[::-1])





input() # чтобы не закрылся терминал