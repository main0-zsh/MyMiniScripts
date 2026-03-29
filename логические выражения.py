age=int(input("Enter your age:"))
if age>=18:
    print("You can get a driver's license.")
else:
    print("You can't get a driver's license.")

your_apples=int(input("How many apples do you have?:"))
friend_apples=int(input("How many apples does a friend have?:"))
if your_apples>friend_apples:
    print("You has more apples than your friend.")
elif your_apples==friend_apples:
    print("You have the same number of apples.")
else:
    print("Your friend has more apples than you.")