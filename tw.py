def repeat():
    while True:

        enter = input('Сыграем ещё раз? ')

        if enter.lower() in 'да':
            return 'да'
        elif enter.lower() in 'нет':
            print('До встречи!')
            return 'нет'
        else:
            print('Я вас не понимаю. Введите свой ответ заново')


game_replay = 'да'
win = 0
answer = randint(0, 100)
counter = ceil(log(100, 2))
