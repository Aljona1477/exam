# 1. Напишите функцию, которая будет принимать номер
# кредитной карты и показывать только последние 4 цифры.
# Остальные цифры должны заменяться звездочками.

def credit_card(number):
    for i in range(len(number)):
        if i <=7:
            print('*', end='')
        else:
            print(number[i], end='')
credit_card('147852369147')

