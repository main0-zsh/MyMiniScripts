try:
    number1 = 100
    number2 = int(input("Введите число, которое будет поделена на 100:"))
    number3=number1/number2
    print(number3)
except ValueError:
    print("Введите корректное число")
except ZeroDivisionError:
    print("Введите число больше нуля")
except BaseException:
    print("Неизвестная ошибка")
finally:
    print("Программа завершена")
