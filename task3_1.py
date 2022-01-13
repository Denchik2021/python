def num_translate(number_en):  # функция принимает аргументом число в анг. языке и возвращает его перевод
    num_en = ''
    if number_en == 'one':
        num_en = 'один'
    elif number_en == 'two':
        num_en = 'два'
    elif number_en == 'three':
        num_en = 'три'
    elif number_en == 'four':
        num_en = 'четыре'
    elif number_en == 'five':
        num_en = 'пять'
    elif number_en == 'six':
        num_en = 'шесть'
    elif number_en == 'seven':
        num_en = 'семь'
    elif number_en == 'eight':
        num_en = 'восемь'
    elif number_en == 'nine':
        num_en = 'девять'
    elif number_en == 'ten':
        num_en = 'десять'
    else:
        print('непонятный ввод')
        exit('выход из функции')
    return 'ваше число: ' + num_en


x_num = str(input('Введите число от 1 до 10 на английском '
              'и получишь его перевод: '))  # просим ввод числа
number_en = x_num  # присваем введенное текстовое число переменной number_en

print(num_translate(number_en))  # вызываем функцию//// почему то без printa она у меня не вызывалась :-)
