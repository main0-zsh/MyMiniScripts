def numbers(число1,число2):
    return число1-число2
разность=numbers(67,32)
print(разность)


def age():
    guess_age = int(input("Enter your age:"))
    if guess_age >=18:
        print("You are an adult.")
    else:
        print("You are a minor.")
age()