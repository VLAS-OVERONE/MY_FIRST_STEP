# Пользователя просят ввести его возраст. Проверка на ошибки try - except - raise:

def age(data):
    if data.isnumeric():
        data = int(data)
        if 0<= data <= 150:
            return data
        else:
            raise ValueError
    else:
        raise TypeError
try:
    s = age(input("Введите свой возраст:"))
except ValueError:
    print("Введите корректное значение возраста")
except TypeError:
    print("Введите числовое значение возраста")
print("Программа завершена!")