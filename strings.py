mail=input("Введите вашу почту:")
end=len(mail)
start=mail.find('@')
domen=mail[start:end]
print(domen)