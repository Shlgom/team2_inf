print('Добро пожаловать в числовую угадайку')
print(f'В этой игре случайным образом выбирается число '
      f'в диапазоне от 0 до 100. Попробуйте отгадать его. '
      f'У вас {counter} попыток')

while game_replay in 'да':
    user_answer = is_valid()

    if user_answer < answer:
        counter -= 1
        print(f'Слишком мало, попробуйте еще раз. '
              f'У вас осталось {counter} попыток')
    elif user_answer > answer:
        counter -= 1
        print(f'Слишком много, попробуйте еще раз. '
              f'У вас осталось {counter} попыток')
    else:
        print('Вы угадали, поздравляем!')
        win = 1

    if counter > 0 and win == 0:
        continue
    elif counter == 0:
        print(f'К сожалению попытки закончились '
              f'раньше, чем вы смогли отгадать число {answer}')

    game_replay = repeat()
