# Реализуйте следующую функцию:
# add_everything_up, будет складывать числа(int, float) и строки(str)


def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError as exc:
        print(f'Ошибка {exc}: {a}{b} ')

    else:
        print(f'Ошибки нет, результат: {result} ')

    finally:
        print("Работа закончена")


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))