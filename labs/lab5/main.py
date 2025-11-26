#Задание 1
print("Задание 1")

ex1_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if 3 in ex1_numbers:
    ex1_index = ex1_numbers.index(3)
    ex1_numbers[ex1_index] = 30
print(ex1_numbers)

#description
#*Код ищет число 3 в заданном списке и заменяет его на 30, используя метод index() для определения позиции числа.*

#Задание 2
print("Задание 2")

ex2_numbers = [1, 2, 3, 4, 5]
ex2_squares = [num ** 2 for num in ex2_numbers]
print(ex2_squares)

#description
#*Код создает новый список, где каждый элемент является квадратом соответствующего элемента из исходного списка, используя генератор списков.*

#Задание 3
print("Задание 3")

ex3_numbers = [10, 2, 8, 15, 3, 7]
if ex3_numbers:
    ex3_max_number = max(ex3_numbers)
    ex3_result = ex3_max_number / len(ex3_numbers)
    print(ex3_result)
else:
    print("Список пуст.")

#description
#*Код находит наибольшее число в списке и делит его на общее количество элементов в этом списке, выводя результат.*

#Задание 4
print("Задание 4")

def ex4_sort_tuple(input_tuple):
    if all(isinstance(x, (int, float)) for x in input_tuple):
        return tuple(sorted(input_tuple))
    else:
        return input_tuple

ex4_elements_numeric = (5, 2, 8, 1, 9)
ex4_elements_mixed = (5, "a", 8, 1, 9)

print(ex4_sort_tuple(ex4_elements_numeric))
print(ex4_sort_tuple(ex4_elements_mixed))

#description
#*Функция проверяет, состоят ли все элементы кортежа из чисел. Если да, она возвращает отсортированный кортеж; в противном случае кортеж остается неизменным.*

#Задание 5
print("Задание 5")

ex5_products = {"яблоки": 120, "молоко": 80, "хлеб": 40, "сыр": 350, "масло": 150}

if ex5_products:
    ex5_min_price_item = min(ex5_products, key=ex5_products.get)
    ex5_max_price_item = max(ex5_products, key=ex5_products.get)
    print(f"Товар с минимальной ценой: {ex5_min_price_item} ({ex5_products[ex5_min_price_item]} руб.)")
    print(f"Товар с максимальной ценой: {ex5_max_price_item} ({ex5_products[ex5_max_price_item]} руб.)")
else:
    print("Словарь товаров пуст.")

#description
#*Код находит товары с самой низкой и самой высокой ценой в словаре, используя функции min() и max() с ключом для сравнения значений.*

#Задание 6
print("Задание 6")

ex6_elements = ["apple", 123, True, None, 3.14]
ex6_new_dict = {item: item for item in ex6_elements}
print(ex6_new_dict)

#description
#*Код создает новый словарь, где каждый элемент исходного списка становится одновременно ключом и значением в словаре, используя генератор словарей.*

#Задание 7
print("Задание 7")

ex7_en_ru_dict = {"hello": "привет", "world": "мир", "python": "питон", "cat": "кошка", "dog": "собака"}

def ex7_translate_ru_to_en(ru_word, dictionary):
    for en, ru in dictionary.items():
        if ru == ru_word.lower():
            return en
    return "Перевод не найден."

ex7_search_word = "мир"
print(f"Перевод '{ex7_search_word}' на английский: {ex7_translate_ru_to_en(ex7_search_word, ex7_en_ru_dict)}")
#description
#*Функция принимает русское слово и словарь (английский:русский), затем ищет русское слово среди значений и возвращает соответствующий английский ключ. Если слово не найдено, сообщает об этом.*

#Задание 8
print("Задание 8")
from random import randint

ex8_rules = {
    0:(1,3),
    1:(2,3),
    2:(0,4),
    3:(2,4),
    4:(1,0)
}
ex8_variants = ("камень","ножницы","бумага","ящерица","спок")
ex8_player_var = int(input("Выбор должен быть сделан\n1 - камень\n2 - ножницы\n3 - бумага\n4 - ящерица\n5 - спок\n"))-1
ex8_computer_var = randint(0,4)
print(f"""{ex8_variants[ex8_player_var]}
vs
{ex8_variants[ex8_computer_var]}""")

if ex8_player_var == ex8_computer_var:
    print("ничья")
elif ex8_player_var in ex8_rules[ex8_computer_var]:
    print("компьютер победил")
else:
    print("игрок победил")

#description
# *Код реализует игру Камень-Ножницы-Бумага-Ящерица-Спок. Пользователь вводит свой выбор, компьютер делает случайный выбор. Программа определяет победителя на основе заданных правил и выводит результат.*

#Задание 9
print("Задание 9")

ex9_words = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]
ex9_grouped_words = {}

for ex9_word in ex9_words:
    ex9_first_letter = ex9_word[0]
    if ex9_first_letter not in ex9_grouped_words:
        ex9_grouped_words[ex9_first_letter] = []
    ex9_grouped_words[ex9_first_letter].append(ex9_word)

print(ex9_grouped_words)

#description
#*Код проходит по списку слов, извлекает первую букву каждого слова. Затем создает словарь, где ключом является эта первая буква, а значением — список всех слов, начинающихся с этой буквы.*

#Задание 10
print("Задание 10")

ex10_students_data = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5]), ("Петр", [4, 5, 4])]

ex10_average_grades = {}
for ex10_name, ex10_grades in ex10_students_data:
    if ex10_grades:
        ex10_average_grades[ex10_name] = sum(ex10_grades) / len(ex10_grades)
    else:
        ex10_average_grades[ex10_name] = 0.0

print("Средние оценки студентов:", ex10_average_grades)

if ex10_average_grades:
    ex10_best_student = max(ex10_average_grades, key=ex10_average_grades.get)
    ex10_max_avg_grade = ex10_average_grades[ex10_best_student]
    print(f"{ex10_best_student} имеет наивысший средний балл: {ex10_max_avg_grade:.1f}")
else:
    print("Нет данных о студентах.")

#description
#*Код сначала создает словарь, сопоставляя каждому студенту его средний балл на основе списка оценок. Затем он находит студента с наивысшим средним баллом в этом словаре и выводит его имя и соответствующий балл.*