#Задание 1
print("Задание 1")

ex1_converter_dictionary = {
    's': 1,
    'm': 60,
    'h': 3600
}
def ex1_convert(convert_from,convert_to_unit):
    return f"{float((ex1_converter_dictionary[convert_from[-1]]*float(convert_from[0:len(convert_from)-1]))/ex1_converter_dictionary[convert_to_unit])}{convert_to_unit}"
print(ex1_convert("12s", "h"),2)
#description
#Функция `ex1_convert_time` принимает числовое значение, исходную единицу измерения и целевую единицу измерения. Она использует словарь `ex1_converter_dictionary` для хранения коэффициентов перевода всех поддерживаемых единиц (секунды, минуты, часы) в секунды. Сначала значение конвертируется в секунды, а затем из секунд в целевую единицу. Результат возвращается в виде числа.

#Задание 2
print("Задание 2")


def ex2_calculate_profit(amount,years):
    percent = 0
    if years <= 3:
        percent = 3
    elif 4 <= years <= 6:
        percent = 5
    else:
        percent = 2

    if amount < 30000:
        return "Сумма вклада не может быть меньше 30000"
    if years < 1:
        return "Срок не может быть меньше года"
    
    percent += min(amount//10000*0.3,5)

    profit = amount
    for _ in range(years):
        profit += profit * percent/100
    return round(profit-amount,2)
print(ex2_calculate_profit(30000,3))
#description
#Функция `ex2_calculate_profit` рассчитывает прибыль по вкладу с учетом сложного процента. Она принимает начальную сумму вклада и количество лет. Сначала определяется базовая процентная ставка в зависимости от срока вклада, затем рассчитывается дополнительный бонус к ставке в зависимости от суммы вклада (с ограничением в 5%). Итоговая годовая ставка применяется к текущей сумме вклада в каждом году. Возвращается общая прибыль (без учета первоначальной суммы) округленная до двух знаков после запятой. Обрабатывается минимальный вклад и некорректное количество лет.

#Задание 3
print("Задание 3")

def ex3_is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def ex3_primes_in_range(a,b):
    primes = []
    if a>b:
        return "Начало диапазона больше конца"
    
    for n in range(a,b+1):
        if ex3_is_prime(n):
            primes.append(n)

    if not primes:
        return "В диапазоне нет простых чисел"
    return primes
print(ex3_primes_in_range(1,123))
#description
#Функция `ex3_primes_in_range` находит все простые числа в заданном диапазоне (включительно). Вспомогательная функция `ex3_is_prime` проверяет, является ли число простым, путем деления на числа от 2 до квадратного корня из числа. Основная функция проверяет входные данные на корректность. Если диапазон не содержит простых чисел или входные данные некорректны, возвращается сообщение об ошибке. В противном случае возвращается массив с простыми числами.

#Задание 4
print("Задание 4")
def ex4_matrices_add():
    dimension = int(input())
    m1 = []
    for i in range(dimension):
        m1.append([])
        nums = input().split(" ")
        for n in nums:
            m1[i].append(float(n))

    m2 = []
    for i in range(dimension):
        m2.append([])
        nums = input().split(" ")
        for n in nums:
            m2[i].append(float(n))

    newMatrix = []
    for i in range(dimension):
        newMatrix.append([])
        for j in range(dimension):
            newMatrix[i].append(m1[i][j]+m2[i][j])
            print(m1[i][j]+m2[i][j],end=" ")
        print()
    return newMatrix
ex4_matrices_add()
#description
#Функция `ex4_matrices_add` выполняет сложение двух квадратных матриц. Она принимает размерность `di` и две матрицы в виде списков списков. Создается новая матрица, каждый элемент которой является суммой соответствующих элементов исходных матриц. Результат форматируется в виде строк, разделенных пробелами и переводами строки.

#Задание 5
print("Задание 5")

def ex5_is_palindrome(input_string):
    unneeded_symbols = ",!?. ;-'\""
    formated_string = input_string.lower()
    for s in unneeded_symbols:
        formated_string = formated_string.replace(s,"")
    formated_string = formated_string.strip()
    return formated_string == formated_string[::-1]

input_str = "abcdeftregfer"
print(ex5_is_palindrome(input_str))
#description
#Функция `ex5_is_palindrome` определяет, является ли входная строка палиндромом. Она игнорирует регистр, пробелы и знаки препинания. Сначала строка переводится в нижний регистр, затем удаляются все лишние символы. После этого очищенная строка сравнивается со своей перевернутой версией. Если они совпадают, возвращается True, иначе - False.