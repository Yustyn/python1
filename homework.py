print('''
    Скласти програму ’Атракціони’.
    Програма запитує суму (грн.) у користувача.
    Потім виводить на екран перелік доступних атракціонів.
    Користувач обирає атракціон та ’оплачує’ його.
    Вихід з програми при виборі пункту ’вихід’ або при недостатній сумі грошей.
''')


sum = int(input('Введіть суму грн користувача: '))
karusel = 200
goida = 150
mashinki = 250
nedostacha = '''
>>> Недостатньо грошей. Виберіть інший атракціон <<<'''

while sum >= karusel or sum >= goida or sum >= mashinki:
    print('''
Доступні кошти: {}
Виберіть атракціон:
1. Гойдалки 150 грн
2. Карусель 200 грн
3. Машинки  250 грн
0. Вихід
        '''.format(sum))

    ask = input('Введіть пункт меню: ')
    try:
        if int(ask) == 0:
            print('Повертайтеся ще!')
            break
        elif int(ask) == 1:
            if (sum - goida) > 0:
                sum -= goida
            else:
                print(nedostacha)
        elif int(ask) == 2:
            if (sum - karusel) > 0:
                sum -= karusel
            else:
                print(nedostacha)
        elif int(ask) == 3:
            if (sum - mashinki) > 0:
                sum -= mashinki
            else:
                print(nedostacha)
    except:
        pass

print('''
Скласти програму ’Банкомат’.
Програма запитує пароль (у вигляді числа) у користувача.
Якщо пароль вірний, то працює меню з пунктів:
поточний баланс, зняти гроші, вихід''')

password_true = input('Встановіть пароль: ')
password_ask = input('Введіть пароль: ')
money = 10000
menu = '''
1. Переглянути баланс
2. Зняти гроші
0. Вийти
'''

if password_ask == password_true:
    print('Вас вітає банк "It Step Foundation"')
    print(menu)
    ask = input('Введіть пункт меню: ')
    while int(ask != 0):
        try:
            if int(ask) == 1:
                print('У вас на рахунку {}грн'.format(money))
            elif int(ask) == 2:
                sum_get = input('Введіть суму, яку Ви бажаєте зняти: ')
                if int(sum_get) > 0 and int(sum_get) < money:
                    print('Будь ласка, заберіть ваші {}грн'.format(sum_get))
                    money -= int(sum_get)
                else:
                    print('Невірно введені дані')
            elif int(ask) == 0:
                print('Вдалого вам дня!')
                break

            ask = input('Введіть пункт меню: ')
        except:
            pass
else:
    print('Невірний пароль!')


print('''
Користувач вказує ціну однієї хвилини вихідного дзвінка з одного
мобільного оператора іншому, а також тривалість розмови.
Необхідно обрахувати грошову сумму, на яку був здійснений дзвінок
''')

cina = float(input('Введіть ціну однієї хвилини дзвінка: '))
trivalist = float(input('Введіть тривалість розмови в хвилинах: '))

print('Вартість дзвінка становитиме:', round(cina * trivalist, 2))


print("""
Написати програму, яка переводить повний оберт
планети Марс навколо Сонця в земні роки. Оберти ввести з клавіатури.
(Марс робить повний оберт навколо Сонця за 686 земних днів)
""")

obert = float(input('Введіть кількість обертів Марсу: '))
year = 686

if obert > 0:
    print('Марс зробить {} обертів за {} земних днів'.format(obert, obert*year))
