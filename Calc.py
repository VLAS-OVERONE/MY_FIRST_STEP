cycle = input("Чтобы начать, введите 1")
res = 0
while cycle == "1":
    num1 = float(input("Введите первое действительное число..."))
    sym = input("Введите арифметическое действие ( +; -; *; /)")
    if sym == "+" or sym == "-" or sym == "*" or sym == "/":
        num2 = float(input("Введите второе действительное число..."))
    if sym == "/" and num2 == 0:
        print("Деление на 0 невозможно!!!")
        num2 = float(input("Введите второе действительное число, отличное от нуля..."))
    if sym == "+":
        res = num1 + num2
    elif sym == "-":
        res = num1 - num2
    elif sym == "*":
        res = num1 * num2
    elif sym == "/":
        res = num1 / num2
    else:
        print("Вы ввели некорректные данные")
    print("Результат", res)
    cycle = input("Чтобы продолжить, введите 1")
else:
    print("Вычисления окончены")
print("Спасибо, что воспользовались моей программой")