from random import *
from time import*
import json

current_user=None

try:
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    users = {}

def register():
    print('Ты также можешь выйти на главное меню, написав "stop"')
    user_name=input('Введи свой никнейм, он должен быть уникальным:')
    if user_name in users:
        print("Этот никнейм существует.")
        user_name = input('Введи свой никнейм, он должен быть уникальным:')
    elif user_name.lower()=='stop':
        return
    else:
        user_password = input('Введи свой пароль, он должен быть не короче 5 символов и должен содержать латинские буквы и цифры:')
        if len(user_password)>=5 and user_password.isalnum():
            users[user_name] ={"password":user_password,"cards":{}}
            global current_user
            current_user=user_name
            print("Добро пожаловать!")
            with open("users.json", "w") as file:
                json.dump(users, file, ensure_ascii=False)
        else:
            print("Пароль не подходит нормам")
def login():
    print('Ты также можешь выйти на главное меню, написав "stop"')
    exist_username=(input("Введи свой никнейм:"))
    if exist_username in users:
        exist_password=input('Введи свой пароль:')
        if exist_password==users[exist_username]["password"]:
            global current_user
            current_user=exist_username
            print("Добро пожаловать!")
        else:
            print("Неверный пароль.")
    elif exist_username.lower()=="stop":
        return
    else:
        print("Пользователя не существует")
def viktorina():
    stop_flag=""
    while stop_flag != 'stop':
        stop_flag = input("Введи'stop' чтобы закончит добавление карточек, Enter чтобы продолжть")
        if len(users[current_user]["cards"])==0:
            print('Создай карточки')
            return
        elif stop_flag=='stop':
            break
        else:
            questian = choice(list(users[current_user]["cards"].keys()))
            print(questian)
            t1=time()
            answerr=input('Введите свой ответ:')
            t2=time()
            rezultat=t2-t1

            if users[current_user]["cards"][questian].lower().strip() == answerr.lower().strip() and rezultat<30:
                print("Молодец!Правильно.")
            elif users[current_user]["cards"][questian].lower().strip() == answerr.lower().strip() and rezultat>30:
                print('Ты не успел. Попробуй еще раз.')
            else:
                print('К сожалению это не правильный ответ. Попробуй еще раз.')
def add_cards():
    stop_flag = ""
    while stop_flag != 'stop':
        stop_flag = input("Введи'stop' чтобы закончит добавление карточек, Enter чтобы продолжть")
        if stop_flag=='stop':
            break
        question=input('Введите свой вопрос:')
        answer=input('Введите ответ на вопрос:')
        users[current_user]["cards"][question]=answer
        with open("users.json", "w", encoding="utf-8") as file:
            json.dump(users, file, ensure_ascii=False)
def show_cards():
    if len(users[current_user]["cards"]) == 0:
        print('Создай карточки')
        return
    else:
        print(users[current_user]["cards"])
def vihod_s_akkaunta():
    global current_user
    current_user=None
while True:
    р_или_в = int(input('2-выход 1-регистрация 0-вход:'))
    while р_или_в not in [0, 1, 2]:
        print("Error")
        р_или_в = int(input("2-выход 1-регистрация 0-вход:"))
    if р_или_в == 1:
        register()
    elif р_или_в == 2:
        break
    else:
        login()
    if current_user is not None:
        while current_user is not None:
            выбор = int(input("1-Мои карточки\n2-Создать карточки\n3-Викторина\n4-Выход из аккаунта"))
            if выбор == 1:
                show_cards()
            elif выбор == 2:
                add_cards()
            elif выбор == 3:
                viktorina()
            elif выбор == 4:
                vihod_s_akkaunta()
            else:
                print("error")
                выбор = int(input("1-Мои карточки\n2-Создать карточки\n3-Викторина\n4-Выход из аккаунта"))