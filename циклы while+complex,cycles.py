import random

print("Угадайте число от 1 до 100")
number=random.randint(1,100)
guess_number=int(input("Твой вариант:"))
while guess_number!=number:
    if guess_number>number:
        print("К сожалению, ваш ответ не верен. Попробуйте еще раз."
              "(Подсказка:Загаданное число меньше)")
        guess_number=int(input("Твой вариант:"))
    else:
        print("К сожалению, ваш ответ не верен. Попробуйте еще раз."
              "(Подсказка:Загаданное число больше)")
        guess_number=int(input("Твой вариант:"))
print("Поздравляю!Ваш ответ полностью соответсвует загаданному числу.")

число=(int(input("Хочешь сделать пирамиду из чисел? Введи любое число:")))
for линия in range(число+1):
    for ряд in range(линия):
        print(линия,end=' ')
    print(' ')