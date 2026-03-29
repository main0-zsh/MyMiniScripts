from random import*
print('Привет! Давай поиграем в "Камень, Ножницы, Бумага" ')
print('Правила простые: Выбираешь что-то любое из камня, ножниц или бумаги, а компьютер тоже выбирает что-то рандомное из этих троих.')
print('ВАЖНО: Камень бьет ножницы, ножницы бьют бумагу, а бумага бьет камень.')
print('Если тебя, так скажем, побили, то компьютер выигрывает и также наоборот(так ты играешь до 3 баллов)')
player_ball=0
computer_ball=0
очки=f'{player_ball}:{computer_ball}'
def determine_winner():
    global player_ball, computer_ball
    while player_ball<3 and computer_ball<3:
        выбор_гостя = input('Введи свой вариант:')
        computer_choice = choice(['камень', 'ножницы', 'бумага'])
        if выбор_гостя.lower()=="камень" and computer_choice=='ножницы' or выбор_гостя.lower()=='ножницы' and computer_choice=='бумага' or выбор_гостя.lower()=='бумага' and computer_choice=="камень":
            player_ball+=1
            print(f"Компьютер выбрал: {computer_choice}")
            print(f"Ты выйграл этот раунд! {player_ball}:{computer_ball}")
        elif выбор_гостя.lower()==computer_choice:
            print(f"Компьютер выбрал: {computer_choice}")
            print(f"Ничья!Счет {player_ball}:{computer_ball}")
        else:
            computer_ball+=1
            print(f"Компьютер выбрал: {computer_choice}")
            print(f"Вы проиграли!Счет {player_ball}:{computer_ball}")
    if computer_ball >= 3:
        print(f"Итог: {player_ball}:{computer_ball}. К сожалению, вы проиграли.")
    else:
        print(f"Итог: {player_ball}:{computer_ball}. Поздравляю, вы выиграли!")
determine_winner()