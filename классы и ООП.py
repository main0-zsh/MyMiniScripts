class Person:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f'Привет! Меня зовут {self.name} и мне {self.age} лет')
челик1=Person("Султан",15)
print(f'Имя:{челик1.name}\nВозраст:{челик1.age}')
Person.introduce(челик1)

челик2=Person("Адиль",13)
print(f'Имя:{челик2.name}\nВозраст:{челик2.age}')
Person.introduce(челик2)

class Peerson:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f'Привет! Меня зовут {self.name} и мне {self.age} лет')
    def new_age(self):
        self.age+=1
челик3=Person("Бекжан",12)
print(f'Имя:{челик3.name}\nВозраст:{челик3.age} лет')
Peerson.new_age(челик3)
Peerson.introduce(челик3)

челик4=Person("Алинур",14)
print(f'Имя:{челик4.name}\nВозраст:{челик4.age}')
Peerson.new_age(челик4)
Person.introduce(челик4)

